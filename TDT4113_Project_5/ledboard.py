"""LEDBoard class that serves as an interface between the KPC agent and the physical LED board"""

import RPi.GPIO as GPIO


class LEDBoard:

    def __init__(self):
        """Setup LED board pins"""

    def light_led(self, id, k):
        """
        Turns on one light in the LED board for k seconds

        :param id: the light to be turned on (int)
        :param k: number of seconds (int)
        """

    def flash_all_leds(self, k):
        """
        Turns on all led lights for k seconds

        :param k: number of seconds (int)
        """

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
