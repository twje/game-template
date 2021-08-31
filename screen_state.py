from state import State
import utils


class ScreenState(State):
    def __init__(self, screen_width, screen_height, color):
        super().__init__()
        self.color = list(color)
        self.surface = utils.new_surface(
            screen_width,
            screen_height,
            self.color
        )

    def set_alpha(self, alpha):
        self.color[3] = alpha
        self.surface.fill(self.color)

    def enter(self):
        pass

    def exit(self):
        pass

    def handle_event(self, event):
        pass

    def update(self, dt):
        return True

    def render(self, renderer):        
        renderer.blit_surface(self.surface)
