class WindowRendererStratgey:
    def __init__(self):
        self.pixels_per_unit = None
        self.x_tiles = None
        self.y_tiles = None
        self.screen_width = None
        self.screen_height = None

    def reset(self, x_tiles, y_tiles, screen_width, screen_height):
        self.x_tiles = x_tiles
        self.y_tiles = y_tiles
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pixels_per_unit = min(
            int(screen_width/x_tiles),
            int(screen_height/y_tiles)
        )

    def world_cords_to_screen_cords(self, x_pos, y_pos, width, height):
        x_pos = self.x_offset + x_pos * self.pixels_per_unit
        y_pos = self.y_offset + y_pos * self.pixels_per_unit
        width = width * self.pixels_per_unit
        height = height * self.pixels_per_unit

        return x_pos, y_pos, width, height

    @property
    def x_offset(self):
        ofsset = self.screen_width
        ofsset = ofsset - self.x_tiles * self.pixels_per_unit
        ofsset = ofsset/2
        return ofsset

    @property
    def y_offset(self):
        ofsset = self.screen_height
        ofsset = ofsset - self.y_tiles * self.pixels_per_unit
        ofsset = ofsset/2
        return ofsset
