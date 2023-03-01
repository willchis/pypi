from datetime import datetime
import json
from lcd import lcd
from time import sleep
from weather import weather
from zoneinfo import ZoneInfo

PST = ZoneInfo("America/Los_Angeles")
UK = ZoneInfo("Europe/Belfast")
INDIA = ZoneInfo("Asia/Kolkata")

def get_time_now(tz=None):
    now = datetime.now()
    
    if (tz is not None):
        now = now.astimezone(tz)
    return now.strftime('%H:%M:%S')

if __name__ == '__main__':
    print ('Program is starting ... ')
    weather = weather()
    weather.request_data()
    temperature = str(round(weather.tempF())) + "F"
    print(temperature)
    print(json.dumps(weather.data))

    lcd = lcd()
    try:
        i = 0
        duration = 3
        times = {
            "Local": None,
            "UK": UK,
            "Pacific": PST,
            "India": INDIA
        }
        times_index = list(times)
        while True:
            time_output = get_time_now(times[times_index[i]]) + " " + times_index[i]
            lcd.write(temperature, time_output)
            print(time_output)
            sleep(1)
            i += 1
            if (i >= len(times_index)):
                i = 0
    except KeyboardInterrupt:
        lcd.destroy()
