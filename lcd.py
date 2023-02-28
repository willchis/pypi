from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime

PCF8574_address = 0x27
PCF8574A_address = 0x3F

class lcd():
    def __init__(self):
        try:
            self.mcp = PCF8574_GPIO(PCF8574_address)
        except:
            try:
                self.mcp = PCF8574_GPIO(PCF8574A_address)
            except:
                print('I2C Address Error !')
                exit(1)

        self.lcd_hardware = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=self.mcp)
        self.mcp.output(3,1) # turn on LCD backlight
        self.lcd_hardware.begin(16,2) # set number of LCD lines and columns

    def get_cpu_temp():
        # get CPU temperature and store it into file
        "/sys/class/thermal/thermal_zone0/temp"
        tmp = open('/sys/class/thermal/thermal_zone0/temp')
        cpu = tmp.read()
        tmp.close()
        return '{:.2f}'.format( float(cpu)/1000 ) + ' C'

    def get_time_now():
        # get system time
        return datetime.now().strftime('%H:%M:%S')

    def write(self, line_one, line_two):
            #lcd.clear()
            self.lcd_hardware.setCursor(0,0)
            self.lcd_hardware.message(str(line_one) + '\n')
            self.lcd_hardware.message(str(line_two))

    def destroy(self):
        self.lcd_hardware.clear()
   