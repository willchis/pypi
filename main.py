from datetime import datetime
import json
#from lcd import lcd
import sched, time
from weather import weather
from zoneinfo import ZoneInfo

PST = ZoneInfo("America/Los_Angeles")
UK = ZoneInfo("Europe/Belfast")
INDIA = ZoneInfo("Asia/Kolkata")

weather = weather()

def update_weather_data(): 
    weather.request_data()
    print(json.dumps(weather.data))

def get_time_now(tz=None):
    now = datetime.now()
    
    if (tz is not None):
        now = now.astimezone(tz)
    return now.strftime('%H:%M:%S')

if __name__ == '__main__':
    print ('Program is starting ... ')
    update_weather_data()

    #lcd = lcd()
    try:
        i = 0
        duration = 3
        chosen_time = 0
        times = {
            "Local": None,
            "UK": UK,
            "Pacific": PST,
            "India": INDIA
        }
        times_index = list(times)
        while True:
            time_output = get_time_now(times[times_index[chosen_time]]) + " " + times_index[chosen_time]
            temperature = str(round(weather.tempF())) + "°F"
            humidity = str(weather.humidity()) + "%"

            #lcd.write(temperature + " " + humidity, time_output)
            print(time_output)
            time.sleep(1)
            i += 1
            if (i % 60 == 0):
                update_weather_data()
            if (i % duration == 0):
                chosen_time += 1
            if (chosen_time >= len(times_index)):
                chosen_time = 0
    except KeyboardInterrupt:
        lcd.destroy()
