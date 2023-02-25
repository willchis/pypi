import RPi.GPIO as GPIO
import time
ledPin = 11

def setup():
    GPIO.setmode(GPIO.BOARD) # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT) # set the ledPin to OUTPUT mode
    GPIO.output(ledPin, GPIO.LOW) # make ledPin output LOW level
    print ('using pin%d'%ledPin)
def loop():
    while True:
        GPIO.output(ledPin, GPIO.HIGH)
        print('led turned on >>>')
        time.sleep(1)
        GPIO.output(ledPin, GPIO.LOW)
        print ('led turned off <<<')
        time.sleep(1)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    print('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        # Press ctrl-c to end the program.
        destroy()