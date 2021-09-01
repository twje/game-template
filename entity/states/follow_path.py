from . import register_state
from state import State


@register_state("follow_path")
class FollowPath(State):
    def __init__(self, entity, context):
        super().__init__()
        self.entity = entity
        self.controller = entity.controller

    def enter(self, data):        
        if self.entity.is_path_complete():
            self.entity.reset_default_state()
            return

        direction = self.entity.path_direction()
        if direction == "left":
            return self.controller.change("move", dict(x=-1, y=0))
        if direction == "up":
            return self.controller.change("move", dict(x=0, y=-1))
        if direction == "right":
            return self.controller.change("move", dict(x=1, y=0))
        if direction == "down":
            return self.controller.change("move", dict(x=0, y=1))

    def exit(self):
        self.entity.increment_path()

    def handle_event(self, event):
        pass

    def update(self, dt):
        pass

    def render(self, renderer):
        pass
