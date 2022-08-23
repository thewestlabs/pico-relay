import time
from utils import read_voltage, disconnect_relay

while True:
    time.sleep(2)
    voltage = read_voltage()
    print(f"voltage: {voltage}v")
    if (voltage > 14.4):
        print("voltage high")
        disconnect_relay()
    if (voltage > 12.1):
        print("voltage low")
        connect_relay()
