from . import register_state
from state import State
import pygame


@register_state("wait")
class WaitState(State):
    def __init__(self, entity):
        super().__init__()
        self.controller = entity.controller

    def enter(self, data):
        pass

    def exit(self):
        pass

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_left()
            if event.key == pygame.K_RIGHT:
                self.move_right()
            if event.key == pygame.K_UP:
                self.move_up()
            if event.key == pygame.K_DOWN:
                self.move_down()

    def update(self, dt):
        pass

    def render(self, renderer):
        pass

    def move_left(self):
        self.controller.change("move", dict(x=-1, y=0))

    def move_up(self):
        self.controller.change("move", dict(x=0, y=-1))

    def move_right(self):
        self.controller.change("move", dict(x=1, y=0))

    def move_down(self):
        self.controller.change("move", dict(x=0, y=1))
