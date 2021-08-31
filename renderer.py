import pygame


class Renderer:
    def __init__(self, context):
        self.context = context
        self.screen = self.context.screen
        self.strategy = None

    def screen_width(self):
        return self.screen.get_width()

    def screen_height(self):
        return self.screen.get_height()

    def reset(self, x_tiles, y_tiles):
        self.strategy.reset(
            x_tiles,
            y_tiles,
            self.screen_width(),
            self.screen_height()
        )

    def blit_surface(self, surface, x_pos, y_pos):
        self.screen.blit(surface, (x_pos, y_pos))

    def draw_rect(self, x_pos, y_pos, width, height, color, outline):
        x_pos, y_pos, width, height = self.strategy.world_cords_to_screen_cords(
            x_pos,
            y_pos,
            width,
            height
        )

        pygame.draw.rect(
            self.screen,
            color,
            (
                x_pos,
                y_pos,
                width,
                height
            ),
            outline
        )
