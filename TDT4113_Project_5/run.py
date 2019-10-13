"""
Code for running the FSM. The code will look for the file password.txt to read the password. If none
exists it will create a new file with the default password '123'.

Type 'python run.py' to start the FSM

*** Operation of FSM ***

When starting, push any button to wake up the system.

Type the password followed by '*' to log in. Pushing '#' will go back to the start state.

When logged in:
    '#' - Log out and go back to start state
    '*' - Initiate creation of new password. Type the new password followed by '*' to validate it, the
          type the old password followed by '*' again to confirm. Type '#' to cancel.
    '0-5' - Select one of the LED lights to light up. Type the number of seconds followed by '*' to
            execute. Type '#' to cancel.
    '6' - Select to light up all the LED lights. Type the number of seconds followed by '*' to execute.
          Type '#' to cancel.
    '7' - Select to make all the LED lights twinkle. Type the number of seconds followed by '*' to
          execute. Type '#' to cancel.

"""
from fsm import FSM
from kpc_agent import KPCAgent
from ledboard import LEDBoard
from keypad import Keypad
from rule import Rule, match_any_signal, match_numeric_signal, match_signal_0_5

START_STATE = 'start_state'
END_STATE = 'end_state'


# TODO: Search through FSM for wrong outputs (LED output) (Have seen several)


def main():
    """Run FSM"""

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

    keypad = Keypad()
    ledboard = LEDBoard()
    agent = KPCAgent(keypad, ledboard)
    fsm = FSM(rules, agent, START_STATE, END_STATE)
    fsm.main_loop()


if __name__ == '__main__':
    main()
