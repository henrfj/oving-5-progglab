"""KPC Agent class for computation and high-level interaction with keypad / LED board"""

import os

PASSWORD_PATH = 'password.txt'
DEFAULT_PASSWORD = '1234'
LEGAL_SYMBOLS = '0123456789'


class KPCAgent:

    def __init__(self, keypad, ledboard):
        """
        Initialize KPCAgent

        :param keypad:
        :param ledboard:
        """

        self.keypad = keypad
        self.ledboard = ledboard
        self.override_signal = None
        self.password_buffer = ''
        self.new_password = None
        self.led_id = None
        self.led_duration = None

    def get_next_signal(self):
        """Get the next signal. Returns override signal if it is set, otherwise polls keypad."""
        if self.override_signal is not None:
            signal = self.override_signal
            self.override_signal = None
            return signal
        else:
            return self.keypad.get_next_signal()

    def do_nothing(self, signal):
        """The agent does nothing"""

    def init_password_entry(self, signal):
        """Readies the agent for receiving a password"""
        self.password_buffer = ''
        self.ledboard.power_up()

    def add_signal_to_password(self, signal):
        """Adds the signal to the password buffer"""
        self.password_buffer += signal

    @staticmethod
    def _get_stored_password():
        """Reads the stored password from file. Returns default password if no file exists."""
        if not os.path.isfile(PASSWORD_PATH):
            return DEFAULT_PASSWORD

        with open(PASSWORD_PATH, 'r') as file:
            password = file.readline().strip()
            return password

    def verify_login(self, signal):
        """Checks if buffer matches stored password, saves result in override, shows appropriate lighting sequence"""
        stored_password = KPCAgent._get_stored_password()
        if stored_password == self.password_buffer:
            self.override_signal = 'Y'
            self.ledboard.success()
        else:
            self.override_signal = 'N'
            self.ledboard.failure()

    def validate_password_change(self, signal):
        """Checks whether password buffer is all numeric and >= 4 chars and shows appropriate lighting sequence"""
        legal = True
        for symbol in self.password_buffer:
            if symbol not in LEGAL_SYMBOLS:
                legal = False
                break
        if len(self.password_buffer) < 4:
            legal = False

        if legal:
            self.override_signal = 'Y'
            self.ledboard.success()
        else:
            self.override_signal = 'N'
            self.ledboard.failure()

    def temp_store_new_password(self, signal):
        """Temporarily stores the new password"""
        self.new_password = self.password_buffer
        self.init_password_entry(signal)

    def save_new_password(self, signal):
        """Saves the new password, overwriting the old one"""
        with open(PASSWORD_PATH, 'w') as file:
            file.write(self.new_password)

    def reset_led_duration(self, signal):
        """Reset led duration"""
        self.led_duration = ''

    def store_led_id(self, signal):
        """Stores the signal as the led id"""
        self.led_id = signal
        self.reset_led_duration(signal)

    def add_signal_to_led_duration(self, signal):
        """Appends the signal to the led duration"""
        self.led_duration += signal

    def light_one_led(self, signal):
        """Turn on LED light specified by led_id for led_duration seconds"""
        led_id = int(self.led_id)
        led_duration = int(self.led_duration)
        self.ledboard.light_led(led_id, led_duration)

    def flash_leds(self, signal):
        """Flash all LED lights for led_duration seconds"""
        led_duration = int(self.led_duration)
        self.ledboard.flash_all_leds(led_duration)

    def twinkle_leds(self, signal):
        """Twinkle all LED lights for led_duration seconds"""
        led_duration = int(self.led_duration)
        self.ledboard.twinkle_all_leds(led_duration)

    def exit_action(self, signal):
        """Show the power down lighting sequence"""
        self.ledboard.power_down()
