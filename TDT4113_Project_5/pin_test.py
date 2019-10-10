import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

test_pin = 0
while test_pin != -1:
    test_pin = int(input("Enter what pin will you test: "))
    print("You entered pin nr. :", test_pin)
    GPIO.setup(test_pin,GPIO.OUT)
    print ("LED on")
    GPIO.output(test_pin,GPIO.HIGH)
    input ("press enter to turn off")
    print ("LED off")
    GPIO.output(test_pin,GPIO.LOW)
    time.sleep(1)

