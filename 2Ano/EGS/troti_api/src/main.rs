use postgres::{Client, NoTls};
use postgres::Error as PostgresError;
use std::net::{TcpListener, TcpStream};
use std::io::{Read, Write};
use std::env;

#[macro_use]
extern crate serde_derive;
extern crate serde_json;

// Modelo para Trotinete
#[derive(Serialize, Deserialize)]
struct Troti {
    id: Option<i32>,
    mac_address: String,
    serial_number: String,
    battery_percentage: i16, // Alterado de u8 para i16
    latitude: f64,
    longitude: f64,
}

// URL da base de dados
const DB_URL: &str = env!("DATABASE_URL");

// Respostas HTTP
const OK_RESPONSE: &str = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n";
const NOT_FOUND: &str = "HTTP/1.1 404 NOT FOUND\r\n\r\n";
const INTERNAL_SERVER_ERROR: &str = "HTTP/1.1 500 INTERNAL SERVER ERROR\r\n\r\n";

// Função principal
fn main() {
    if let Err(e) = set_database() {
        println!("Erro: {}", e);
        return;
    }

    let listener = TcpListener::bind("0.0.0.0:8080").unwrap();
    println!("Servidor iniciado na porta 8080");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                handle_client(stream);
            }
            Err(e) => {
                println!("Erro: {}", e);
            }
        }
    }
}

// Lidar com clientes
fn handle_client(mut stream: TcpStream) {
    let mut buffer = [0; 1024];
    let mut request = String::new();

    if let Ok(size) = stream.read(&mut buffer) {
        request.push_str(String::from_utf8_lossy(&buffer[..size]).as_ref());

        let (status_line, content) = match &*request {
            r if r.starts_with("POST /trotis") => handle_post_request(r),
            r if r.starts_with("GET /trotis/") => handle_get_request(r),
            r if r.starts_with("GET /trotis") => handle_get_all_request(r),
            r if r.starts_with("PUT /trotis/") => handle_put_request(r),
            r if r.starts_with("DELETE /trotis/") => handle_delete_request(r),
            _ => (NOT_FOUND.to_string(), "404 Not Found".to_string()),
        };

        stream.write_all(format!("{}{}", status_line, content).as_bytes()).unwrap();
    }
}

// Criar nova trotinete
fn handle_post_request(request: &str) -> (String, String) {
    match (get_troti_request_body(&request), Client::connect(DB_URL, NoTls)) {
        (Ok(troti), Ok(mut client)) => {
            client.execute(
                "INSERT INTO trotis (mac_address, serial_number, battery_percentage, latitude, longitude) VALUES ($1, $2, $3, $4, $5)",
                &[&troti.mac_address, &troti.serial_number, &troti.battery_percentage, &troti.latitude, &troti.longitude]
            ).unwrap();

            (OK_RESPONSE.to_string(), "Troti criada".to_string())
        }
        _ => (INTERNAL_SERVER_ERROR.to_string(), "Erro".to_string()),
    }
}

// Obter uma trotinete por ID
fn handle_get_request(request: &str) -> (String, String) {
    match (get_id(&request).parse::<i32>(), Client::connect(DB_URL, NoTls)) {
        (Ok(id), Ok(mut client)) =>
            match client.query_one("SELECT * FROM trotis WHERE id = $1", &[&id]) {
                Ok(row) => {
                    let troti = Troti {
                        id: row.get(0),
                        mac_address: row.get(1),
                        serial_number: row.get(2),
                        battery_percentage: row.get(3),
                        latitude: row.get(4),
                        longitude: row.get(5),
                    };

                    (OK_RESPONSE.to_string(), serde_json::to_string(&troti).unwrap())
                }
                _ => (NOT_FOUND.to_string(), "Troti não encontrada".to_string()),
            }

        _ => (INTERNAL_SERVER_ERROR.to_string(), "Erro".to_string()),
    }
}

// Obter todas as trotinetes
fn handle_get_all_request(_request: &str) -> (String, String) {
    match Client::connect(DB_URL, NoTls) {
        Ok(mut client) => {
            let mut trotis = Vec::new();

            for row in client.query("SELECT * FROM trotis", &[]).unwrap() {
                trotis.push(Troti {
                    id: row.get(0),
                    mac_address: row.get(1),
                    serial_number: row.get(2),
                    battery_percentage: row.get(3),
                    latitude: row.get(4),
                    longitude: row.get(5),
                });
            }

            (OK_RESPONSE.to_string(), serde_json::to_string(&trotis).unwrap())
        }
        _ => (INTERNAL_SERVER_ERROR.to_string(), "Erro".to_string()),
    }
}

// Atualizar uma trotinete
fn handle_put_request(request: &str) -> (String, String) {
    match (
        get_id(&request).parse::<i32>(),
        get_troti_request_body(&request),
        Client::connect(DB_URL, NoTls),
    ) {
        (Ok(id), Ok(troti), Ok(mut client)) => {
            client.execute(
                "UPDATE trotis SET mac_address = $1, serial_number = $2, battery_percentage = $3, latitude = $4, longitude = $5 WHERE id = $6",
                &[&troti.mac_address, &troti.serial_number, &troti.battery_percentage, &troti.latitude, &troti.longitude, &id]
            ).unwrap();

            (OK_RESPONSE.to_string(), "Troti atualizada".to_string())
        }
        _ => (INTERNAL_SERVER_ERROR.to_string(), "Erro".to_string()),
    }
}

// Excluir uma trotinete
fn handle_delete_request(request: &str) -> (String, String) {
    match (get_id(&request).parse::<i32>(), Client::connect(DB_URL, NoTls)) {
        (Ok(id), Ok(mut client)) => {
            let rows_affected = client.execute("DELETE FROM trotis WHERE id = $1", &[&id]).unwrap();

            if rows_affected == 0 {
                return (NOT_FOUND.to_string(), "Troti não encontrada".to_string());
            }

            (OK_RESPONSE.to_string(), "Troti eliminada".to_string())
        }
        _ => (INTERNAL_SERVER_ERROR.to_string(), "Erro".to_string()),
    }
}

// Configurar base de dados
fn set_database() -> Result<(), PostgresError> {
    let mut client = Client::connect(DB_URL, NoTls)?;

    client.batch_execute(
        "CREATE TABLE IF NOT EXISTS trotis (
            id SERIAL PRIMARY KEY,
            mac_address VARCHAR NOT NULL,
            serial_number VARCHAR NOT NULL,
            battery_percentage SMALLINT NOT NULL,
            latitude DOUBLE PRECISION NOT NULL,
            longitude DOUBLE PRECISION NOT NULL
        )"
    )?;
    Ok(())
}

// Extrair ID da URL
fn get_id(request: &str) -> &str {
    request.split("/").nth(2).unwrap_or_default().split_whitespace().next().unwrap_or_default()
}

// Converter corpo da requisição em uma estrutura Troti
fn get_troti_request_body(request: &str) -> Result<Troti, serde_json::Error> {
    serde_json::from_str(request.split("\r\n\r\n").last().unwrap_or_default())
}
