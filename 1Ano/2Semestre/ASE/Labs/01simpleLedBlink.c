#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_system.h"
#include "esp_log.h"
#include "driver/gpio.h"

#define LED_GPIO 2 // GPIO pin 2

void app_main()
{
    // Configure GPIO pin
    gpio_config_t io_config;
    io_config.intr_type = GPIO_INTR_DISABLE;
    io_config.mode = GPIO_MODE_OUTPUT;
    io_config.pin_bit_mask = (1ULL << LED_GPIO);
    io_config.pull_down_en = GPIO_PULLDOWN_DISABLE;
    io_config.pull_up_en = GPIO_PULLUP_DISABLE;
    gpio_config(&io_config);

    while (1)
    {
        // Turn on LED
        gpio_set_level(LED_GPIO, 1);
        vTaskDelay(100 / portTICK_PERIOD_MS);
        printf("ONN");
        // Turn off LED
        gpio_set_level(LED_GPIO, 0);
        vTaskDelay(100 / portTICK_PERIOD_MS);
    }
}