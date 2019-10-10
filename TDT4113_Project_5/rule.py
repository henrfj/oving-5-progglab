"""Rule class for FSM"""


def match_any_signal(signal):
    """Matches any signal"""
    return True


def match_numeric_signal(signal):
    """Matches any numeric signal"""
    return signal in '0123456789'


def match_signal_0_5(signal):
    """Matches numeric signal"""
    return signal in "012345"


class Rule:

    def __init__(self, state1, state2, signal, action):
        """
        Initializes the rule

        :param state1: FSM must be in state1 for this rule to fire, string or function taking string
        :param state2: FSM will be in state2 after rule fires, must be string
        :param signal: triggering signal, must be string or function accepting string input
        :param action: agent will be instructed to perform action when rule fires
        """

        self.state1 = state1
        self.state2 = state2
        self.signal = signal
        self.action = action

    def match(self, state, signal):
        """
        Determine whether current state and signal matches rule antecedent

        :param state: FSM current state
        :param signal: FSM signal
        :return: True if match, else False
        """

        if isinstance(self.state1, str):
            state_match = self.state1 == state
        else:
            state_match = self.state1(state)

        if isinstance(self.signal, str):
            signal_match = self.signal == signal
        else:
            signal_match = self.signal(signal)

        match = state_match and signal_match
        return match

    def fire(self, agent, signal):
        """
        Rule fires by having the agent execute its action

        :param agent:
        :param signal:
        :return: next state
        """

        self.action(agent, signal)
        return self.state2

