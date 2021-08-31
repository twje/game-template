from utils import create_text


class Text:
    def __init__(self, text, size, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rendered_text = create_text(text, size)

    def handle_event(self, event):
        pass

    def update(self, dt):
        pass

    def render(self, renderer):
        renderer.blit_surface(
            self.rendered_text,
            self.x_pos,
            self.y_pos
        )
