# import GPIO library & time
import RPi.GPIO as GPIO
import time

# Pin numbers
led0 = 7
led1 = 11
led2 = 13
button0 = 16

# Create a list of leds
leds = [led0, led1, led2]

# Set GPIO numbering mode and define input pin
GPIO.setmode(GPIO.BOARD)

# Setup input
GPIO.setup(button0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# For each LED in our list of LEDs
for ledX in leds:
    # Set LEDs mode to output
    GPIO.setup(ledX, GPIO.OUT)
    # Set led to low(0V) for clean start
    GPIO.output(ledX, GPIO.LOW)

try:
    while True:
        for ledX in leds:
            # blink only when button0 is pressed
            GPIO.output(ledX, GPIO.input(button0))

# Exit on ctrl+c
except KeyboardInterrupt:
    GPIO.cleanup()
