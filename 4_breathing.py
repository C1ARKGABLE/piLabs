#import GPIO library
#import RPi.GPIO as GPIO
import time

#Pin numbers
led0 = 7
led1 = 11
led2 = 13

# Create a list of leds
leds = [led0, led1, led2]
# Create a list to keep track of PWM objects
pwmObjs = []


def setup():

    #set GPIO numbering mode
    GPIO.setmode(GPIO.BOARD)

    #OUT setup
    for ledX in leds:

        # Set LEDs mode to output
        GPIO.setup(ledX,GPIO.OUT)

        # Set led to low(0V)
        GPIO.output(ledX, GPIO.LOW)

        # Set Frequency (1000 = 1KHz)
        x = GPIO.PWM(ledX, 50)

        # Duty Cycle = 0
        x.start(0)

        # Add x to pwmObjs
        pwmObjs.append(x)


def loop():
    while True:
        # Increase duty cycle: 0 -> 100
        for dutyCycle in range(0, 101, 20):
            for x in pwmObjs:
                x.ChangeDutyCycle(dutyCycle)
                time.sleep(0.1)
            time.sleep(0.5)

        # Decrease duty cycle: 100 -> 0
        for dutyCycle in range(100, -1, -10):
            for x in pwmObjs:
                x.ChangeDutyCycle(dutyCycle)
                time.sleep(0.1)
            time.sleep(0.5)

def destroy():
    for x in pwmObjs:
        # Stop all the PWM objects
        x.stop()

    for ledX in leds:
        # Turn off all leds
        GPIO.output(ledX, GPIO.LOW)

    GPIO.cleanup()

# Program start from here

if __name__ == '__main__':
        setup()
        try:
                loop()
        # When ctrl+c is pressed, destroy() is called to cleanup
        except KeyboardInterrupt:
                destroy()
