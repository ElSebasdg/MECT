#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/i2c_master.h"
#include "esp_log.h"
#include "TempSensorTC74.c"
#include "driver/ledc.h"

// Este programa inicializa um sensor de temperatura TC74 usando comunicação I2C, lê a 
// temperatura continuamente e imprime os valores lidos a cada 10 milissegundos.


#define MIN_TEMP 20    // Minimum temperature value
#define MAX_TEMP 35  // Maximum temperature value
#define MIN_DUTY 0   // Minimum duty cycle for LEDC
#define MAX_DUTY 8191 // Maximum duty cycle for LEDC (13-bit)

uint32_t map(uint32_t value, uint32_t fromLow, uint32_t fromHigh, uint32_t toLow, uint32_t toHigh);


uint8_t sensorAddr = 0x49;
int sdaPin = 1;  // channel 2
int sclPin = 0;  // channel 1
uint32_t clkSpeedHz = 50000;


void app_main(void) {
	i2c_master_bus_handle_t i2cBusHandle;
	i2c_master_dev_handle_t i2cDevHandle;
	tc74_init(&i2cBusHandle, &i2cDevHandle, sensorAddr, sdaPin, sclPin, clkSpeedHz);

	tc74_wakeup(i2cDevHandle);
	uint8_t rxBuf[1];
	tc74_read_temp_after_cfg(i2cDevHandle, rxBuf);
	//tc74_read_temp_after_cfg(i2cDevHandle, rxBuf);
	while(1) {
		tc74_read_temp_after_temp(i2cDevHandle, rxBuf);

		printf("\nTemperature: %d", rxBuf[0]);

		// Delay between readings
		vTaskDelay(10 / portTICK_PERIOD_MS);
	}
}


// Function to map a value from one range to another
uint32_t map(uint32_t value, uint32_t fromLow, uint32_t fromHigh, uint32_t toLow, uint32_t toHigh) {
    return (value - fromLow) * (toHigh - toLow) / (fromHigh - fromLow) + toLow;
}
