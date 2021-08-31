from pygame.constants import SWSURFACE
import colors
from camera import Camera
from tween import Tween
import constants
import pygame


class Boid:
    def __init__(self, pos_x, pos_y, angle):
        self.camera = Camera(pos_x, pos_y, angle, 60)
        self.moved = False
        self.path = []
        self.tween = Tween(0, 1, 1)
        self.foo = [1, 2, 3]

    def handle_event(self, event):
        self.moved = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.camera.pos_x -= 1
                self.moved = True
            if event.key == pygame.K_RIGHT:
                self.camera.pos_x += 1
                self.moved = True
            if event.key == pygame.K_UP:
                self.camera.pos_y -= 1
                self.moved = True
            if event.key == pygame.K_DOWN:
                self.camera.pos_y += 1
                self.moved = True

    def update(self, dt):
        if self.is_path_complete():
            return

        self.tween.update(dt)
        if self.tween.value == 1:
            direction = self.path[0]
            if direction == constants.Direction.LEFT:
                self.camera.pos_x -= 1
            elif direction == constants.Direction.RIGHT:
                self.camera.pos_x += 1
            elif direction == constants.Direction.TOP:
                self.camera.pos_y -= 1
            elif direction == constants.Direction.BUTTOM:
                self.camera.pos_y += 1
            self.tween = Tween(0, 1, 1)
            del self.path[0]

    def render(self, renderer):
        renderer.draw_rect(
            self.camera.pos_x,
            self.camera.pos_y,
            1,
            1,
            colors.WHITE,
            0
        )

    def follow_path(self, path):
        self.path = path

    def is_path_complete(self):
        return len(self.path) == 0
