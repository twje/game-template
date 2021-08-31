from . import register_state
from state import State
from tween import Tween


@register_state("move")
class MoveStates(State):
    def __init__(self, entity):
        super().__init__()
        self.entity = entity
        self.controller = self.entity.controller
        self.move_speed = 0.3

        # initilized on enter
        self.x_move = None
        self.y_move = None
        self.x_pixel = None
        self.y_pixel = None
        self.tween = None

    def enter(self, data):
        self.x_move = data["x"]
        self.y_move = data["y"]
        self.x_pixel = self.entity.x_pos
        self.y_pixel = self.entity.y_pos
        self.tween = Tween(0, 1, self.move_speed)

    def exit(self):
        pass

    def handle_event(self, event):
        pass

    def update(self, dt):
        self.tween.update(dt)

        value = self.tween.value
        x = self.x_pixel + (value * self.x_move)
        y = self.y_pixel + (value * self.y_move)
        self.entity.set_position(x, y)

        if self.tween.is_finished:
            self.controller.change(self.entity.default_state)

    def render(self, renderer):
        pass
