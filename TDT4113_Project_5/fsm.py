"""Finite State Machine (FSM) class"""


class FSM:

    def __init__(self, rules, agent, start_state, end_state):
        """
        Finite state machine

        :param rules: list of Rule objects
        :param agent: Agent object
        :param start_state: initial state
        :param end_state: final state
        """

        self.rules = rules
        self.agent = agent
        self.state = start_state
        self.end_state = end_state

    def main_loop(self):
        """Repeatedly gets the next input and runs the rules until the end state is reached"""
        while self.state != self.end_state:
            signal = self.agent.get_next_signal()
            self.run_rules(signal)

    def run_rules(self, signal):
        """
        Iterates over the rules, fires the first rule that matches and updates the state accordingly

        :param signal:
        """

        for rule in self.rules:
            if rule.match(self.state, signal):
                next_state = rule.fire(self.agent, signal)
                self.state = next_state
                break
