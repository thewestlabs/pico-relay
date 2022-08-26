import time
from utils import read_voltage, disconnect_relay, connect_relay, read_time, toggle_onboard_led

while True:
    time.sleep(2)
    toggle_onboard_led()
    voltage = read_voltage()
    year, month, date, hour, minute, second = read_time()

    formated_time = "{}:{}{}".format(hour % 12, "{:02d}".format(minute), 'am' if hour < 12 else 'pm')
    print(f"time: {formated_time} voltage: {voltage}v")
    
    if (hour > 17 or hour < 5):
        connect_relay()
        print("grid lockin")
    elif (voltage > 14.4):
        disconnect_relay()
        print("voltage high")
    elif (voltage < 12.1):
        connect_relay()
        print("voltage low")
