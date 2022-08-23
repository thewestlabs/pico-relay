import time
from utils import read_voltage, disconnect_relay

while True:
    time.sleep(2)
    voltage = read_voltage()
    print(f"voltage: {voltage}v")
    if (voltage > 14.4):
        print("voltage above")
        disconnect_relay()
