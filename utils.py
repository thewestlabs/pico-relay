import re
from machine import Pin, ADC, Timer, UART
from Device import UART_BLE_PORT, UART_BLE_RX, UART_BLE_TX, ADC_VOLTAGE_SENSOR_PIN, VOLTAGE_MULTIPLIER, GPIO_RELAY_PIN,  I2C_RTC_PORT, I2C_RTC_SCL, I2C_RTC_SDA
from lib.ds3231 import ds3231

adc = ADC(ADC_VOLTAGE_SENSOR_PIN)
uart = UART(UART_BLE_PORT, 9600, rx=Pin(UART_BLE_RX), tx=Pin(UART_BLE_TX))
conversion_factor = (3.3/65536) * VOLTAGE_MULTIPLIER
relay = Pin(GPIO_RELAY_PIN, Pin.OUT)
rtc = ds3231(I2C_RTC_PORT, I2C_RTC_SCL, I2C_RTC_SDA)
rtc_i2c_addr = [hex(ii) for ii in rtc.bus.scan()] 
date_regex = re.compile(" |:|/")

def read_voltage() -> float:
    voltage = adc.read_u16() * conversion_factor
    return float("{:.2f}".format(voltage))

def execute_timer(callback, delay):
    Timer().init(mode=Timer.ONE_SHOT, period=int(delay * 1000), callback=lambda t: callback())

def read_bluetooth():
    if uart.any():
        command: bytearray = uart.readline()
        if command != b'\x00':
            print(f"bluetooth read: {command} {command.decode()}")
            return command.decode()

def write_bluetooth(data):
    uart.write(str(data) + "\n")

def connect_relay():
    relay.value(0)

def disconnect_relay():
    relay.value(1)

def read_time():
    if rtc_i2c_addr != []:
        date_time = rtc.read_time()
        items = date_regex.split(date_time)
        return [int(items[0]), int(items[1]), int(items[2]), int(items[3]), int(items[4]), int(items[5])]
    else:
        return None

def set_time(time):
    if (self.i2c_addr != []):
        self.rtc.set_time(time)  # '03:52:30,Thursday,2022-07-28'
