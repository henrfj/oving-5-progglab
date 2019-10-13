"""LEDBoard class that serves as an interface between the KPC agent and the physical LED board"""

import RPi.GPIO as GPIO
import time

# TODO: k might actually be a string object and not an int

class LEDBoard:

    pins = [16, 20, 21]
    pin_led_states = [
          [1, 0, -1], # A
          [0, 1, -1], # B
          [-1, 1, 0], # C
          [-1, 0, 1], # D
          [1, -1, 0], # E
          [0, -1, 1]  # F
        ]
    
    def __init__(self):
        """Setup LED board pins"""

           


    def light_led(self, id, k):
        """
        Turns on one light in the LED board for k seconds

        :param id: the light to be turned on (int) in 0 - 5
        :param k: number of seconds (int)
        """
        print("Lighting one led:", id, k)

        for pin_index, pin_state in enumerate(self.pin_led_states[led_number]):
            self.set_pin(pin_index, pin_state)
        time.sleep(k)
        
        # Turns all leds off
        self.set_pin(0, -1)
        self.set_pin(1, -1)
        self.set_pin(2, -1)

    def set_pin(pin_index, pin_state):
        if pin_state == -1:
            GPIO.setup(pins[pin_index], GPIO.IN)
        else:
            GPIO.setup(pins[pin_index], GPIO.OUT)
            GPIO.output(pins[pin_index], pin_state)



    def flash_all_leds(self, k):
        """
        Turns on all led lights for k seconds

        :param k: number of seconds (int)
        """
        print("Flashing all lights!")

        # TODO: test if quickly turnig all leds on and off in sequence will appear as flashing




    def twinkle_all_leds(self, k):
        """
        Turns on and off all led lights sequentially for k seconds
        :param k: number of seconds (int)
        """



    def power_up(self):
        """Executes the power up lighting sequence"""

    def power_down(self):
        """Executes the power down lighting sequence"""

    def success(self):
        """Executes lighting sequence indicating success"""

    def failure(self):
        """Executes lighting sequence indicating failure"""
