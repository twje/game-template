from renderer_strategy import WindowRendererStratgey
from map_registry import map_registry
from state import State
from entity import create_entity_by_id


class World(State):
    def __init__(self, context, stack, map):
        super().__init__()
        self.context = context
        self.stack = stack
        self.map = map
        self.hide_player = False
        self.player = create_entity_by_id("player", 3, 3)

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
        self.player.controller.handle_input(event)

    def update(self, dt):
        self.player.controller.update(dt)
        for npc in self.map.npcs:
            npc.controller.update(dt)

        return False

    def render(self, renderer):
        player = self.player
        if self.hide_player:
            player = None

        self.map.render(renderer, player)
