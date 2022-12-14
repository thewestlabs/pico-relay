# Contains hardware build config info

# Device Info
DEVICE_ID = "relay_1"
DEVICE_VERSION = "2.2"

# Relay Pin
GPIO_RELAY_PIN = 2

# Voltage Sensor
ADC_VOLTAGE_SENSOR_PIN = 26
VOLTAGE_MULTIPLIER = 10

# DS3231 I2C Chip 
I2C_RTC_PORT = 1
I2C_RTC_SDA = 10
I2C_RTC_SCL = 11

# SD1306 0.91" I2C OLED Display
I2C_DISPLAY_PORT = 0
I2C_DISPLAY_SDA = 4
I2C_DISPLAY_SCL = 5
SSD1306_DISPLAY_RES_X = 128
SSD1306_DISPLAY_RES_Y = 32

# HM-10 BLE UART Module
UART_BLE_PORT = 0
UART_BLE_TX = 12
UART_BLE_RX = 13
