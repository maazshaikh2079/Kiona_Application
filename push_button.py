import RPi.GPIO as GPIO
import time

# Set GPIO mode (BCM mode)
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin for the button
button_pin = 18
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # Read the state of the button
        button_state = GPIO.input(button_pin)

        # Check if the button is pressed
        if button_state == GPIO.LOW:
            print("Button is pressed")
        else:
            print("Button is not pressed")

        # Delay to debounce the button
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nExiting program")

finally:
    # Clean up GPIO
    GPIO.cleanup()
