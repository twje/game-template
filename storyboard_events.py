class NullEvent:
    def update(self, dt):
        pass

    def is_blocking(self):
        return False

    def is_finished(self):
        return True

    def render(self, renderer):
        pass


class WaitEvent:
    def __init__(self, seconds):
        self.seconds = seconds

    def update(self, dt):
        self.seconds = self.seconds - dt

    def is_blocking(self):
        return True

    def is_finished(self):
        return self.seconds <= 0

    def render(self, renderer):
        pass


class BlockUntilEvent:
    def __init__(self, until_func):
        self.until_func = until_func

    def update(self, dt):
        pass

    def is_blocking(self):
        return not self.until_func()

    def is_finished(self):
        return not self.is_blocking()

    def render(self, renderer):
        pass


class TweenEvent:
    def __init__(self, tween, target, apply_func):
        self.tween = tween
        self.target = target
        self.apply_func = apply_func

    def update(self, dt):        
        self.tween.update(dt)
        self.apply_func(self.target, self.tween.value)

    def is_blocking(self):
        return True

    def is_finished(self):
        return self.tween.is_finished

    def render(self, renderer):
        pass
