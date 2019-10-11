import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

test_pin = 0
while test_pin != -1:
    test_pin = int(input("Enter what pin will you test( '-1' for Charlietest): "))
    if test_pin != -1:
        print("You entered pin nr. :", test_pin)
        GPIO.setup(test_pin,GPIO.OUT)
        print ("LED on")
        GPIO.output(test_pin,GPIO.HIGH)
        input ("press enter to turn off")
        print ("LED off")
        GPIO.output(test_pin,GPIO.LOW)
        time.sleep(1)


print("Charlietest!")
pins = [16, 20, 21]

pin_led_states = [
  [1, 0, -1], # A
  [0, 1, -1], # B
  [-1, 1, 0], # C
  [-1, 0, 1], # D
  [1, -1, 0], # E
  [0, -1, 1]  # F
]

def set_pin(pin_index, pin_state):
    if pin_state == -1:
        GPIO.setup(pins[pin_index], GPIO.IN)
    else:
        GPIO.setup(pins[pin_index], GPIO.OUT)
        GPIO.output(pins[pin_index], pin_state)

def light_led(led_number):
    for pin_index, pin_state in enumerate(pin_led_states[led_number]):
        set_pin(pin_index, pin_state)

set_pin(0, -1)
set_pin(1, -1)
set_pin(2, -1)

while True:
    x = int(input("Pin (0 to 5):"))
    light_led(x)

# ALL relevant pins and T-cobbler are tested and are working. 
