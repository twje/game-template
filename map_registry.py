map_registry = {}


def register_map(identifier):
    def register(clazz):
        map_registry[identifier] = clazz
        return clazz

    return register

import map