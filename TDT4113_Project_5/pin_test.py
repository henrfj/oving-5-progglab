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

x = 0
while x in [0, 1, 2, 3, 4, 5]:
    x = int(input("Pin (0 to 5): other input for next test"))
    if x in [0, 1, 2, 3, 4, 5]:
        light_led(x)

set_pin(0, -1)
set_pin(1, -1)
set_pin(2, -1)

k = 10 # Hopefully 10 sec => yes

print ("Testing twinkle all lights")
start_time = time.time()
elapsed_time = 0
i = 0

while elapsed_time < k:
    light_led(i%5, 0.2)
    i += 1
    elapsed_time = time.time() - start_time

set_pin(0, -1)
set_pin(1, -1)
set_pin(2, -1)




print("testing flash all lights")
start_time = time.time()
elapsed_time = 0

while elapsed_time < k:
    
    start_time2 = time.time()
    elapsed_time2 = 0
    i = 0
    while elapsed_time2 < 0.5:
        light_led(i)
        i+=1
        if i > 5:
            i = 0
        elapsed_time2 = time.time() - start_time2
    
    elapsed_time = time.time() - start_time
    if elapsed_time > k:
        break

    # Turn all lights off
    set_pin(0, -1)
    set_pin(1, -1)
    set_pin(2, -1)

    start_time3 = time.time()
    elapsed_time3 = 0
    while elapsed_time3 < 0.5:
        elapsed_time3 = time.time() - start_time3

    elapsed_time = time.time() - start_time

    # In case we are cut short
    set_pin(0, -1)
    set_pin(1, -1)
    set_pin(2, -1)
        


