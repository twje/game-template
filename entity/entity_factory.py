from .entity import Entity


# temporary data file
entity_defs = {
    "player": {
        "controller": ["move", "wait"],
        "state": "wait"
    },
    "npc": {
        "controller": ["npc_stand", "follow_path", "move"],
        "state": "npc_stand"
    }
}


def create_entity_by_id(entity_id, context, x_pos, y_pos):
    return Entity(entity_defs[entity_id], context, x_pos, y_pos)
