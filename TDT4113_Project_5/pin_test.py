import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

test_pin = 0
while test_pin != -1:
    test_pin = int(input("Enter what pin will you test: -1 for Charlietest"))
    print("You entered pin nr. :", test_pin)
    GPIO.setup(test_pin,GPIO.OUT)
    print ("LED on")
    GPIO.output(test_pin,GPIO.HIGH)
    input ("press enter to turn off")
    print ("LED off")
    GPIO.output(test_pin,GPIO.LOW)
    time.sleep(1)


print("Charlietest!")

GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21, GPIO.IN

GPIO.output(16,GPIO.HIGH)
GPIO.output(20,GPIO.LOW)


print("16 is High and 20 is low, output")
print (" pin 21 is input~~Ground")

# ALL relevant pins and T-cobbler are tested and are working. 
