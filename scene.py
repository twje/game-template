from abc import ABC
from abc import abstractmethod


class Scene(ABC):
    def __init__(self):
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
