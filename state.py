from abc import ABC
from abc import abstractmethod


class State(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def enter(self, data):
        pass

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def handle_event(self, event):
        pass

    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def render(self, renderer):
        pass


class NullState(State):
    def __init__(self):
        super().__init__()

    def enter(self, data):
        pass

    def exit(self):
        pass

    def handle_event(self, event):
        pass

    def update(self, dt):
        pass

    def render(self, renderer):
        pass
