state_registry = {}


def register_state(identifier):
    def register(clazz):
        state_registry[identifier] = clazz
        return clazz

    return register


from move_state import MoveState