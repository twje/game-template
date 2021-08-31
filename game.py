from map_registry import map_registry
from state_stack import StateStack
from storyboard import Storyboard
from world import World
from scene import Scene
import constants
import storyboard_event_factory as sb_event_factory


class Game(Scene):
    def __init__(self, context):
        super().__init__()        
        self.stack = StateStack()
        self.context = context
        self.renderer = context.renderer
        self.create_world()
        self.start_cutscene()

    def create_world(self):
        map = map_registry[constants.MapID.MAP_1]()
        world = World(self.context, self.stack, map)
        self.stack.push(world)

    def start_cutscene(self):
        cutscene = [
            sb_event_factory.scene(
                self.context,
                "scene_2",
                constants.MapID.MAP_2,
                True
            ),
            sb_event_factory.add_npc(
                None,
                "npc",
                10,
                15
            ),
            sb_event_factory.black_screen(
                "blackscreen",
                self.renderer.screen_width(),
                self.renderer.screen_height(),
                255,
            ),
            sb_event_factory.no_block(
                sb_event_factory.fade_in_screen(
                    "blackscreen",
                    4
                )
            ),
            sb_event_factory.move_npc(
                "scene_2",
                "npc",
                [
                    constants.Direction.LEFT,
                    constants.Direction.LEFT,
                    constants.Direction.TOP,
                    constants.Direction.TOP,
                ]
            ),
            sb_event_factory.hand_off_scene(
                Storyboard.HAND_IN_SCENE
            )
        ]
        storyboard = Storyboard(self.stack, cutscene, True)
        self.stack.push(storyboard)

    def handle_event(self, event):
        self.stack.handle_event(event)

    def update(self, dt):
        self.stack.update(dt)

    def render(self, renderer):
        self.stack.render(renderer)
