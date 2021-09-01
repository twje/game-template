action_registry = {}


def register_action(name):
    """add resolver class to registry"""
    def add_func(func):

        action_registry[name] = func
        return func

    return add_func


@register_action("teleport")
def teleport(map, teleport_x, teleport_y):
    def action(trigger, entity, tile_x, tile_y):
        entity.x_pos = teleport_x
        entity.y_pos = teleport_y

    return action
