#ifndef __TEMP_SENSOR_TC74_H__INCLUDED__
#define __TEMP_SENSOR_TC74_H__INCLUDED__

#include "esp_err.h"
#include "driver/i2c.h"

esp_err_t tc74_init(i2c_master_bus_handle_t* pBusHandle,
					i2c_master_dev_handle_t* pSensorHandle,
					uint8_t sensorAddr, int sdaPin, int sclPin, uint32_t clkSpeedHz);

esp_err_t tc_74_free(i2c_master_bus_handle_t busHandle,
					 i2c_master_dev_handle_t sensorHandle);

esp_err_t tc74_standy(i2c_master_dev_handle_t sensorHandle);

esp_err_t tc74_wakeup(i2c_master_dev_handle_t sensorHandle);

bool tc74_is_temperature_ready(i2c_master_dev_handle_t sensorHandle);

esp_err_t tc74_wakeup_and_read_temp(i2c_master_dev_handle_t sensorHandle, uint8_t* pTemp);

esp_err_t tc74_read_temp_after_cfg(i2c_master_dev_handle_t sensorHandle, uint8_t* pTemp);

esp_err_t tc74_read_temp_after_temp(i2c_master_dev_handle_t sensorHandle, uint8_t* pTemp);

#endif // __TEMP_SENSOR_TC74_H__INCLUDED__
