#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_system.h"
#include "driver/gpio.h"

// Define os pinos dos displays de 7 segmentos
#define SEG_A_PIN 2
#define SEG_B_PIN 3
#define SEG_C_PIN 4
#define SEG_D_PIN 5
#define SEG_E_PIN 6
#define SEG_F_PIN 7
#define SEG_G_PIN 8
#define SEG_DP_PIN 10

// Define os pinos dos displays
#define DISPLAY_1_PIN 0
#define DISPLAY_2_PIN 1

void app_main() {
    // Configura os pinos dos displays como saída
    gpio_config_t io_config;
    io_config.intr_type = GPIO_INTR_DISABLE;
    io_config.mode = GPIO_MODE_OUTPUT;
    io_config.pin_bit_mask = ((1ULL << SEG_A_PIN) | (1ULL << SEG_B_PIN) | (1ULL << SEG_C_PIN) | (1ULL << SEG_D_PIN) |
                              (1ULL << SEG_E_PIN) | (1ULL << SEG_F_PIN) | (1ULL << SEG_G_PIN) | (1ULL << SEG_DP_PIN) |
                              (1ULL << DISPLAY_1_PIN) | (1ULL << DISPLAY_2_PIN));
    io_config.pull_down_en = GPIO_PULLDOWN_DISABLE;
    io_config.pull_up_en = GPIO_PULLUP_DISABLE;
    gpio_config(&io_config);

    // Acende os dois displays
    gpio_set_level(DISPLAY_1_PIN, 1);
    gpio_set_level(DISPLAY_2_PIN, 1);

    // Acende todos os segmentos dos dois displays
    gpio_set_level(SEG_A_PIN, 1);
    gpio_set_level(SEG_B_PIN, 1);
    gpio_set_level(SEG_C_PIN, 1);
    gpio_set_level(SEG_D_PIN, 1);
    gpio_set_level(SEG_E_PIN, 1);
    gpio_set_level(SEG_F_PIN, 1);
    gpio_set_level(SEG_G_PIN, 1);
    gpio_set_level(SEG_DP_PIN, 1);

    while(1) {
        // Mantém os displays acesos constantemente
        vTaskDelay(pdMS_TO_TICKS(1000)); // Aguarda 1 segundo antes de repetir o loop
    }
}