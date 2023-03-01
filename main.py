from datetime import datetime
import json
#from lcd import lcd
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
    temperature = "Current: " + str(round(weather.tempF())) + "F"
    print(temperature)
    print(json.dumps(weather.data))

    #lcd = lcd()
    try:
        i = 0
        duration = 3
        times = {
            "Local": None,
            "UK": UK,
            "PST": PST
        }
        times_index = list(times)
        while True:
            #lcd.write(temperature, get_time_now())
            print(get_time_now(times[times_index[i]]) + " " + times_index[i])
            sleep(1)
            i += 1
            if (i >= len(times_index)):
                i = 1
    except KeyboardInterrupt:
        lcd.destroy()
