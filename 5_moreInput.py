import RPi.GPIO as GPIO
import time


# LED pins
led0 = 7
led1 = 11


leds = [led0, led1]

# PIR sensor input
pir0 = 13


def setup():

    # set GPIO numbering mode
    GPIO.setmode(GPIO.BOARD)

    # For each LED in our list of LEDs
    for ledX in leds:

        GPIO.setup(ledX, GPIO.OUT)

    # led0 is clear led, will be on when no motion is detected.
    GPIO.output(led0, GPIO.HIGH)

    # led1 is motion led, will be on when motion is detected.
    GPIO.output(led1, GPIO.LOW)

    # setup the input
    GPIO.setup(pir0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def loop():
    # Loop forever
    while True:
        # Set on to false
        on = False

        # Wait for PIR to change state
        # (Detecting motion or not detecting motion)
        GPIO.wait_for_edge(pir0, GPIO.BOTH)

        # if edge, and motion has been detected before, then edge is falling,
        # (aka no more motion)
        if on:
            # Turn off motion light, turn on clear
            GPIO.output(led0, GPIO.HIGH)
            GPIO.output(led1, GPIO.LOW)
            # set on to False
            on = False
        # if edge, and no motion has been detected before, then edge is rising,
        # (aka new motion)
        else:
            # Turn on motion light, turn off clear light
            GPIO.output(led1, GPIO.HIGH)
            GPIO.output(led0, GPIO.LOW)
            # set on to True
            on = True


def destroy():

    for ledX in leds:
        # Turn off all leds
        GPIO.output(ledX, GPIO.LOW)

    GPIO.cleanup()


if __name__ == '__main__':
    setup()
    try:
        loop()
        # When ctrl+c is pressed, destroy() is called to cleanup
    except KeyboardInterrupt:
        destroy()
