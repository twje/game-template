from state import NullState


class StateMachine:
    def __init__(self):
        self.states = {}
        self.current = NullState()

    def set_state(self, state_id, state):
        self.states[state_id] = state

    def change(self, state_id, enter_params={}):
        if state_id not in self.states:
            raise Exception(f"state {state_id} must exist")
        self.current.exit()
        self.current = self.states[state_id]()
        self.current.enter(enter_params)

    def update(self, dt):
        self.current.update(dt)

    def render(self, renderer):
        self.current.render(renderer)

    def handle_input(self, event):
        self.current.handle_event(event)
