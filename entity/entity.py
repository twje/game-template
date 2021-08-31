from state_machine import StateMachine
from .states import state_registry
import colors


class Entity:
    def __init__(self, entity_def, x_pos, y_pos):
        self.controller = self.create_controller(entity_def)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.path = None
        self.path_index = -1
        self.default_state = entity_def["state"]
        self.prv_default_state = self.default_state

        self.controller.change(self.default_state)

    def set_position(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def create_controller(self, entity_def):
        controller = StateMachine()
        states = entity_def["controller"]
        for state_id in states:
            factory = self.state_factory(state_id, self)
            controller.set_state(state_id, factory)

        return controller

    def state_factory(self, state_id, entity):
        def create():
            clazz = state_registry[state_id]
            return clazz(entity)
        return create

    def follow_path(self, path):
        self.path_index = 0
        self.path = path
        self.default_state = "follow_path"
        self.controller.change("follow_path")

    def is_path_complete(self):
        return self.path_index >= len(self.path)

    def is_path_exhausted(self):
        return any((
            self.path_index == -1,
            self.is_path_complete()
        ))

    def path_direction(self):
        return self.path[self.path_index]

    def increment_path(self):
        self.path_index += 1

    def reset_default_state(self):
        self.default_state = self.prv_default_state

    def render(self, renderer):
        renderer.draw_rect(
            self.x_pos,
            self.y_pos,
            1,
            1,
            colors.WHITE,
            0
        )
