import datetime
import json
from lcd import lcd
from time import sleep
from weather import weather

def get_time_now():    
    return datetime.now().strftime('%H:%M:%S')

if __name__ == '__main__':
    print ('Program is starting ... ')
    weather = weather()
    weather.request_data()
    temperature = "Current: " + str(round(weather.tempF())) + "F"
    print(temperature)
    print(json.dumps(weather.data))

    lcd = lcd()
    try:
        while True:
            lcd.write(temperature, "current temp", get_time_now())
            sleep(1)
    except KeyboardInterrupt:
        lcd.destroy()
