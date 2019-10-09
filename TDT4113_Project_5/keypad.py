"""Keypad class that serves as interface between Agent object and physical keypad"""

import RPi.GPIO as GPIO


class Keypad:

    def __init__(self):
        """Setup Keypad pins"""

    def do_polling(self):
        """
        Poll the physical keypad and return which key is being pressed as a string. Return None if no key is being
        pressed.
        """

    def get_next_signal(self):
        """
        Repeatedly  poll the physical keypad until a key press is detected.
        :return:
        """
