import importlib
import os

state_registry = {}
__all__ = [state_registry]


def register_state(identifier):
    def register(clazz):
        state_registry[identifier] = clazz
        return clazz

    return register


def load_modules():
    for filename in os.listdir(os.path.dirname(__file__)):
        if filename == '__init__.py' or filename[-3:] != '.py':
            continue

        # import module
        module = importlib.import_module(f".{filename[:-3]}", package=__name__)
        names = getattr(module, '__all__', [n for n in dir(module)
                                            if not n.startswith('_')])

        for name in names:
            globals()[name] = getattr(module, name)

            __all__.append(name)


load_modules()
