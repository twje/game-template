from renderer_strategy import WindowRendererStratgey
from map_registry import map_registry
from boid import Boid
from state import State


class World(State):
    def __init__(self, context, stack, map):
        super().__init__()
        self.context = context
        self.stack = stack        
        self.map = map
        self.hide_player = False
        self.player = Boid(3, 3, 0) 

    def enter(self):
        self.set_render_units()

    def exit(self):
        pass

    def switch_map(self, identifier):
        self.map = map_registry[identifier]()
        self.set_render_units()

    def set_render_units(self):
        renderer = self.context.renderer
        renderer.strategy = WindowRendererStratgey()
        renderer.reset(
            self.map.map_width,
            self.map.map_height
        )

    def handle_event(self, event):
        self.player.handle_event(event)

    def update(self, dt):
        for npc in self.map.npcs:
            npc.update(dt)

        return False

    def render(self, renderer):
        player = self.player
        if self.hide_player:
            player = None

        self.map.render(renderer, player)
