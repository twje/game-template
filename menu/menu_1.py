from state import State
from .text import Text
from .button import Button
import colors


class Menu1(State):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.background = parent.create_background()
        self.elements = [
            Text(
                "Menu 1",
                20,
                self.parent.screen_offset,
                self.parent.screen_offset
            ),
            Button(
                150,
                150,
                colors.CYAN,
                colors.WHITE,
                lambda: self.parent.stack.pop()
            ),
            Button(
                300,
                200,
                colors.RED,
                colors.WHITE,
                lambda: self.parent.state_machine.change("menu2")
            )
        ]

    def enter(self, data):
        pass

    def exit(self):
        pass

    def handle_event(self, event):
        for element in self.elements:
            element.handle_event(event)

    def update(self, dt):
        for element in self.elements:
            element.update(dt)

    def render(self, renderer):
        renderer.blit_surface(
            self.background,
            self.parent.screen_offset,
            self.parent.screen_offset
        )
        for element in self.elements:
            element.render(renderer)
