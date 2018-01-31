#import GPIO library
import RPi.GPIO as GPIO
import time

#Pin numbers
led1 = 7
led2 = 11
led3 = 13

def setup():
        global p, q, r

        #set GPIO numbering mode
        GPIO.setmode(GPIO.BOARD)

        #OUT setup
        for ledX in [led1, led2, led3]:
                GPIO.setup(ledX,GPIO.OUT)   # Set led's mode is output
                GPIO.output(ledX, GPIO.LOW) # Set led to low(0V)
        p = GPIO.PWM(led1, 50)  # set Frequece (1000 = 1KHz)              
        q = GPIO.PWM(led2, 50)     
        r = GPIO.PWM(led3, 50)     
        for x in [p, q, r]:
                x.start(0) # Duty Cycle = 0

def loop():
        while True:
                for dc in range(0, 101, 20): # Increase duty cycle: 0~100
                        for x in [p, q, r]:
                                x.ChangeDutyCycle(dc)   # Change duty cycle
                                time.sleep(0.1)
                time.sleep(0.5)  
                for dc in range(100, -1, -10): # Decrease duty cycle: 100~0
                        for x in [p, q, r]:
                                x.ChangeDutyCycle(dc)   # Change duty cycle
                                time.sleep(0.1)
                time.sleep(0.5)

def destroy():
        for x in [p, q, r]:
                x.stop()
        for ledX in [led1, led2, led3]:
                GPIO.output(ledX, GPIO.LOW) # turn off all leds
        GPIO.cleanup()

if __name__ == '__main__': # Program start from here
        setup()
        try:
                loop()
        # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        except KeyboardInterrupt:
                destroy()
