import RPi.GPIO as GPIO
import time

# Define GPIO pins
PIR_SENSOR_PIN = 17    # PIR sensor output connected to GPIO 17
BUZZER_PIN = 27        # Buzzer connected to GPIO 27
LED_PIN = 22           # LED connected to GPIO 22

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_SENSOR_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)

def activate_alarm():
    """Activates the buzzer and LED when motion is detected."""
    GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Turn on buzzer
    GPIO.output(LED_PIN, GPIO.HIGH)     # Turn on LED
    time.sleep(1)                       # Keep alarm active for 1 second
    GPIO.output(BUZZER_PIN, GPIO.LOW)   # Turn off buzzer
    GPIO.output(LED_PIN, GPIO.LOW)      # Turn off LED

try:
    print("Security System Activated. Waiting for motion...")
    while True:
        if GPIO.input(PIR_SENSOR_PIN):
            print("Motion detected!")
            activate_alarm()
            time.sleep(2)  # Delay before rechecking motion to prevent continuous triggering
        else:
            print("No motion.")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("System shutting down...")

finally:
    GPIO.cleanup()  # Reset GPIO settings on exit
