class CalculatorMemento:
    def __init__(self, history_state):
        self.history_state = history_state.copy()

    def get_state(self):
        return self.history_state.copy()