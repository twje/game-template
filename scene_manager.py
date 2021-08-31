class SceneManager:
    def __init__(self, context):
        self.context = context
        self.scenes = {}
        self.scene = None

    def add_scene(self, sceneId, scene):
        self.scenes[sceneId] = scene

    def set_scene(self, sceneId):
        self.scene = self.scenes[sceneId](self.context)

    def handle_event(self, event):
        self.scene.handle_event(event)

    def update(self, dt):
        self.scene.update(dt)

    def render(self):
        self.scene.render(self.context.renderer)
