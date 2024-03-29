import RPi.GPIO as GPIO
import time
from ledboard import LEDBoard

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

ledboard = LEDBoard()
input("Success!")
ledboard.success()
input("Failure")
ledboard.failure()
input("Power down!")
ledboard.power_down()
input("Power up!")
ledboard.power_up()
input("Twinkle all lights!")
ledboard.twinkle_all_leds(10)
input("Flashin all lights!")
ledboard.flash_all_leds(10)




