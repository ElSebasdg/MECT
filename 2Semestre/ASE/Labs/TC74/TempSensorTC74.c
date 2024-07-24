#include "TempSensorTC74.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h" 
#include "driver/i2c_master.h"

esp_err_t tc74_init(i2c_master_bus_handle_t* pBusHandle,
                    i2c_master_dev_handle_t* pSensorHandle,
                    uint8_t sensorAddr, int sdaPin, int sclPin, uint32_t clkSpeedHz) {

    i2c_master_bus_config_t i2cMasterConfig = {
        .clk_source = I2C_CLK_SRC_DEFAULT,
        .i2c_port = I2C_NUM_0,
        .scl_io_num = sclPin,
        .sda_io_num = sdaPin,
        .glitch_ignore_cnt = 7,
        .flags.enable_internal_pullup = true,
    };

    ESP_ERROR_CHECK(i2c_new_master_bus(&i2cMasterConfig, pBusHandle));

    i2c_device_config_t i2cDevCfg = {
        .dev_addr_length = I2C_ADDR_BIT_LEN_7,
        .device_address = sensorAddr,
        .scl_speed_hz = clkSpeedHz,
    };

    ESP_ERROR_CHECK(i2c_master_bus_add_device(*pBusHandle, &i2cDevCfg, pSensorHandle));

    return ESP_OK;
}

// esp_err_t tc_74_free(i2c_master_bus_handle_t busHandle,
//                      i2c_master_dev_handle_t sensorHandle) {
//     // Free I2C device handle
//     // Return appropriate error code
// }

esp_err_t tc74_standy(i2c_master_dev_handle_t sensorHandle) {
    uint8_t buffer[2] = {0x01, 0x80};
    ESP_ERROR_CHECK(i2c_master_transmit(sensorHandle, buffer, sizeof(buffer), -1));

    return ESP_OK;
}

esp_err_t tc74_wakeup(i2c_master_dev_handle_t sensorHandle) {
    uint8_t buffer[2] = {0x01, 0x00};
    ESP_ERROR_CHECK(i2c_master_transmit(sensorHandle, buffer, sizeof(buffer), -1));

    return ESP_OK;
}

// bool tc74_is_temperature_ready(i2c_master_dev_handle_t sensorHandle) {
//     // Check if temperature data is ready to be read from the sensor
//     // Return true if ready, false otherwise
// }

// esp_err_t tc74_wakeup_and_read_temp(i2c_master_dev_handle_t sensorHandle, uint8_t* pTemp) {
//     // Wake up the sensor if in standby mode
//     // Read temperature data from the sensor
//     // Store temperature data in pTemp
//     // Return appropriate error code
// }

esp_err_t tc74_read_temp_after_cfg(i2c_master_dev_handle_t sensorHandle, uint8_t* pTemp) {
    uint8_t txBuf[1] = {0x00};
    ESP_ERROR_CHECK(i2c_master_transmit_receive(sensorHandle, txBuf, sizeof(txBuf),
                                                                pTemp, sizeof(uint8_t), -1));

    return ESP_OK;
 }

esp_err_t tc74_read_temp_after_temp(i2c_master_dev_handle_t sensorHandle, uint8_t* pTemp) {
    ESP_ERROR_CHECK(i2c_master_receive(sensorHandle, pTemp, sizeof(uint8_t), -1));

    return ESP_OK;
}
