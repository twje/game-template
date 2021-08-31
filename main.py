from application import Application
from game import Game
import constants


def main():
    app = Application("Storyboard", 800, 640)
    app.add_scene(constants.SceneID.GAME, Game)
    app.set_start_scene(constants.SceneID.GAME)
    app.run()

if __name__ == "__main__":
    main()
