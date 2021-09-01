from . import register_state
from state import State


@register_state("npc_stand")
class NPCStand(State):
    def __init__(self, entity, context):
        super().__init__()

    def enter(self, data):
        pass

    def exit(self):
        pass

    def handle_event(self, event):
        pass

    def update(self, dt):
        pass

    def render(self, renderer):
        pass
