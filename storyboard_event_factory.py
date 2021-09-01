import storyboard_events as events


def black_screen(scene_id, screen_width, screen_height, alpha):
    def create(storyboard):
        from screen_state import ScreenState
        state = ScreenState(screen_width, screen_height, (0, 0, 0, alpha))
        storyboard.push_state(scene_id, state)
        return events.NullEvent()
    return create


def fade_screen(scene_id, start, finish, duration):
    def create(storyboard):
        from tween import Tween

        state = get_state(storyboard, scene_id)
        return events.TweenEvent(
            Tween(start, finish, duration),
            state,
            lambda target, value: target.set_alpha(value)
        )
    return create


def fade_in_screen(scene_id, duration):
    return fade_screen(scene_id, 255, 0, duration)


def wait(seconds):
    def create(storyboard):
        return events.WaitEvent(seconds)
    return create


def no_block(factory):
    def create(storybaord):
        event = factory(storybaord)
        event.is_blocking = lambda: False
        return event
    return create


def scene(context, scene_id, map_id, hide_player):
    def create(storyboard):
        from world import World
        from map_registry import map_registry

        map = map_registry[map_id]()
        state = World(context, None, map)
        state.hide_player = hide_player
        storyboard.push_state(scene_id, state)
        return events.NullEvent()
    return create


def hand_off_scene(scene_id):
    def create(storyboard):
        yield_control_to_scene(storyboard, scene_id)
        return events.NullEvent()
    return create


def add_npc(scene_id, npc_id, context, pos_x, pos_y):
    def create(storyboard):
        from entity import create_entity_by_id

        npc = create_entity_by_id(npc_id, context, pos_x, pos_y)
        state = get_state(storyboard, scene_id)
        state.map.add_npc(npc_id, npc)
        return events.NullEvent()

    return create


def move_npc(scene_id, npc_id, path):
    def create(storyboard):
        state = get_state(storyboard, scene_id)
        map = state.map
        npc = map.get_npc(npc_id)
        npc.follow_path(path)
        return events.BlockUntilEvent(lambda: npc.is_path_complete())

    return create


# -----------------
# Utility Functions
# -----------------
def get_state(storyboard, scene_id):
    target = storyboard.internal_stack.top()
    if scene_id is not None:
        target = storyboard.states[scene_id]
    return target


def yield_control_to_scene(storyboard, scene_id):
    state = storyboard.states[scene_id]
    storyboard.stack.pop()
    storyboard.stack.push(state)
    state.stack = storyboard.stack
