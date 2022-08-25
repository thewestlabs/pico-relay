import time
from utils import read_voltage, disconnect_relay, connect_relay, read_time

while True:
    time.sleep(2)
    voltage = read_voltage()
    year, month, date, hour, minute, second = read_time()

    time = "{}:{}{}".format(hour % 12, "{:02d}".format(minute), 'am' if hour < 12 else 'pm')
    print(f"time: {time} voltage: {voltage}v")
    
    if (hour > 17 or hour < 5):
        connect_relay()
        print("grid lockin")
    elif (voltage > 14.4):
        disconnect_relay()
        print("voltage high")
    eliif (voltage < 12.1):
        connect_relay()
        print("voltage low")
