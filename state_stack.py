class StateStack:
    def __init__(self):
        self.states = []

    def handle_event(self, event):
        top = self.top()
        if top is None:
            return

        top.handle_event(event)

    def update(self, dt):
        for state in reversed(self.states):
            update_prior_state = state.update(dt)
            if not update_prior_state:
                break

    def render(self, renderer):
        for state in self.states:
            state.render(renderer)

    def push(self, state):
        self.states.append(state)
        state.enter(None)

    def pop(self):
        top = self.top()
        self.remove_top()
        top.exit()
        return top

    def top(self):
        try:
            return self.states[-1]
        except IndexError:
            return

    def remove_top(self):
        self.states = self.states[:-1]
