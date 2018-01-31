#import GPIO library & time
import RPi.GPIO as GPIO
import time

#Pin numbers
led1 = 7
led2 = 11
led3 = 13

#set GPIO numbering mode and define input pin
GPIO.setmode(GPIO.BOARD)
#OUT
for ledX in [led1, led2, led3]:
    	GPIO.setup(ledX,GPIO.OUT)   # Set led's mode is output
    	GPIO.output(ledX, GPIO.LOW) # Set led to low(0V) for clean start

try:
    	while True:
    			for ledX in [led1, led2, led3]:
    					GPIO.output(ledX, GPIO.HIGH) # Set led to high(3V)
    					time.sleep(0.2)
    			for ledX in [led1, led2, led3]:
    					GPIO.output(ledX, GPIO.LOW) # Set led to high(3V)
    					time.sleep(0.2)

except KeyboardInterrupt:
        GPIO.cleanup()