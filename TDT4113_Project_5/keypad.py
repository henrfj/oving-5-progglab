"""Keypad class that serves as interface between Agent object and physical keypad"""

import RPi.GPIO as GPIO
import time

class Keypad:

    layout = [['1', '2', '3'],
     ['4', '5', '6'],
      ['7', '8,', '9'],
       ['*', '0', '#']]

    def __init__(self):
        """Setup Keypad pins"""
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
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
        Poll the physical keypad and return which key is being pressed as a string. Return -1 if no key is being
        pressed.
        """
        
        
        for row, rp in enumerate(self.row_pins):
            GPIO.output(rp, GPIO.HIGH)
            for col, cp in enumerate(self.col_pins):
                if GPIO.input(cp) == GPIO.HIGH:
                    return (row, col)
            GPIO.output(rp, GPIO.LOW)
    
        return -1

    def get_next_signal(self):
        """
        Repeatedly  poll the physical keypad until a key press is detected.
        :return: one of the following chars: "0123456789*#"
        """
        
        returnvalue = -1
        while returnvalue == -1:
            # Making sure we dont return an inactive reading
            count = 0
            prev_coord = -1
            coord = -1
            
            while count < 20:
                # Makeing sure to return a stable reading
                coord = self.do_polling()
                if coord == prev_coord:
                    count += 1
                    
                else:
                    count = 0

                prev_coord = coord
                time.sleep(0.010)
                
            returnvalue = coord

        x = returnvalue[0]
        y = returnvalue[1]

        print("X: ", x, "Y: ", y)
        return self.layout[x][y]
        

        # TODO: we only get the columns not rows when we press