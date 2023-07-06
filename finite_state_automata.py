class State:
    def __init__(self, name=None, is_start_state=False, is_final_state=False):
        self.in_symbols = []
        self.transitions = []
        self.name = name
        self.is_start_state = is_start_state
        self.is_final_state = is_final_state

    def add_transition(self, symbol, next_state):
        self.in_symbols.append(symbol)
        self.transitions.append(next_state)

    def _accept(self, symbol):
        if symbol not in self.in_symbols:
            raise ValueError(f"The symbol '{symbol}' is not in the accepted set {self.in_symbols}")
        return self.transitions[self.in_symbols.index(symbol)]

class FSA:
    def __init__(self):
        self.input_tape = None
        self.head = None
        self.curr_state = None

        self.states = []

    def _add_single_state(self, state):
        if state.is_start_state:
            if self.head is not None:
                raise ValueError("Cannot have two starting states")
            self.curr_state = state
        self.states.append(state)

    def add_state(self, states):
        if type(states) == list:
            for s in states:
                self._add_single_state(s)
        else:
            self._add_single_state(states)

    def load_tape(self, tape):
        self.input_tape = tape

    def run(self):
        for sym in self.input_tape:
            self.curr_state = self.curr_state._accept(sym)
        if self.curr_state.is_final_state:
            print(f"The string '{self.input_tape}' is accepted")
        else:
            raise ValueError(f"{self.curr_state.name} is not a final state")
        


if __name__ == "__main__":
    A = State(name='A', is_start_state=True)
    B = State(name='B')
    C = State(name='C', is_final_state=True)

    A.add_transition("1", A)
    A.add_transition("0", B)

    B.add_transition("1", A)
    B.add_transition("0", C)

    C.add_transition("0", C)
    C.add_transition("1", C)

    my_fsa = FSA()
    my_fsa.add_state([A, B, C])
