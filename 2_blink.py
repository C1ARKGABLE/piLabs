# import GPIO library & time
import RPi.GPIO as GPIO
import time

# Pin numbers
led0 = 7
led1 = 11
led2 = 13


# Create a list of leds
leds = [led0, led1, led2]

# Set GPIO numbering mode and define input pin
GPIO.setmode(GPIO.BOARD)


# For each LED in our list of LEDs
for ledX in leds:
  # Set LEDs mode to output
    GPIO.setup(ledX, GPIO.OUT)
  # Set led to low(0V) for clean start
    GPIO.output(ledX, GPIO.LOW)

try:
    # Loop forever
    while True:
        for ledX in leds:
            # Set led to high(3V)
            GPIO.output(ledX, GPIO.HIGH)
            time.sleep(0.2)
        for ledX in leds:
            # Set led to low(0V)
            GPIO.output(ledX, GPIO.LOW)
            time.sleep(0.2)
# Exit on ctrl+c
except KeyboardInterrupt:
    GPIO.cleanup()
