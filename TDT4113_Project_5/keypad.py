"""Keypad class that serves as interface between Agent object and physical keypad"""

import RPi.GPIO as GPIO


class Keypad:

    layout = [['1', '2', '3'],
     ['4', '5', '6'],
      ['7', '8,', '9'],
       ['*', '0', '#']]

    def __init__(self):
        """Setup Keypad pins"""
        GPIO.setmode(GPIO.BCM)
        self.row_pins = [18, 23, 24, 25]
        self.col_pins = [17, 27, 22]
        

        # Output pins (ROWS)
        for rp in self.row_pins:
            GPIO.setup(rp, GPIO.OUT)
    
        # Input pins (COLUMNS)
        for cp in self.col_pins:
            GPIO.setup(cp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
        



    def do_polling(self):
        """
        Poll the physical keypad and return which key is being pressed as a string. Return None if no key is being
        pressed.
        """
        
        row = 0
        col = 0

        for rp in self.row_pins:
            GPIO.output(rp, GPIO.HIGH)
            for cp in self.col_pins:
                if GPIO.input(cp) == GPIO.HIGH:
                    return (row, col)
                col += 1
            GPIO.output(rp, GPIO.LOW)
            row += 1

        return -1

    def get_next_signal(self):
        """
        Repeatedly  poll the physical keypad until a key press is detected.
        :return:
        """
        coord = self.do_polling()
        if coord != -1:
            print(layout[coord[0]][coord[1]])
            return layout[coord[0]][coord[1]]
        return 'p'  # is always not a match of any rule

