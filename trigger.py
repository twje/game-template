def null_action(*args, **kwargs):
    pass


class Trigger:
    def __init__(self, **kwargs):
        self.on_enter = kwargs.get("on_enter", null_action)
        self.on_exit = kwargs.get("on_exit", null_action)
        self.on_use = kwargs.get("on_use", null_action)
