from state_stack import StateStack
from state import State


class StoryboardEvent:
    def __init__(self, factory):
        self.factory = factory
        self.event = None

    def update(self, storyboard, dt):
        if self.event is None:
            self.event = self.factory(storyboard)
        self.event.update(dt)

    def is_blocking(self):
        return self.event.is_blocking()

    def is_finished(self):
        return self.event.is_finished()


class Storyboard(State):
    HAND_IN_SCENE = "handin"

    def __init__(self, stack, events, hand_in_scene):
        super().__init__()
        self.stack = stack
        self.events = [StoryboardEvent(event) for event in events]
        self.states = {}
        self.internal_stack = StateStack()
        self.finished_events = []

        if hand_in_scene:
            state = self.stack.pop()
            self.push_state(self.HAND_IN_SCENE, state)

    def enter(self):
        pass

    def exit(self):
        pass

    def handle_event(self, event):
        pass

    def update(self, dt):
        self.internal_stack.update(dt)

        if len(self.events) == 0:
            self.pop_self()

        self.finished_events.clear()
        for event in self.events:
            event.update(self, dt)
            if event.is_finished():
                self.finished_events.append(event)
            if event.is_blocking():
                break

        for event in self.finished_events:
            self.events.remove(event)

    def render(self, renderer):
        self.internal_stack.render(renderer)

    def push_state(self, state_id, state):
        assert(state_id not in self.states)
        self.states[state_id] = state
        self.internal_stack.push(state)

    def remove_state(self, state_id):
        state = self.states[state_id]
        del self.states[state_id]
        self.internal_stack.states.remove(state)

    def pop_self(self):
        self.stack.pop()
