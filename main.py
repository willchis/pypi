from lcd import lcd
from weather import weather
import json

if __name__ == '__main__':
    print ('Program is starting ... ')
    #try:
    weather = weather()
    weather.request_data()
    temperature = weather.tempF()
    print(temperature)
    print(json.dumps(weather.data))
    #except KeyboardInterrupt:

       # destroy()
    lcd = lcd()
    lcd.write()
