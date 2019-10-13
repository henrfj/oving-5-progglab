"""LEDBoard class that serves as an interface between the KPC agent and the physical LED board"""

import RPi.GPIO as GPIO
import time

# TODO: k might actually be a string object and not an int

class LEDBoard:

    
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
        self.pins = [16, 20, 21]
           
    def light_led(self, id, k):
        """
        Turns on one light in the LED board for k seconds

        :param id: the light to be turned on (int) in 0 - 5
        :param k: number of seconds (int)
        """
        
        for pin_index, pin_state in enumerate(self.pin_led_states[led_number]):
            self.set_pin(pin_index, pin_state)
        time.sleep(k)
        
        # Turns all leds off
        self.reset_pins()

    def set_pin(pin_index, pin_state):
        if pin_state == -1:
            GPIO.setup(self.pins[pin_index], GPIO.IN)
        else:
            GPIO.setup(self.pins[pin_index], GPIO.OUT)
            GPIO.output(self.pins[pin_index], pin_state)

    @staticmethod
    def reset_pins():
        self.set_pin(0, -1)
        self.set_pin(1, -1)
        self.set_pin(2, -1)

    def flash_all_leds(self, k):
        """
        Turns on all led lights for k seconds

        :param k: number of seconds (int)
        """
        print("Flashing all lights!")
        start_time = time.time()
        elapsed_time = 0

        while elapsed_time < k:
            
            start_time2 = time.time()
            elapsed_time2 = 0
            i = 0
            while elapsed_time2 < 0.5:
                #light a led without delay
                self.light_led(i, 0)
                i+=1
                if i > 5:
                    i = 0
                elapsed_time2 = time.time() - start_time2
            
            elapsed_time = time.time() - start_time
            if elapsed_time > k:
                break

            # Turn all lights off
            self.reset_pins()

            start_time3 = time.time()
            elapsed_time3 = 0
            while elapsed_time3 < 0.5:
                elapsed_time3 = time.time() - start_time3

            elapsed_time = time.time() - start_time

        # In case we are cut short
        self.reset_pins()

    def twinkle_all_leds(self, k):
        """
        Turns on and off all led lights sequentially for k seconds
        :param k: number of seconds (int)
        """

        start_time = time.time()
        elapsed_time = 0
        i = 0

        while elapsed_time < k:
            self.light_led(i%5, 0.2)
            i += 1
            elapsed_time = time.time() - start_time

        self.reset_pins()

    def power_up(self):
        """Executes the power up lighting sequence"""

    def power_down(self):
        """Executes the power down lighting sequence"""

    def success(self):
        """Executes lighting sequence indicating success"""

    def failure(self):
        """Executes lighting sequence indicating failure"""
