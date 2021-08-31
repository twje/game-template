from state_machine import StateMachine
from state import State
from .menu_1 import Menu1
from .menu_2 import Menu2
from .menu_3 import Menu3
import colors
import utils


def menu_factory(parent, menu):
    def create():
        return menu(parent)
    return create


class InGameMenuState(State):
    def __init__(self, stack, screen_width, screen_height):
        super().__init__()
        self.stack = stack
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_offset = 100
        self.state_machine = StateMachine()
        self.state_machine.set_state("menu1", menu_factory(self, Menu1))
        self.state_machine.set_state("menu2", menu_factory(self, Menu2))
        self.state_machine.set_state("menu3", menu_factory(self, Menu3))
        self.state_machine.change("menu1")

    def create_background(self):
        return utils.new_surface(
            self.screen_width - self.screen_offset * 2,
            self.screen_height - self.screen_offset * 2,
            colors.BLUE
        )

    def enter(self, data):
        pass

    def exit(self):
        pass

    def handle_event(self, event):
        self.state_machine.handle_event(event)

    def update(self, dt):
        self.state_machine.update(dt)
        return False

    def render(self, renderer):
        self.state_machine.render(renderer)
