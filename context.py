from renderer import Renderer
from message_handler import MessageHandler


class Context:
    def __init__(self, screen):
        self.screen = screen
        self.renderer = Renderer(self)
        self.message_handler = MessageHandler()
        self.data = {}

    def add_data(self, key, value):
        self.data[key] = value

    def get_data(self, key):
        return self.data[key]
