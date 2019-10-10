import RPi.GPIO as GPIO
import time


test_pin = 25
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(test_pin,GPIO.OUT)
print ("LED on")
GPIO.output(test_pin,GPIO.HIGH)
time.sleep(1)
print ("LED off")
GPIO.output(test_pin,GPIO.LOW)
