from renderer_strategy import WindowRendererStratgey
from map_registry import map_registry
from state import State
from constants import MessageID
from entity import create_entity_by_id
import pygame


class World(State):
    def __init__(self, context, stack, map):
        super().__init__()
        self.context = context
        self.stack = stack
        self.map = map
        self.message_handler = self.context.message_handler
        self.hide_player = False
        self.player = create_entity_by_id("player", context, 3, 3)

    def notify(self, message):
        message.response = self.map

    def on_use_action(self):
        x, y = self.player.get_faced_tile_coords()
        trigger = self.map.get_trigger(x, y)
        if trigger is not None:
            trigger.on_use(
                trigger,
                self.player,
                x,
                y,
            )

    def enter(self, data):
        self.set_render_units()
        self.message_handler.subscribe(MessageID.GET_MAP, self)

    def exit(self):
        self.message_handler.unsubscribe(MessageID.GET_MAP, self)

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
        self.player.controller.handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.on_use_action()

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
