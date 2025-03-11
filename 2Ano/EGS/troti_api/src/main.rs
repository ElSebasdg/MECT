use warp::{Filter, http::StatusCode, Rejection, Reply, reject};
use serde::{Deserialize, Serialize};
use tokio_postgres::{NoTls, Client};
use std::sync::Arc;
use tokio::sync::Mutex;
use utoipa::{OpenApi, ToSchema};
use warp::http::Method;
use std::convert::Infallible;
use std::collections::HashMap;
use futures::{StreamExt, SinkExt};
use tokio::sync::broadcast;
use warp::ws::{Message, WebSocket};

/// Scooter representation
#[derive(Serialize, Deserialize, Debug, ToSchema, Clone)]
struct Scooter {
    /// Unique ID, automatically generated
    #[schema(nullable = true)]
    id: Option<i32>,
    /// Device MAC address
    mac_address: String,
    /// Scooter serial number
    serial_number: String,
    /// Battery percentage (0-100)
    battery_percentage: i16,
    /// Latitude coordinate
    latitude: f64,
    /// Longitude coordinate
    longitude: f64,
    /// Availability status (true = available, false = not available)
    available: bool,
}

/// Location update for WebSocket
#[derive(Serialize, Deserialize, Debug, Clone)]
struct LocationUpdate {
    /// Scooter ID
    id: i32,
    /// New latitude
    latitude: f64,
    /// New longitude
    longitude: f64,
}

/// Generic response message
#[derive(Serialize, Deserialize, ToSchema)]
struct ApiResponse {
    /// Informative message
    message: String,
}

/// Error message
#[derive(Serialize, Deserialize, ToSchema)]
struct ErrorResponse {
    /// Error description
    error: String,
}

/// Availability update request
#[derive(Serialize, Deserialize, ToSchema)]
struct AvailabilityUpdate {
    /// Whether the scooter is available for rental
    available: bool,
}

// Custom rejection type for handling database errors
#[derive(Debug)]
struct DatabaseError(String);
impl reject::Reject for DatabaseError {}

// Custom rejection for not found errors
#[derive(Debug)]
struct NotFoundError(String);
impl reject::Reject for NotFoundError {}

#[derive(OpenApi)]
#[openapi(
    info(
        title = "Scooter API",
        version = "1.0.0",
        description = "API for managing electric scooters"
    ),
    paths(
        get_scooters,
        get_scooter,
        add_scooter,
        update_scooter,
        delete_scooter,
        update_scooter_availability
    ),
    components(
        schemas(Scooter, ApiResponse, ErrorResponse, AvailabilityUpdate)
    ),
    tags(
        (name = "scooters", description = "Scooter management API")
    )
)]
struct ApiDoc;

type Db = Arc<Mutex<Client>>;
type Clients = Arc<Mutex<HashMap<String, broadcast::Sender<LocationUpdate>>>>;

async fn setup_database() -> Db {
    let mut retries = 5;
    while retries > 0 {
        match tokio_postgres::connect("host=db user=postgres password=postgres dbname=postgres", NoTls).await {
            Ok((client, connection)) => {
                tokio::spawn(async move {
                    if let Err(e) = connection.await {
                        eprintln!("Database connection error: {}", e);
                    }
                });

                let client_arc = Arc::new(Mutex::new(client));
                
                // Create table if it doesn't exist
                let create_table = "
                CREATE TABLE IF NOT EXISTS scooters (
                    id SERIAL PRIMARY KEY,
                    mac_address TEXT NOT NULL,
                    serial_number TEXT NOT NULL,
                    battery_percentage SMALLINT NOT NULL,
                    latitude DOUBLE PRECISION NOT NULL,
                    longitude DOUBLE PRECISION NOT NULL,
                    available BOOLEAN NOT NULL DEFAULT TRUE
                )";
                
                {
                    let client_lock = client_arc.lock().await;
                    if let Err(e) = client_lock.execute(create_table, &[]).await {
                        eprintln!("Error creating table: {}", e);
                    }
                    
                    // Check if the available column exists, if not add it
                    // This is for backward compatibility with existing databases
                    let check_column = "
                    DO $$
                    BEGIN
                        IF NOT EXISTS (
                            SELECT 1 
                            FROM information_schema.columns 
                            WHERE table_name='scooters' AND column_name='available'
                        ) THEN
                            ALTER TABLE scooters ADD COLUMN available BOOLEAN NOT NULL DEFAULT TRUE;
                        END IF;
                    END $$;";
                    
                    if let Err(e) = client_lock.execute(check_column, &[]).await {
                        eprintln!("Error checking/adding available column: {}", e);
                    }
                } // lock is released here
                
                return client_arc;
            }
            Err(e) => {
                eprintln!("Connection attempt failed: {}. Trying again...", e);
                tokio::time::sleep(std::time::Duration::from_secs(5)).await;
                retries -= 1;
            }
        }
    }
    panic!("Failed to connect to database after several attempts.");
}

// Custom error handler
async fn handle_rejection(err: Rejection) -> Result<impl Reply, Infallible> {
    let (code, message) = if err.is_not_found() {
        (StatusCode::NOT_FOUND, "Not Found: The requested resource doesn't exist".to_string())
    } else if let Some(e) = err.find::<NotFoundError>() {
        (StatusCode::NOT_FOUND, format!("Not Found: {}", e.0))
    } else if let Some(e) = err.find::<DatabaseError>() {
        (StatusCode::INTERNAL_SERVER_ERROR, format!("Database error: {}", e.0))
    } else if let Some(_) = err.find::<warp::filters::body::BodyDeserializeError>() {
        (StatusCode::BAD_REQUEST, "Invalid request data format".to_string())
    } else if let Some(_) = err.find::<warp::filters::ws::MissingConnectionUpgrade>() {
        (StatusCode::BAD_REQUEST, "WebSocket upgrade required".to_string())
    } else {
        (StatusCode::INTERNAL_SERVER_ERROR, "Internal Server Error".to_string())
    };

    // Create HTML response for errors
    let html = format!(
        r#"<!DOCTYPE html>
        <html>
            <head>
                <title>Error {}</title>
                <style>
                    body {{ 
                        font-family: Arial, sans-serif; 
                        margin: 0;
                        padding: 20px;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        justify-content: center;
                        min-height: 80vh;
                    }}
                    .error-container {{
                        background-color: #f8d7da;
                        color: #721c24;
                        padding: 20px;
                        border-radius: 5px;
                        border: 1px solid #f5c6cb;
                        max-width: 600px;
                        text-align: center;
                    }}
                    h1 {{ margin-top: 0; }}
                    p {{ margin-bottom: 0; }}
                </style>
            </head>
            <body>
                <div class="error-container">
                    <h1>Error {}</h1>
                    <p>{}</p>
                </div>
            </body>
        </html>"#,
        code.as_u16(),
        code.as_u16(),
        message
    );

    // Create a response with the HTML and appropriate status code
    Ok(warp::reply::with_status(
        warp::reply::html(html),
        code
    ))
}

// Handle WebSocket connection for a specific scooter
async fn handle_ws_client(ws: WebSocket, id: i32, clients: Clients, db: Db) {
    println!("New WebSocket client connected for scooter ID: {}", id);
    
    // Split the WebSocket into sender and receiver
    let (mut ws_tx, mut ws_rx) = ws.split();
    
    // Create a channel for this specific scooter if it doesn't exist
    let (tx, _rx) = {
        let mut clients = clients.lock().await;
        let channel_name = format!("scooter-{}", id);
        
        match clients.get(&channel_name) {
            Some(sender) => {
                let tx = sender.clone();
                // Create a new receiver from the existing sender
                let rx = tx.subscribe();
                (tx, rx)
            },
            None => {
                // Create a new channel
                let (tx, rx) = broadcast::channel::<LocationUpdate>(100);
                clients.insert(channel_name, tx.clone());
                (tx, rx)
            }
        }
    };
    
    // Create a new receiver to receive updates
    let mut rx = tx.subscribe();
    
    // Check if scooter exists
    {
        let client = db.lock().await;
        match client.query_opt("SELECT * FROM scooters WHERE id = $1", &[&id]).await {
            Ok(None) => {
                let error_msg = format!("Scooter with ID {} not found", id);
                let _ = ws_tx.send(Message::text(error_msg)).await;
                return;
            },
            Err(e) => {
                let error_msg = format!("Database error: {}", e);
                let _ = ws_tx.send(Message::text(error_msg)).await;
                return;
            },
            _ => {} // Scooter found, continue
        }
    }
    
    // Initial data send
    {
        let client = db.lock().await;
        match client.query_opt("SELECT * FROM scooters WHERE id = $1", &[&id]).await {
            Ok(Some(row)) => {
                let scooter = Scooter {
                    id: row.get(0),
                    mac_address: row.get(1),
                    serial_number: row.get(2),
                    battery_percentage: row.get(3),
                    latitude: row.get(4),
                    longitude: row.get(5),
                    available: row.get(6),
                };
                
                if let Ok(json) = serde_json::to_string(&scooter) {
                    let _ = ws_tx.send(Message::text(json)).await;
                }
            },
            _ => {} // Already checked above, shouldn't happen
        }
    }
    
    // Handle incoming messages from the WebSocket client
    let db_clone = db.clone();
    let tx_clone = tx.clone();
    
    // This task handles incoming messages from WebSocket to update location
    let mut incoming = tokio::spawn(async move {
        while let Some(result) = ws_rx.next().await {
            match result {
                Ok(msg) => {
                    if let Ok(txt) = msg.to_str() {
                        // Try to parse the incoming message as a LocationUpdate
                        if let Ok(update) = serde_json::from_str::<LocationUpdate>(txt) {
                            // Update the database with new location
                            let db = db_clone.lock().await;
                            match db.execute(
                                "UPDATE scooters SET latitude = $1, longitude = $2 WHERE id = $3",
                                &[&update.latitude, &update.longitude, &update.id],
                            ).await {
                                Ok(rows) => {
                                    if rows > 0 {
                                        // Broadcast the update to all connected clients
                                        let _ = tx_clone.send(update);
                                    }
                                },
                                Err(e) => {
                                    eprintln!("Error updating location: {}", e);
                                }
                            }
                        }
                    }
                },
                Err(e) => {
                    eprintln!("WebSocket error: {}", e);
                    break;
                }
            }
        }
    });
    
    // This task forwards broadcasted updates to this WebSocket client
    let mut outgoing = tokio::spawn(async move {
        while let Ok(update) = rx.recv().await {
            // Only forward updates for this scooter
            if update.id == id {
                if let Ok(json) = serde_json::to_string(&update) {
                    if let Err(e) = ws_tx.send(Message::text(json)).await {
                        eprintln!("Error sending WebSocket message: {}", e);
                        break;
                    }
                }
            }
        }
    });
    
    // Wait for either task to finish
    tokio::select! {
        _ = (&mut outgoing) => incoming.abort(),
        _ = (&mut incoming) => outgoing.abort(),
    }
    
    println!("WebSocket client disconnected for scooter ID: {}", id);
}

// Handle WebSocket connection for all scooters
async fn handle_ws_all_client(ws: WebSocket, clients: Clients, db: Db) {
    println!("New WebSocket client connected for all scooters");
    
    // Split the WebSocket into sender and receiver
    let (mut ws_tx, mut ws_rx) = ws.split();
    
    // Create a channel for "all scooters" if it doesn't exist
    let (tx, mut rx) = {
        let mut clients = clients.lock().await;
        let channel_name = "all-scooters".to_string();
        
        match clients.get(&channel_name) {
            Some(sender) => {
                let tx = sender.clone();
                // Create a new receiver from the existing sender
                let rx = tx.subscribe();
                (tx, rx)
            },
            None => {
                // Create a new channel
                let (tx, rx) = broadcast::channel::<LocationUpdate>(100);
                clients.insert(channel_name, tx.clone());
                (tx, rx)
            }
        }
    };
    
    // Initial data send - all scooters
    {
        let client = db.lock().await;
        match client.query("SELECT * FROM scooters", &[]).await {
            Ok(rows) => {
                let scooters: Vec<Scooter> = rows
                    .iter()
                    .map(|row| Scooter {
                        id: row.get(0),
                        mac_address: row.get(1),
                        serial_number: row.get(2),
                        battery_percentage: row.get(3),
                        latitude: row.get(4),
                        longitude: row.get(5),
                        available: row.get(6),
                    })
                    .collect();
                
                if let Ok(json) = serde_json::to_string(&scooters) {
                    let _ = ws_tx.send(Message::text(json)).await;
                }
            },
            Err(e) => {
                let error_msg = format!("Database error: {}", e);
                let _ = ws_tx.send(Message::text(error_msg)).await;
                return;
            }
        }
    }
    
    // Handle incoming messages from the WebSocket client
    let db_clone = db.clone();
    let tx_clone = tx.clone();
    let clients_clone = clients.clone();
    
    // This task handles incoming messages from WebSocket to update location
    let mut incoming = tokio::spawn(async move {
        while let Some(result) = ws_rx.next().await {
            match result {
                Ok(msg) => {
                    if let Ok(txt) = msg.to_str() {
                        // Try to parse the incoming message as a LocationUpdate
                        if let Ok(update) = serde_json::from_str::<LocationUpdate>(txt) {
                            // Update the database with new location
                            let db = db_clone.lock().await;
                            match db.execute(
                                "UPDATE scooters SET latitude = $1, longitude = $2 WHERE id = $3",
                                &[&update.latitude, &update.longitude, &update.id],
                            ).await {
                                Ok(rows) => {
                                    if rows > 0 {
                                        // Broadcast the update to all connected clients
                                        let _ = tx_clone.send(update.clone());
                                        
                                        // Also forward to the specific scooter channel
                                        let mut clients = clients_clone.lock().await;
                                        let channel_name = format!("scooter-{}", update.id);
                                        if let Some(sender) = clients.get(&channel_name) {
                                            let _ = sender.send(update);
                                        }
                                    }
                                },
                                Err(e) => {
                                    eprintln!("Error updating location: {}", e);
                                }
                            }
                        }
                    }
                },
                Err(e) => {
                    eprintln!("WebSocket error: {}", e);
                    break;
                }
            }
        }
    });
    
    // This task forwards broadcasted updates to this WebSocket client
    let mut outgoing = tokio::spawn(async move {
        while let Ok(update) = rx.recv().await {
            if let Ok(json) = serde_json::to_string(&update) {
                if let Err(e) = ws_tx.send(Message::text(json)).await {
                    eprintln!("Error sending WebSocket message: {}", e);
                    break;
                }
            }
        }
    });
    
    // Wait for either task to finish
    tokio::select! {
        _ = (&mut outgoing) => incoming.abort(),
        _ = (&mut incoming) => outgoing.abort(),
    }
    
    println!("WebSocket client disconnected for all scooters");
}

#[tokio::main]
async fn main() {
    let db = setup_database().await;
    let db_filter = warp::any().map(move || db.clone());
    
    // HashMap to store broadcasters for WebSocket connections
    let clients: Clients = Arc::new(Mutex::new(HashMap::new()));
    let clients_filter = warp::any().map(move || clients.clone());

    // CORS configuration
    let cors = warp::cors()
        .allow_any_origin()
        .allow_methods(&[Method::GET, Method::POST, Method::PUT, Method::DELETE, Method::PATCH])
        .allow_headers(vec!["content-type"]);

    // WebSocket routes
    let ws_route = warp::path!("ws" / "scooters" / i32)
        .and(warp::ws())
        .and(clients_filter.clone())
        .and(db_filter.clone())
        .map(|id: i32, ws: warp::ws::Ws, clients, db| {
            ws.on_upgrade(move |socket| handle_ws_client(socket, id, clients, db))
        });
        
    let ws_all_route = warp::path!("ws" / "scooters")
        .and(warp::ws())
        .and(clients_filter.clone())
        .and(db_filter.clone())
        .map(|ws: warp::ws::Ws, clients, db| {
            ws.on_upgrade(move |socket| handle_ws_all_client(socket, clients, db))
        });

    // REST API routes with v1 prefix
    let get_one = warp::path!("v1" / "scooters" / i32)
        .and(warp::get())
        .and(db_filter.clone())
        .and_then(get_scooter);

    let get_all = warp::path!("v1" / "scooters")
        .and(warp::get())
        .and(warp::path::end())
        .and(db_filter.clone())
        .and_then(get_scooters);

    let add = warp::path!("v1" / "scooters")
        .and(warp::post())
        .and(warp::path::end())
        .and(warp::body::json())
        .and(db_filter.clone())
        .and_then(add_scooter);

    let update = warp::path!("v1" / "scooters" / i32)
        .and(warp::put())
        .and(warp::body::json())
        .and(db_filter.clone())
        .and_then(update_scooter);

    let delete = warp::path!("v1" / "scooters" / i32)
        .and(warp::delete())
        .and(db_filter.clone())
        .and_then(delete_scooter);

    let update_availability = warp::path!("v1" / "scooters" / i32 / "availability")
        .and(warp::patch())
        .and(warp::body::json())
        .and(db_filter.clone())
        .and_then(update_scooter_availability);

    // Combine all routes for the API
    let api_routes = get_one
        .or(get_all)
        .or(add)
        .or(update)
        .or(delete)
        .or(update_availability) 
        .with(cors.clone());

    // Generate OpenAPI documentation
    let openapi = ApiDoc::openapi();

    // Endpoint for OpenAPI JSON
    let api_doc = warp::path("api-doc")
        .and(warp::path("openapi.json"))
        .and(warp::get())
        .map(move || warp::reply::json(&openapi));

    // Route to serve Swagger UI
    let swagger_ui = warp::path("swagger-ui")
        .and(warp::get())
        .and(warp::fs::dir("./swagger-ui-dist"));

    // Create page for WebSocket testing
    let websocket_test_page = warp::path("websocket-test")
        .and(warp::get())
        .map(|| {
            warp::http::Response::builder()
                .header("content-type", "text/html")
                .body(r#"
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <title>Scooter WebSocket Test</title>
                        <style>
                            body {
                                font-family: Arial, sans-serif;
                                max-width: 800px;
                                margin: 0 auto;
                                padding: 20px;
                            }
                            .container {
                                display: flex;
                                flex-direction: column;
                                gap: 20px;
                            }
                            .card {
                                border: 1px solid #ddd;
                                border-radius: 8px;
                                padding: 15px;
                                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                            }
                            h1, h2 {
                                color: #333;
                            }
                            button {
                                padding: 8px 16px;
                                background-color: #4CAF50;
                                color: white;
                                border: none;
                                border-radius: 4px;
                                cursor: pointer;
                                margin-right: 10px;
                            }
                            button:hover {
                                background-color: #45a049;
                            }
                            input, select {
                                padding: 8px;
                                margin: 5px 0;
                                border: 1px solid #ddd;
                                border-radius: 4px;
                            }
                            .form-group {
                                margin-bottom: 15px;
                            }
                            #messages {
                                height: 200px;
                                overflow-y: auto;
                                border: 1px solid #ddd;
                                padding: 10px;
                                background-color: #f9f9f9;
                                border-radius: 4px;
                            }
                            .message {
                                margin-bottom: 8px;
                                padding: 8px;
                                border-radius: 4px;
                            }
                            .received {
                                background-color: #e3f2fd;
                            }
                            .sent {
                                background-color: #e8f5e9;
                            }
                            #map {
                                height: 400px;
                                width: 100%;
                                border-radius: 8px;
                                margin-top: 20px;
                            }
                        </style>
                    </head>
                    <body>
                        <h1>Scooter WebSocket Test</h1>
                        
                        <div class="container">
                            <div class="card">
                                <h2>Connection</h2>
                                <div class="form-group">
                                    <label for="connectionType">Connection Type:</label>
                                    <select id="connectionType">
                                        <option value="all">All Scooters</option>
                                        <option value="single">Single Scooter</option>
                                    </select>
                                </div>
                                
                                <div class="form-group" id="scooterIdGroup">
                                    <label for="scooterId">Scooter ID:</label>
                                    <input type="number" id="scooterId" min="1" value="1">
                                </div>
                                
                                <button id="connectBtn">Connect</button>
                                <button id="disconnectBtn" disabled>Disconnect</button>
                                <span id="status">Disconnected</span>
                            </div>
                            
                            <div class="card">
                                <h2>Send Location Update</h2>
                                <div class="form-group">
                                    <label for="updateScooterId">Scooter ID:</label>
                                    <input type="number" id="updateScooterId" min="1" value="1">
                                </div>
                                <div class="form-group">
                                    <label for="latitude">Latitude:</label>
                                    <input type="number" id="latitude" step="0.000001" value="41.1579">
                                </div>
                                <div class="form-group">
                                    <label for="longitude">Longitude:</label>
                                    <input type="number" id="longitude" step="0.000001" value="-8.6291">
                                </div>
                                <button id="sendUpdateBtn" disabled>Send Update</button>
                            </div>
                            
                            <div class="card">
                                <h2>Messages</h2>
                                <div id="messages"></div>
                            </div>
                            
                            <div class="card">
                                <h2>Map</h2>
                                <div id="map"></div>
                            </div>
                        </div>
                        
                        <script>
                            let socket;
                            let map;
                            let markers = {};
                            
                            document.getElementById('connectionType').addEventListener('change', function() {
                                const isSingleScooter = this.value === 'single';
                                document.getElementById('scooterIdGroup').style.display = isSingleScooter ? 'block' : 'none';
                            });
                            
                            document.getElementById('connectBtn').addEventListener('click', function() {
                                const connectionType = document.getElementById('connectionType').value;
                                let wsUrl;
                                
                                if (connectionType === 'single') {
                                    const scooterId = document.getElementById('scooterId').value;
                                    wsUrl = `ws://${window.location.host}/ws/scooters/${scooterId}`;
                                } else {
                                    wsUrl = `ws://${window.location.host}/ws/scooters`;
                                }
                                
                                socket = new WebSocket(wsUrl);
                                
                                socket.onopen = function(e) {
                                    document.getElementById('status').textContent = 'Connected';
                                    document.getElementById('connectBtn').disabled = true;
                                    document.getElementById('disconnectBtn').disabled = false;
                                    document.getElementById('sendUpdateBtn').disabled = false;
                                    addMessage('Connected to WebSocket server', 'system');
                                };
                                
                                socket.onmessage = function(event) {
                                    const data = event.data;
                                    addMessage('Received: ' + data, 'received');
                                    
                                    try {
                                        const jsonData = JSON.parse(data);
                                        
                                        // Check if it's an array (initial data for all scooters)
                                        if (Array.isArray(jsonData)) {
                                            // Clear existing markers
                                            for (const key in markers) {
                                                markers[key].setMap(null);
                                            }
                                            markers = {};
                                            
                                            // Add markers for all scooters
                                            jsonData.forEach(scooter => {
                                                if (scooter.id) {
                                                    addOrUpdateMarker(scooter.id, scooter.latitude, scooter.longitude);
                                                }
                                            });
                                            
                                            // If we have at least one scooter, center the map on it
                                            if (jsonData.length > 0) {
                                                map.setCenter({
                                                    lat: jsonData[0].latitude,
                                                    lng: jsonData[0].longitude
                                                });
                                            }
                                        } 
                                        // Single scooter initial data
                                        else if (jsonData.id && jsonData.latitude && jsonData.longitude) {
                                            addOrUpdateMarker(jsonData.id, jsonData.latitude, jsonData.longitude);
                                            map.setCenter({
                                                lat: jsonData.latitude,
                                                lng: jsonData.longitude
                                            });
                                        }
                                        // Location update
                                        else if (jsonData.id && jsonData.latitude && jsonData.longitude) {
                                            addOrUpdateMarker(jsonData.id, jsonData.latitude, jsonData.longitude);
                                        }
                                    } catch (e) {
                                        console.error('Error parsing JSON:', e);
                                    }
                                };
                                
                                socket.onclose = function(event) {
                                    if (event.wasClean) {
                                        addMessage(`Connection closed cleanly, code=${event.code} reason=${event.reason}`, 'system');
                                    } else {
                                        addMessage('Connection died', 'system');
                                    }
                                    
                                    document.getElementById('status').textContent = 'Disconnected';
                                    document.getElementById('connectBtn').disabled = false;
                                    document.getElementById('disconnectBtn').disabled = true;
                                    document.getElementById('sendUpdateBtn').disabled = true;
                                };
                                
                                socket.onerror = function(error) {
                                    addMessage(`Error: ${error
socket.onerror = function(error) {
                                    addMessage(`Error: ${error.message}`, 'system');
                                };
                            });
                            
                            document.getElementById('disconnectBtn').addEventListener('click', function() {
                                if (socket) {
                                    socket.close();
                                    document.getElementById('status').textContent = 'Disconnected';
                                    document.getElementById('connectBtn').disabled = false;
                                    document.getElementById('disconnectBtn').disabled = true;
                                    document.getElementById('sendUpdateBtn').disabled = true;
                                }
                            });
                            
                            document.getElementById('sendUpdateBtn').addEventListener('click', function() {
                                if (socket && socket.readyState === WebSocket.OPEN) {
                                    const update = {
                                        id: parseInt(document.getElementById('updateScooterId').value),
                                        latitude: parseFloat(document.getElementById('latitude').value),
                                        longitude: parseFloat(document.getElementById('longitude').value)
                                    };
                                    
                                    const json = JSON.stringify(update);
                                    socket.send(json);
                                    addMessage('Sent: ' + json, 'sent');
                                }
                            });
                            
                            function addMessage(message, type) {
                                const messagesDiv = document.getElementById('messages');
                                const messageElement = document.createElement('div');
                                messageElement.classList.add('message', type);
                                messageElement.textContent = message;
                                messagesDiv.appendChild(messageElement);
                                messagesDiv.scrollTop = messagesDiv.scrollHeight;
                            }
                            
                            function addOrUpdateMarker(id, lat, lng) {
                                if (!map) return;
                                
                                if (markers[id]) {
                                    // Update existing marker
                                    markers[id].setPosition({
                                        lat: lat,
                                        lng: lng
                                    });
                                } else {
                                    // Create new marker
                                    markers[id] = new google.maps.Marker({
                                        position: {
                                            lat: lat,
                                            lng: lng
                                        },
                                        map: map,
                                        title: `Scooter ${id}`
                                    });
                                }
                            }
                           
                    </body>
                    </html>
                "#)
        });

    // Home page redirecting to Swagger
    let index = warp::path::end()
        .map(|| {
            warp::http::Response::builder()
                .header("content-type", "text/html")
                .body(r#"
                    <html>
                        <head>
                            <meta http-equiv="refresh" content="0;url=/swagger-ui" />
                        </head>
                        <body>
                            <p>Redirecting to <a href="/swagger-ui">Swagger UI</a>...</p>
                            <p>WebSocket test page available at <a href="/websocket-test">WebSocket Test</a></p>
                        </body>
                    </html>
                "#)
        });

    // Combine all routes
    let routes = api_routes
        .or(ws_route)
        .or(ws_all_route)
        .or(api_doc)
        .or(swagger_ui)
        .or(websocket_test_page)
        .or(index)
        .with(cors)
        .recover(handle_rejection);

    println!("Server running at http://127.0.0.1:8080");
    println!("API documentation available at http://127.0.0.1:8080/api-doc/openapi.json");
    println!("Swagger UI at http://127.0.0.1:8080/swagger-ui");
    println!("WebSocket test page at http://127.0.0.1:8080/websocket-test");
    
    // Create directory for Swagger UI
    if !std::path::Path::new("./swagger-ui-dist").exists() {
        std::fs::create_dir("./swagger-ui-dist").expect("Failed to create swagger-ui-dist directory");
        
        // Create index.html file for Swagger UI
        let index_html = r#"
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <title>Scooter API - Swagger UI</title>
            <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@4.5.0/swagger-ui.css" />
        </head>
        <body>
            <div id="swagger-ui"></div>
            <script src="https://unpkg.com/swagger-ui-dist@4.5.0/swagger-ui-bundle.js"></script>
            <script>
                window.onload = () => {
                    window.ui = SwaggerUIBundle({
                        url: '/api-doc/openapi.json',
                        dom_id: '#swagger-ui',
                        presets: [
                            SwaggerUIBundle.presets.apis,
                            SwaggerUIBundle.SwaggerUIStandalonePreset
                        ],
                        layout: "BaseLayout",
                        deepLinking: true
                    });
                };
            </script>
        </body>
        </html>
        "#;
        
        std::fs::write("./swagger-ui-dist/index.html", index_html)
            .expect("Failed to create index.html file for Swagger UI");
    }
    
    warp::serve(routes).run(([0, 0, 0, 0], 8080)).await;
}

/// Get all scooters
///
/// Returns a list of all scooters available in the system.
#[utoipa::path(
    get,
    path = "/v1/scooters",
    responses(
        (status = 200, description = "List of scooters retrieved successfully", body = Vec<Scooter>)
    ),
    tag = "scooters"
)]
async fn get_scooters(db: Db) -> Result<impl Reply, Rejection> {
    let client = db.lock().await;
    println!("Executing get_scooters - retrieving all scooters");
    match client.query("SELECT * FROM scooters", &[]).await {
        Ok(rows) => {
            let scooters: Vec<Scooter> = rows
                .iter()
                .map(|row| Scooter {
                    id: row.get(0),
                    mac_address: row.get(1),
                    serial_number: row.get(2),
                    battery_percentage: row.get(3),
                    latitude: row.get(4),
                    longitude: row.get(5),
                    available: row.get(6),
                })
                .collect();

            println!("Returning {} scooters", scooters.len());
            Ok(warp::reply::json(&scooters))
        },
        Err(e) => {
            eprintln!("Error retrieving scooters: {}", e);
            Err(reject::custom(DatabaseError(e.to_string())))
        }
    }
}

/// Get a specific scooter by ID
///
/// Returns the details of a specific scooter based on the provided ID.
#[utoipa::path(
    get,
    path = "/v1/scooters/{id}",
    responses(
        (status = 200, description = "Scooter found successfully", body = Scooter),
        (status = 404, description = "Scooter not found", body = ErrorResponse)
    ),
    params(
        ("id" = i32, Path, description = "Scooter ID")
    ),
    tag = "scooters"
)]
async fn get_scooter(id: i32, db: Db) -> Result<impl Reply, Rejection> {
    let client = db.lock().await;
    println!("Executing get_scooter - retrieving scooter with ID: {}", id);
    
    match client.query_opt("SELECT * FROM scooters WHERE id = $1", &[&id]).await {
        Ok(Some(row)) => {
            println!("Scooter found with ID: {}", id);
            let scooter = Scooter {
                id: row.get(0),
                mac_address: row.get(1),
                serial_number: row.get(2),
                battery_percentage: row.get(3),
                latitude: row.get(4),
                longitude: row.get(5),
                available: row.get(6),
            };
            Ok(warp::reply::json(&scooter))
        },
        Ok(None) => {
            println!("Scooter with ID {} not found", id);
            // Return custom Not Found rejection with HTML response
            Err(reject::custom(NotFoundError(format!("Scooter with ID {} not found", id))))
        },
        Err(e) => {
            eprintln!("Database error while looking up scooter: {}", e);
            Err(reject::custom(DatabaseError(e.to_string())))
        }
    }
}

/// Add a new scooter
///
/// Creates a new scooter with the provided data.
#[utoipa::path(
    post,
    path = "/v1/scooters",
    request_body = Scooter,
    responses(
        (status = 201, description = "Scooter created successfully", body = ApiResponse),
        (status = 400, description = "Invalid input data", body = ErrorResponse),
        (status = 500, description = "Server error", body = ErrorResponse)
    ),
    tag = "scooters"
)]
async fn add_scooter(new_scooter: Scooter, db: Db) -> Result<impl Reply, Rejection> {
    let client = db.lock().await;
    
    // Validate input data
    if new_scooter.battery_percentage < 0 || new_scooter.battery_percentage > 100 {
        return Err(reject::custom(
            NotFoundError("Battery percentage must be between 0 and 100".to_string())
        ));
    }

    match client
        .execute(
            "INSERT INTO scooters (mac_address, serial_number, battery_percentage, latitude, longitude, available) 
             VALUES ($1, $2, $3, $4, $5, $6)",
            &[
                &new_scooter.mac_address,
                &new_scooter.serial_number,
                &new_scooter.battery_percentage,
                &new_scooter.latitude,
                &new_scooter.longitude,
                &new_scooter.available,
            ],
        )
        .await {
            Ok(_) => {
                Ok(warp::reply::with_status(
                    warp::reply::json(&ApiResponse { message: "Scooter created".to_string() }),
                    StatusCode::CREATED,
                ))
            },
            Err(e) => {
                eprintln!("Error creating scooter: {}", e);
                Err(reject::custom(DatabaseError(e.to_string())))
            }
        }
}

/// Update an existing scooter
///
/// Updates the data of an existing scooter based on the provided ID.
#[utoipa::path(
    put,
    path = "/v1/scooters/{id}",
    request_body = Scooter,
    responses(
        (status = 200, description = "Scooter updated successfully", body = ApiResponse),
        (status = 404, description = "Scooter not found", body = ErrorResponse)
    ),
    params(
        ("id" = i32, Path, description = "Scooter ID")
    ),
    tag = "scooters"
)]
async fn update_scooter(id: i32, updated_scooter: Scooter, db: Db) -> Result<impl Reply, Rejection> {
    let client = db.lock().await;

    // Validate input data
    if updated_scooter.battery_percentage < 0 || updated_scooter.battery_percentage > 100 {
        return Err(reject::custom(
            NotFoundError("Battery percentage must be between 0 and 100".to_string())
        ));
    }

    match client
        .execute(
            "UPDATE scooters SET mac_address = $1, serial_number = $2, battery_percentage = $3, latitude = $4, longitude = $5, available = $6 WHERE id = $7",
            &[
                &updated_scooter.mac_address,
                &updated_scooter.serial_number,
                &updated_scooter.battery_percentage,
                &updated_scooter.latitude,
                &updated_scooter.longitude,
                &updated_scooter.available,
                &id,
            ],
        )
        .await {
            Ok(rows_affected) => {
                if rows_affected == 0 {
                    return Err(reject::custom(NotFoundError(format!("Scooter with ID {} not found", id))));
                }

                Ok(warp::reply::with_status(
                    warp::reply::json(&ApiResponse { message: "Scooter updated".to_string() }),
                    StatusCode::OK,
                ))
            },
            Err(e) => {
                eprintln!("Error updating scooter: {}", e);
                Err(reject::custom(DatabaseError(e.to_string())))
            }
        }
}

/// Delete a scooter
///
/// Removes a scooter from the system based on the provided ID.
#[utoipa::path(
    delete,
    path = "/v1/scooters/{id}",
    responses(
        (status = 200, description = "Scooter deleted successfully", body = ApiResponse),
        (status = 404, description = "Scooter not found", body = ErrorResponse)
    ),
    params(
        ("id" = i32, Path, description = "Scooter ID")
    ),
    tag = "scooters"
)]
async fn delete_scooter(id: i32, db: Db) -> Result<impl Reply, Rejection> {
    let client = db.lock().await;
    match client.execute("DELETE FROM scooters WHERE id = $1", &[&id]).await {
        Ok(rows_affected) => {
            if rows_affected == 0 {
                return Err(reject::custom(NotFoundError(format!("Scooter with ID {} not found", id))));
            }

            Ok(warp::reply::with_status(
                warp::reply::json(&ApiResponse { message: "Scooter deleted".to_string() }),
                StatusCode::OK,
            ))
        },
        Err(e) => {
            eprintln!("Error deleting scooter: {}", e);
            Err(reject::custom(DatabaseError(e.to_string())))
        }
    }
}

/// Update scooter availability
///
/// Updates only the availability status of a scooter without modifying other fields.
#[utoipa::path(
    patch,
    path = "/v1/scooters/{id}/availability",
    request_body = AvailabilityUpdate,
    responses(
        (status = 200, description = "Availability status updated successfully", body = ApiResponse),
        (status = 404, description = "Scooter not found", body = ErrorResponse),
        (status = 500, description = "Server error", body = ErrorResponse)
    ),
    params(
        ("id" = i32, Path, description = "Scooter ID")
    ),
    tag = "scooters"
)]
async fn update_scooter_availability(id: i32, update: AvailabilityUpdate, db: Db) -> Result<impl Reply, Rejection> {
    let client = db.lock().await;

    match client
        .execute(
            "UPDATE scooters SET available = $1 WHERE id = $2",
            &[&update.available, &id],
        )
        .await {
            Ok(rows_affected) => {
                if rows_affected == 0 {
                    return Err(reject::custom(NotFoundError(format!("Scooter with ID {} not found", id))));
                }

                Ok(warp::reply::with_status(
                    warp::reply::json(&ApiResponse { message: "Scooter availability updated".to_string() }),
                    StatusCode::OK,
                ))
            },
            Err(e) => {
                eprintln!("Error updating scooter availability: {}", e);
                Err(reject::custom(DatabaseError(e.to_string())))
            }
        }
}
