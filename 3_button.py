#import GPIO library & time
import RPi.GPIO as GPIO
import time

#Pin numbers
led1 = 7
led2 = 11
led3 = 13
button1 = 16

#set GPIO numbering mode and define input pin
GPIO.setmode(GPIO.BOARD)
#IN
GPIO.setup(button1,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#OUT
for ledX in [led1, led2, led3]:
        GPIO.setup(ledX,GPIO.OUT)   # Set led's mode is output
        GPIO.output(ledX, GPIO.LOW) # Set led to low(0V) for clean start

try:
        while True:
                for ledX in [led1, led2, led3]:
                        GPIO.output(ledX, GPIO.input(button1)) #blink when button1
        

except KeyboardInterrupt:
        GPIO.cleanup()