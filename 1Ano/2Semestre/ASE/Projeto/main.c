#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/i2c_master.h"
#include "esp_log.h"
#include "TempSensorTC74.c"
#include "driver/ledc.h"

#include "esp_wifi.h"
#include "nvs_flash.h"
#include "esp_event.h"
#include "esp_system.h"
#include "esp_http_server.h"
#include "driver/i2c.h"

static const char *TAG = "wifi_station";

// GPIO configurations for LEDs
#define GREEN_LED_GPIO 1
#define RED_LED_GPIO 0

i2c_master_bus_handle_t busHandle;
i2c_master_dev_handle_t sensorHandle;
uint8_t sensorAddr = 0x49;
int SDA_PIN = 2;  // channel 2s
int SCL_PIN= 3;  // channel 1
uint32_t CLOCK_SPEED_HZ = 50000;

// Global variable to hold temperature data
uint8_t temperature = 0;

// HTTP GET Handler for the root URL
esp_err_t root_get_handler(httpd_req_t *req) {
    // Read temperature
    esp_err_t ret = tc74_read_temp_after_temp(sensorHandle, &temperature);
    if (ret != ESP_OK) {
        ESP_LOGE(TAG, "Failed to read temperature");
        // Send error response
        httpd_resp_send_err(req, HTTPD_500_INTERNAL_SERVER_ERROR, "Failed to read temperature");
        return ESP_FAIL;
    }

    // HTML content for temperature monitoring interface
    const char *html_content = "<!DOCTYPE html>"
                               "<html lang='en'>"
                               "<head>"
                               "<meta charset='UTF-8'>"
                               "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
                               "<title>ESP32 Temperature Monitor</title>"
                               "<style>"
                               "body { font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0; }"
                               ".container { max-width: 800px; margin: 20px auto; background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }"
                               "h1 { font-size: 2.5em; color: #333; text-align: center; margin-bottom: 20px; }"
                               ".temperature { font-size: 2em; color: #666; text-align: center; margin-bottom: 30px; }"
                               "canvas { width: 100%; height: 300px; }"
                               "</style>"
                               "</head>"
                               "<body>"
                               "<div class='container'>"
                               "<h1>ESP32 Temperature Monitor</h1>"
                               "<div class='temperature' id='temperature-display'>Current Temperature: --°C</div>"
                               "<canvas id='temperature-chart'></canvas>"
                               "</div>"
                               "<script src='https://cdn.jsdelivr.net/npm/chart.js'></script>"
                               "<script>"
                               "let temperatureData = [];"
                               "let labels = [];"
                               "let chart;"
                               "function fetchTemperature() {"
                               "  fetch('/temperature').then(response => response.json()).then(data => {"
                               "    const currentTemp = data.temperature;"
                               "    document.getElementById('temperature-display').innerText = 'Current Temperature: ' + currentTemp + '°C';"
                               "    if (temperatureData.length >= 20) {"
                               "      temperatureData.shift();"
                               "      labels.shift();"
                               "    }"
                               "    const now = new Date();"
                               "    labels.push(now.getHours() + ':' + now.getMinutes() + ':' + now.getSeconds());"
                               "    temperatureData.push(currentTemp);"
                               "    chart.update();"
                               "  });"
                               "}"
                               "function initializeChart() {"
                               "  const ctx = document.getElementById('temperature-chart').getContext('2d');"
                               "  chart = new Chart(ctx, {"
                               "    type: 'line',"
                               "    data: {"
                               "      labels: labels,"
                               "      datasets: [{"
                               "        label: 'Temperature (°C)',"
                               "        data: temperatureData,"
                               "        backgroundColor: 'rgba(75, 192, 192, 0.2)',"
                               "        borderColor: 'rgba(75, 192, 192, 1)',"
                               "        borderWidth: 1,"
                               "        fill: true,"
                               "      }]"
                               "    },"
                               "    options: {"
                               "      responsive: true,"
                               "      scales: {"
                               "        x: {"
                               "          display: true,"
                               "          title: {"
                               "            display: true,"
                               "            text: 'Time'"
                               "          }"
                               "        },"
                               "        y: {"
                               "          display: true,"
                               "          title: {"
                               "            display: true,"
                               "            text: 'Temperature (°C)'"
                               "          }"
                               "        }"
                               "      }"
                               "    }"
                               "  });"
                               "}"
                               "window.onload = function() {"
                               "  initializeChart();"
                               "  setInterval(fetchTemperature, 1000);"
                               "};"
                               "</script>"
                               "</body>"
                               "</html>";

    // Send HTML response
    httpd_resp_send(req, html_content, strlen(html_content));
    return ESP_OK;
}

// HTTP GET Handler for the temperature URL
esp_err_t temperature_get_handler(httpd_req_t *req) {
    char resp_str[100];
    sprintf(resp_str, "{\"temperature\": %d}", temperature);
    httpd_resp_set_type(req, "application/json");
    httpd_resp_send(req, resp_str, strlen(resp_str));
    return ESP_OK;
}

// URI structure for the root URL
httpd_uri_t root_uri = {
    .uri       = "/",
    .method    = HTTP_GET,
    .handler   = root_get_handler,
    .user_ctx  = NULL
};

// URI structure for the temperature URL
httpd_uri_t temperature_uri = {
    .uri       = "/temperature",
    .method    = HTTP_GET,
    .handler   = temperature_get_handler,
    .user_ctx  = NULL
};

// Start the web server
httpd_handle_t start_webserver(void) {
    httpd_config_t config = HTTPD_DEFAULT_CONFIG();
    httpd_handle_t server = NULL;

    if (httpd_start(&server, &config) == ESP_OK) {
        httpd_register_uri_handler(server, &root_uri);
        httpd_register_uri_handler(server, &temperature_uri);
    }
    return server;
}

// Task to toggle the state of the red LED
void blink_red_led_task(void *pvParameter) {
    while (1) {
        // Toggle the red LED every 500ms
        gpio_set_level(RED_LED_GPIO, 1);
        vTaskDelay(100 / portTICK_PERIOD_MS);
        gpio_set_level(RED_LED_GPIO, 0);
        vTaskDelay(100 / portTICK_PERIOD_MS);
    }
}


static bool wifi_connected = false;

// Callback function for Wi-Fi events
void wifi_event_handler(void* arg, esp_event_base_t event_base, int32_t event_id, void* event_data) {
	static TaskHandle_t blinkRedLedTaskHandle = NULL;
    if (event_base == WIFI_EVENT && event_id == WIFI_EVENT_STA_START) {
        esp_wifi_connect();
    } else if (event_base == WIFI_EVENT && event_id == WIFI_EVENT_STA_DISCONNECTED) {
        ESP_LOGI(TAG, "Disconnected from Wi-Fi, retrying...");
        gpio_set_level(GREEN_LED_GPIO, 0);
        	if (blinkRedLedTaskHandle == NULL) {
        		xTaskCreate(&blink_red_led_task, "blink_red_led_task", configMINIMAL_STACK_SIZE, NULL, 5, &blinkRedLedTaskHandle);
        	}
        esp_wifi_connect();
    } else if (event_base == IP_EVENT && event_id == IP_EVENT_STA_GOT_IP) {
        ip_event_got_ip_t* event = (ip_event_got_ip_t*) event_data;
        ESP_LOGI(TAG, "Got IP: " IPSTR, IP2STR(&event->ip_info.ip));
        gpio_set_level(GREEN_LED_GPIO, 1);
        if (blinkRedLedTaskHandle != NULL) {
        	vTaskDelete(blinkRedLedTaskHandle);
            blinkRedLedTaskHandle = NULL;
        	}
        gpio_set_level(RED_LED_GPIO, 0);

        // Signal that Wi-Fi is connected
        wifi_connected = true;
    }
}

void wifi_init_sta() {
    esp_netif_init();
    esp_event_loop_create_default();
    esp_netif_create_default_wifi_sta();

    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
    esp_wifi_init(&cfg);

    esp_event_handler_instance_t instance_any_id;
    esp_event_handler_instance_t instance_got_ip;
    esp_event_handler_instance_register(WIFI_EVENT, ESP_EVENT_ANY_ID, &wifi_event_handler, NULL, &instance_any_id);
    esp_event_handler_instance_register(IP_EVENT, IP_EVENT_STA_GOT_IP, &wifi_event_handler, NULL, &instance_got_ip);

    wifi_config_t wifi_config = {
        .sta = {
            .ssid = "iPhone de Sebastian",
            .password = "sebastiao",
        },
    };

    esp_wifi_set_mode(WIFI_MODE_STA);
    esp_wifi_set_config(WIFI_IF_STA, &wifi_config);
    esp_wifi_start();

    ESP_LOGI(TAG, "wifi_init_sta finished.");
    ESP_LOGI(TAG, "Connecting to SSID:%s", wifi_config.sta.ssid);
}

void app_main(void) {
    esp_err_t ret = nvs_flash_init();
    if (ret == ESP_ERR_NVS_NO_FREE_PAGES || ret == ESP_ERR_NVS_NEW_VERSION_FOUND) {
        ESP_ERROR_CHECK(nvs_flash_erase());
        ret = nvs_flash_init();
    }
    ESP_ERROR_CHECK(ret);

    // Configure the GPIOs for the LED
    gpio_set_direction(GREEN_LED_GPIO, GPIO_MODE_OUTPUT);
    gpio_set_direction(RED_LED_GPIO, GPIO_MODE_OUTPUT);

    ESP_LOGI(TAG, "ESP_WIFI_MODE_STA");
    wifi_init_sta();

    // Start the event loop to handle Wi-Fi events
    esp_event_loop_create_default();

    // Wait for Wi-Fi connection
    while (!wifi_connected) {
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }

    // Start the web server
    start_webserver();

    // Initialize temperature sensor
    ret = tc74_init(&busHandle, &sensorHandle, sensorAddr, SDA_PIN, SCL_PIN, CLOCK_SPEED_HZ);
    if (ret != ESP_OK) {
        ESP_LOGE(TAG, "Failed to initialize temperature sensor");
        return;
    }

    while (1) {
        // Read temperature
        ret = tc74_read_temp_after_temp(sensorHandle, &temperature);
        if (ret != ESP_OK) {
            ESP_LOGE(TAG, "Failed to read temperature");
        }

        // Print temperature
        ESP_LOGI(TAG, "Temperature: %d", temperature);

        // Delay for some time before reading again
        vTaskDelay(1000 / portTICK_PERIOD_MS); // Adjust delay as needed
    }
}
