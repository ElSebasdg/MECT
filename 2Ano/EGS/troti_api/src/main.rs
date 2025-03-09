use warp::{Filter, http::StatusCode, Rejection, Reply};
use serde::{Deserialize, Serialize};
use tokio_postgres::{NoTls, Client};
use std::sync::Arc;
use tokio::sync::Mutex;
use utoipa::{OpenApi, ToSchema};
use warp::http::Method;

/// Scooter representation
#[derive(Serialize, Deserialize, Debug, ToSchema)]
struct Troti {
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

#[derive(OpenApi)]
#[openapi(
    info(
        title = "Scooter API",
        version = "1.0.0",
        description = "API for managing electric scooters"
    ),
    paths(
        get_trotis,
        get_troti,
        add_troti,
        update_troti,
        delete_troti
    ),
    components(
        schemas(Troti, ApiResponse, ErrorResponse)
    ),
    tags(
        (name = "scooters", description = "Scooter management API")
    )
)]
struct ApiDoc;

type Db = Arc<Mutex<Client>>;

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
                CREATE TABLE IF NOT EXISTS trotis (
                    id SERIAL PRIMARY KEY,
                    mac_address TEXT NOT NULL,
                    serial_number TEXT NOT NULL,
                    battery_percentage SMALLINT NOT NULL,
                    latitude DOUBLE PRECISION NOT NULL,
                    longitude DOUBLE PRECISION NOT NULL
                )";
                
                {
                    let client_lock = client_arc.lock().await;
                    if let Err(e) = client_lock.execute(create_table, &[]).await {
                        eprintln!("Error creating table: {}", e);
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

#[tokio::main]
async fn main() {
    let db = setup_database().await;
    let db_filter = warp::any().map(move || db.clone());

    // CORS configuration
    let cors = warp::cors()
        .allow_any_origin()
        .allow_methods(&[Method::GET, Method::POST, Method::PUT, Method::DELETE])
        .allow_headers(vec!["content-type"]);

    // API routes definition - Removed "/api" prefix
    let api_routes = warp::path("trotis")
        .and(warp::get())
        .and(db_filter.clone())
        .and_then(get_trotis)
        .or(warp::path!("trotis" / i32)
            .and(warp::get())
            .and(db_filter.clone())
            .and_then(get_troti))
        .or(warp::path("trotis")
            .and(warp::post())
            .and(warp::body::json())
            .and(db_filter.clone())
            .and_then(add_troti))
        .or(warp::path!("trotis" / i32)
            .and(warp::put())
            .and(warp::body::json())
            .and(db_filter.clone())
            .and_then(update_troti))
        .or(warp::path!("trotis" / i32)
            .and(warp::delete())
            .and(db_filter.clone())
            .and_then(delete_troti))
        .with(cors);

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
                        </body>
                    </html>
                "#)
        });

    // Combine all routes
    let routes = api_routes
        .or(api_doc)
        .or(swagger_ui)
        .or(index);

    println!("Server running at http://127.0.0.1:8080");
    println!("API documentation available at http://127.0.0.1:8080/api-doc/openapi.json");
    println!("Swagger UI at http://127.0.0.1:8080/swagger-ui");
    
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
    path = "/trotis",
    responses(
        (status = 200, description = "List of scooters retrieved successfully", body = Vec<Troti>)
    ),
    tag = "scooters"
)]
async fn get_trotis(db: Db) -> Result<impl Reply, Rejection> {
    let client = db.lock().await;
    match client.query("SELECT * FROM trotis", &[]).await {
        Ok(rows) => {
            let trotis: Vec<Troti> = rows
                .iter()
                .map(|row| Troti {
                    id: row.get(0),
                    mac_address: row.get(1),
                    serial_number: row.get(2),
                    battery_percentage: row.get(3),
                    latitude: row.get(4),
                    longitude: row.get(5),
                })
                .collect();

            Ok(warp::reply::json(&trotis))
        },
        Err(e) => {
            eprintln!("Error retrieving scooters: {}", e);
            Ok(warp::reply::json(&Vec::<Troti>::new()))
        }
    }
}

/// Get a specific scooter by ID
///
/// Returns the details of a specific scooter based on the provided ID.
#[utoipa::path(
    get,
    path = "/trotis/{id}",
    responses(
        (status = 200, description = "Scooter found successfully", body = Troti),
        (status = 404, description = "Scooter not found", body = ErrorResponse)
    ),
    params(
        ("id" = i32, Path, description = "Scooter ID")
    ),
    tag = "scooters"
)]
async fn get_troti(id: i32, db: Db) -> Result<warp::reply::WithStatus<warp::reply::Json>, Rejection> {
    let client = db.lock().await;
    match client.query_one("SELECT * FROM trotis WHERE id = $1", &[&id]).await {
        Ok(row) => {
            let troti = Troti {
                id: row.get(0),
                mac_address: row.get(1),
                serial_number: row.get(2),
                battery_percentage: row.get(3),
                latitude: row.get(4),
                longitude: row.get(5),
            };
            Ok(warp::reply::with_status(
                warp::reply::json(&troti),
                StatusCode::OK,
            ))
        }
        Err(_) => Ok(warp::reply::with_status(
            warp::reply::json(&ErrorResponse { error: "Scooter not found".to_string() }),
            StatusCode::NOT_FOUND,
        )),
    }
}

/// Add a new scooter
///
/// Creates a new scooter with the provided data.
#[utoipa::path(
    post,
    path = "/trotis",
    request_body = Troti,
    responses(
        (status = 201, description = "Scooter created successfully", body = ApiResponse)
    ),
    tag = "scooters"
)]
async fn add_troti(new_troti: Troti, db: Db) -> Result<warp::reply::WithStatus<warp::reply::Json>, Rejection> {
    let client = db.lock().await;
    match client
        .execute(
            "INSERT INTO trotis (mac_address, serial_number, battery_percentage, latitude, longitude) 
             VALUES ($1, $2, $3, $4, $5)",
            &[
                &new_troti.mac_address,
                &new_troti.serial_number,
                &new_troti.battery_percentage,
                &new_troti.latitude,
                &new_troti.longitude,
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
                Ok(warp::reply::with_status(
                    warp::reply::json(&ErrorResponse { error: format!("Error creating scooter: {}", e) }),
                    StatusCode::INTERNAL_SERVER_ERROR,
                ))
            }
        }
}

/// Update an existing scooter
///
/// Updates the data of an existing scooter based on the provided ID.
#[utoipa::path(
    put,
    path = "/trotis/{id}",
    request_body = Troti,
    responses(
        (status = 200, description = "Scooter updated successfully", body = ApiResponse),
        (status = 404, description = "Scooter not found", body = ErrorResponse)
    ),
    params(
        ("id" = i32, Path, description = "Scooter ID")
    ),
    tag = "scooters"
)]
async fn update_troti(id: i32, updated_troti: Troti, db: Db) -> Result<warp::reply::WithStatus<warp::reply::Json>, Rejection> {
    let client = db.lock().await;
    match client
        .execute(
            "UPDATE trotis SET mac_address = $1, serial_number = $2, battery_percentage = $3, latitude = $4, longitude = $5 WHERE id = $6",
            &[
                &updated_troti.mac_address,
                &updated_troti.serial_number,
                &updated_troti.battery_percentage,
                &updated_troti.latitude,
                &updated_troti.longitude,
                &id,
            ],
        )
        .await {
            Ok(rows_affected) => {
                if rows_affected == 0 {
                    return Ok(warp::reply::with_status(
                        warp::reply::json(&ErrorResponse { error: "Scooter not found".to_string() }),
                        StatusCode::NOT_FOUND,
                    ));
                }

                Ok(warp::reply::with_status(
                    warp::reply::json(&ApiResponse { message: "Scooter updated".to_string() }),
                    StatusCode::OK,
                ))
            },
            Err(e) => {
                eprintln!("Error updating scooter: {}", e);
                Ok(warp::reply::with_status(
                    warp::reply::json(&ErrorResponse { error: format!("Error updating scooter: {}", e) }),
                    StatusCode::INTERNAL_SERVER_ERROR,
                ))
            }
        }
}

/// Delete a scooter
///
/// Removes a scooter from the system based on the provided ID.
#[utoipa::path(
    delete,
    path = "/trotis/{id}",
    responses(
        (status = 200, description = "Scooter deleted successfully", body = ApiResponse),
        (status = 404, description = "Scooter not found", body = ErrorResponse)
    ),
    params(
        ("id" = i32, Path, description = "Scooter ID")
    ),
    tag = "scooters"
)]
async fn delete_troti(id: i32, db: Db) -> Result<warp::reply::WithStatus<warp::reply::Json>, Rejection> {
    let client = db.lock().await;
    match client.execute("DELETE FROM trotis WHERE id = $1", &[&id]).await {
        Ok(rows_affected) => {
            if rows_affected == 0 {
                return Ok(warp::reply::with_status(
                    warp::reply::json(&ErrorResponse { error: "Scooter not found".to_string() }),
                    StatusCode::NOT_FOUND,
                ));
            }

            Ok(warp::reply::with_status(
                warp::reply::json(&ApiResponse { message: "Scooter deleted".to_string() }),
                StatusCode::OK,
            ))
        },
        Err(e) => {
            eprintln!("Error deleting scooter: {}", e);
            Ok(warp::reply::with_status(
                warp::reply::json(&ErrorResponse { error: format!("Error deleting scooter: {}", e) }),
                StatusCode::INTERNAL_SERVER_ERROR,
            ))
        }
    }
}