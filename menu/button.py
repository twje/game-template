import utils
import colors
import pygame


class Button:
    def __init__(self, x_pos, y_pos, color, hover_color, callback):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.callback = callback
        self.size = 50
        self.background = utils.new_surface(self.size, self.size, color)
        self.hover = utils.new_surface(self.size, self.size, hover_color)
        self.is_mouse_over = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            if x_mouse > self.x_pos and x_mouse < self.x_pos + self.size and y_mouse > self.y_pos and y_mouse < self.y_pos + self.size:
                self.is_mouse_over = True
            else:
                self.is_mouse_over = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_mouse_over:
                self.callback()

    def update(self, dt):
        pass

    def render(self, renderer):
        image = self.background
        if self.is_mouse_over:
            image = self.hover
        renderer.blit_surface(image, self.x_pos, self.y_pos)
