from window import Window
from context import Context
from scene_manager import SceneManager
import pygame


class Application:
    def __init__(self, width, height, caption):
        self.window = Window(width, height, caption, self.handle_event)
        self.context = Context(self.window.screen)
        self.scene_manager = SceneManager(self.context)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.elapsed_time = 0

    def add_scene(self, scene_id, scene):
        self.scene_manager.add_scene(scene_id, scene)

    def set_start_scene(self, level_id):
        self.scene_manager.set_scene(level_id)

    def run(self):
        while not self.window.is_done:
            self.update()
            self.render()
            self.restart_clock()

        self.destroy()

    def handle_event(self, event):
        self.scene_manager.handle_event(event)

    def update(self):
        self.window.update()
        self.scene_manager.update(self.elapsed_time)

    def render(self):
        self.window.begin_render()
        self.scene_manager.render()
        self.window.end_render()

    def restart_clock(self):
        self.elapsed_time = self.clock.tick(self.fps)/1000

    def destroy(self):
        self.window.destroy()
