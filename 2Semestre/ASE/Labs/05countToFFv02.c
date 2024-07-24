#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
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

// Define os pinos dos displays de cátodo comum
#define PIN_DISPLAY_LSB 0
#define PIN_DISPLAY_MSB 1

// Define a frequência de incremento do contador (1 Hz)
#define INCREMENT_FREQUENCY_MS 100

// Define a frequência de refrescamento dos displays (100 Hz)
#define REFRESH_FREQUENCY_MS 10

// Tabela de conversão de número hexadecimal para display de 7 segmentos
const uint8_t sevenSegmentLookupTable[] = {
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

// Função para configurar os pinos GPIO
void gpio_setup() {
    gpio_config_t io_config;
    io_config.intr_type = GPIO_INTR_DISABLE;
    io_config.mode = GPIO_MODE_OUTPUT;
    io_config.pull_down_en = GPIO_PULLDOWN_DISABLE;
    io_config.pull_up_en = GPIO_PULLUP_DISABLE;

    // Configura os pinos dos displays de 7 segmentos
    io_config.pin_bit_mask = (1ULL << SEG_A_PIN) |
                             (1ULL << SEG_B_PIN) |
                             (1ULL << SEG_C_PIN) |
                             (1ULL << SEG_D_PIN) |
                             (1ULL << SEG_E_PIN) |
                             (1ULL << SEG_F_PIN) |
                             (1ULL << SEG_G_PIN) |
                             (1ULL << SEG_DP_PIN);
    gpio_config(&io_config);

    // Configura os pinos dos displays de cátodo comum
    io_config.pin_bit_mask = (1ULL << PIN_DISPLAY_LSB) |
                             (1ULL << PIN_DISPLAY_MSB);
    gpio_config(&io_config);
}

// Função para exibir um dígito nos displays de 7 segmentos
void display_digit(uint8_t digit) {
    uint8_t segments = sevenSegmentLookupTable[digit];
    gpio_set_level(SEG_A_PIN, (segments >> 0) & 1);
    gpio_set_level(SEG_B_PIN, (segments >> 1) & 1);
    gpio_set_level(SEG_C_PIN, (segments >> 2) & 1);
    gpio_set_level(SEG_D_PIN, (segments >> 3) & 1);
    gpio_set_level(SEG_E_PIN, (segments >> 4) & 1);
    gpio_set_level(SEG_F_PIN, (segments >> 5) & 1);
    gpio_set_level(SEG_G_PIN, (segments >> 6) & 1);
}

// Função para atualizar os displays com o valor do contador em hexadeci
void update_display(uint8_t count) {
    static int display_number = 0;

    if(display_number == 0) {
        gpio_set_level(PIN_DISPLAY_LSB, 1);
        gpio_set_level(PIN_DISPLAY_MSB, 0);
        display_digit(count & 0xF);
    } else {
        gpio_set_level(PIN_DISPLAY_LSB, 0);
        gpio_set_level(PIN_DISPLAY_MSB, 1);
        display_digit(count >> 4);
    }
    display_number = !display_number;
}

// Função principal
void app_main() {
    gpio_setup();
    uint8_t loops = 0;
    uint8_t count = 0;
    while (1) {
        update_display(count);
        if(loops == INCREMENT_FREQUENCY_MS) {
        	count = (count + 1) & 0xFF; // Incrementa o contador e limita ao intervalo de 0 a 255
        	printf("%x\n", count);
        	loops = 0;
		}
		loops++;
        vTaskDelay(pdMS_TO_TICKS(REFRESH_FREQUENCY_MS));
    }
}