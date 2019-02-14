#import GPIO library & time
import RPi.GPIO as GPIO
import time

#Pin numbers
led0 = 7
led1 = 11
led2 = 13
button0 = 16

# Create a list of leds
leds = [led0,led1,led2]

# Set GPIO numbering mode and define input pin
GPIO.setmode(GPIO.BOARD)

# Setup input
GPIO.setup(button0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#OUT
for ledX in leds:
    GPIO.setup(ledX,GPIO.OUT)   # Set led's mode is output
    GPIO.output(ledX, GPIO.LOW) # Set led to low(0V) for clean start

try:
    while True:
        for ledX in leds:
        GPIO.output(ledX, GPIO.input(button0)) # blink when button0


except KeyboardInterrupt:
    GPIO.cleanup()
