from sre_parse import State


class Spinner:
    def __init__(self, par1):
        self.states = par1
    
    def state(self):
        return State