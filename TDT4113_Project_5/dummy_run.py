from rule import Rule, match_numeric_signal, match_signal_0_5, match_any_signal
from fsm import FSM
from kpc_agent import KPCAgent

START_STATE = 'start_state'
END_STATE = 'end_state'


class DummyKeypad:

    def __init__(self):
        """Setup Keypad pins"""

    def do_polling(self):
        """
        Poll the physical keypad and return which key is being pressed as a string. Return None
        if no key is being pressed.
        """

    def get_next_signal(self):
        """
        Repeatedly  poll the physical keypad until a key press is detected.
        :return:
        """
        signal = input('Type next input: ')
        return signal


class DummyLEDBoard:

    def __init__(self):
        """Setup LED board pins"""

    def light_led(self, id, k):
        """
        Turns on one light in the LED board for k seconds

        :param id: the light to be turned on (int)
        :param k: number of seconds (int)
        """

        print('Lighting', id, 'for', k, 'seconds')

    def flash_all_leds(self, k):
        """
        Turns on all led lights for k seconds

        :param k: number of seconds (int)
        """

        print('Lighting all LEDs for',k, 'seconds')

    def twinkle_all_leds(self, k):
        """
        Turns on and off all led lights sequentially for k seconds

        :param k: number of seconds (int)
        """

        print('Twinkling all LEDs for', k, 'seconds')

    def power_up(self):
        """Executes the power up lighting sequence"""
        print('Power up')

    def power_down(self):
        """Executes the power down lighting sequence"""
        print('Power down')

    def success(self):
        """Executes lighting sequence indicating success"""
        print('Success')

    def failure(self):
        """Executes lighting sequence indicating failure"""
        print('Failure')


def run():
    rules = [
        Rule(
            'start_state',
            'logged_out',
            match_any_signal,
            KPCAgent.init_password_entry),
        Rule('logged_out', 'start_state', '#', KPCAgent.exit_action),
        Rule(
            'logged_out',
            'logged_out',
            match_numeric_signal,
            KPCAgent.add_signal_to_password),
        Rule('logged_out', 'verify_login', '*', KPCAgent.verify_login),
        Rule('verify_login', 'logged_in', 'Y', KPCAgent.do_nothing),
        Rule('verify_login', 'logged_out', 'N', KPCAgent.init_password_entry),
        Rule('logged_in', 'start_state', '#', KPCAgent.exit_action),

        # Create new password
        Rule('logged_in', 'create_new_password',
             '*', KPCAgent.init_password_entry),
        Rule(
            'create_new_password',
            'create_new_password',
            match_numeric_signal,
            KPCAgent.add_signal_to_password),
        Rule('create_new_password', 'logged_in', '#', KPCAgent.do_nothing),
        Rule(
            'create_new_password',
            'validate_new_password',
            '*',
            KPCAgent.validate_password_change),
        Rule(
            'validate_new_password',
            'confirm_new_password',
            'Y',
            KPCAgent.temp_store_new_password),
        Rule('validate_new_password', 'logged_in', 'N', KPCAgent.do_nothing),
        Rule(
            'confirm_new_password',
            'confirm_new_password',
            match_numeric_signal,
            KPCAgent.add_signal_to_password),
        Rule('confirm_new_password', 'logged_in', '#', KPCAgent.do_nothing),
        Rule(
            'confirm_new_password',
            'verify_confirmation',
            '*',
            KPCAgent.verify_login),
        Rule(
            'verify_confirmation',
            'logged_in',
            'Y',
            KPCAgent.save_new_password),
        Rule('verify_confirmation', 'logged_in', 'N', KPCAgent.do_nothing),

        # Flash single light
        Rule(
            'logged_in',
            'flash_single_light',
            match_signal_0_5,
            KPCAgent.store_led_id),
        Rule(
            'flash_single_light',
            'flash_single_light',
            match_numeric_signal,
            KPCAgent.add_signal_to_led_duration),
        Rule('flash_single_light', 'logged_in', '#', KPCAgent.do_nothing),
        Rule('flash_single_light', 'logged_in', '*', KPCAgent.light_one_led),

        # Flash all lights
        Rule(
            'logged_in',
            'flash_all_lights',
            '6',
            KPCAgent.reset_led_duration),
        Rule(
            'flash_all_lights',
            'flash_all_lights',
            match_numeric_signal,
            KPCAgent.add_signal_to_led_duration),
        Rule('flash_all_lights', 'logged_in', '#', KPCAgent.do_nothing),
        Rule('flash_all_lights', 'logged_in', '*', KPCAgent.flash_leds),

        # Twinkle all lights
        Rule('logged_in', 'twinkle_all_lights',
             '7', KPCAgent.reset_led_duration),
        Rule(
            'twinkle_all_lights',
            'twinkle_all_lights',
            match_numeric_signal,
            KPCAgent.add_signal_to_led_duration),
        Rule('twinkle_all_lights', 'logged_in', '#', KPCAgent.do_nothing),
        Rule('twinkle_all_lights', 'logged_in', '*', KPCAgent.twinkle_leds)
    ]

    keypad = DummyKeypad()
    ledboard = DummyLEDBoard()
    agent = KPCAgent(keypad, ledboard)
    fsm = FSM(rules, agent, START_STATE, END_STATE)
    fsm.main_loop()


if __name__ == '__main__':
    run()
