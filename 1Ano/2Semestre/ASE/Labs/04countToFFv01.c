#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_system.h"
#include "driver/gpio.h"

// Define os pinos dos displays de 7 segmentos
#define SEG_A_PIN 5
#define SEG_B_PIN 10
#define SEG_C_PIN 4
#define SEG_D_PIN 8
#define SEG_E_PIN 7
#define SEG_F_PIN 2
#define SEG_G_PIN 3
#define SEG_DP_PIN 6

// Define os pinos dos displays
#define DISPLAY_1_PIN 1
#define DISPLAY_2_PIN 0

// Define a frequência de incremento do contador (1 Hz)
#define COUNTER_FREQ_HZ 1

// Tabela de conversão de número hexadecimal para segmentos de display de 7 segmentos
const uint8_t hex_to_segments[] = {
    0b00111111, // 0
    0b00000110, // 1
    0b01011011, // 2
    0b01001111, // 3
    0b01100110, // 4
    0b01101101, // 5
    0b01111101, // 6
    0b00000111, // 7
    0b01111111, // 8
    0b01101111, // 9
    0b01110111, // A
    0b01111100, // B
    0b00111001, // C
    0b01011110, // D
    0b01111001, // E
    0b01110001  // F
};

// Variáveis globais
volatile uint8_t counter = 0;

// Função para atualizar os displays
void update_display(uint8_t value) {
    // Atualiza o display 1
    gpio_set_level(SEG_A_PIN, (hex_to_segments[value >> 4] & (1 << 0)) >> 0);
    gpio_set_level(SEG_B_PIN, (hex_to_segments[value >> 4] & (1 << 1)) >> 1);
    gpio_set_level(SEG_C_PIN, (hex_to_segments[value >> 4] & (1 << 2)) >> 2);
    gpio_set_level(SEG_D_PIN, (hex_to_segments[value >> 4] & (1 << 3)) >> 3);
    gpio_set_level(SEG_E_PIN, (hex_to_segments[value >> 4] & (1 << 4)) >> 4);
    gpio_set_level(SEG_F_PIN, (hex_to_segments[value >> 4] & (1 << 5)) >> 5);
    gpio_set_level(SEG_G_PIN, (hex_to_segments[value >> 4] & (1 << 6)) >> 6);
    gpio_set_level(SEG_DP_PIN, 0);
    gpio_set_level(DISPLAY_1_PIN, 1);
    gpio_set_level(DISPLAY_2_PIN, 0);
    vTaskDelay(pdMS_TO_TICKS(1)); // Tempo de espera para evitar o efeito fantasma

    // Atualiza o display 2
    gpio_set_level(SEG_A_PIN, (hex_to_segments[value & 0x0F] & (1 << 0)) >> 0);
    gpio_set_level(SEG_B_PIN, (hex_to_segments[value & 0x0F] & (1 << 1)) >> 1);
    gpio_set_level(SEG_C_PIN, (hex_to_segments[value & 0x0F] & (1 << 2)) >> 2);
    gpio_set_level(SEG_D_PIN, (hex_to_segments[value & 0x0F] & (1 << 3)) >> 3);
    gpio_set_level(SEG_E_PIN, (hex_to_segments[value & 0x0F] & (1 << 4)) >> 4);
    gpio_set_level(SEG_F_PIN, (hex_to_segments[value & 0x0F] & (1 << 5)) >> 5);
    gpio_set_level(SEG_G_PIN, (hex_to_segments[value & 0x0F] & (1 << 6)) >> 6);
    gpio_set_level(SEG_DP_PIN, 0);
    gpio_set_level(DISPLAY_1_PIN, 0);
    gpio_set_level(DISPLAY_2_PIN, 1);
}

// Função de incremento do contador
void increment_counter_task(void *pvParameters) {
    while (1) {
        counter++;
        if (counter > 255) {
            counter = 0;
        }
        update_display(counter);
        vTaskDelay(pdMS_TO_TICKS(1000 / COUNTER_FREQ_HZ)); // Aguarda 1 segundo antes de incrementar novamente
    }
}

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

    // Inicia a tarefa de incremento do contador
    xTaskCreate(increment_counter_task, "increment_counter_task", 2048, NULL, 5, NULL);
}