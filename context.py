from renderer import Renderer


class Context:
    def __init__(self, screen):
        self.screen = screen
        self.renderer = Renderer(self)
        self.data = {}

    def add_data(self, key, value):
        self.data[key] = value

    def get_data(self, key):
        return self.data[key]
