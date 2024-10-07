#include <stdio.h>
#include "esp_system.h"
#include "esp_spi_flash.h"
#include "driver/gpio.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#define BUTTON_GPIO 4
#define LED_GPIO 2

void app_main(void)
{
    // Initialize the GPIO configuration
    gpio_config_t io_conf;

    // Configure GPIO2 as output for LED
    io_conf.pin_bit_mask = (1ULL << LED_GPIO);
    io_conf.mode = GPIO_MODE_OUTPUT;
    gpio_config(&io_conf);

    // Configure GPIO4 as input for button
    io_conf.pin_bit_mask = (1ULL << BUTTON_GPIO);
    io_conf.mode = GPIO_MODE_INPUT;
    gpio_config(&io_conf);

    while (1)
    {
        // Read the state of the button
        int button_state = gpio_get_level(BUTTON_GPIO);

        gpio_set_level(LED_GPIO, button_state); // Turn on LED deppending on Button state
        //printf("Button Pressed\n");


        // If the button is pressed (GPIO4 reads high), turn on the LED
        /*if (button_state == 1)
        {
            printf("Button Pressed\n");
        }*/

        // A short delay to avoid continuous reading
        vTaskDelay(pdMS_TO_TICKS(100)); // Use pdMS_TO_TICKS to convert milliseconds to ticks
    }
}