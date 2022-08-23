from machine import Pin, ADC, Timer, UART
from Device import UART_BLE_PORT, UART_BLE_RX, UART_BLE_TX, ADC_VOLTAGE_SENSOR_PIN, VOLTAGE_MULTIPLIER, GPIO_RELAY_PIN

adc = ADC(ADC_VOLTAGE_SENSOR_PIN)
uart = UART(UART_BLE_PORT, 9600, rx=Pin(UART_BLE_RX), tx=Pin(UART_BLE_TX))
conversion_factor = (3.3/65536) * VOLTAGE_MULTIPLIER
relay = Pin(GPIO_RELAY_PIN, Pin.OUT)

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
