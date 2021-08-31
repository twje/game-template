import math


class Camera:
    def __init__(self, pos_x, pos_y, angle, fov):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.fov = fov
        self.angle = angle
        self.dir_x = math.cos(math.radians(angle))
        self.dir_y = math.sin(math.radians(angle))
        self.plane_x = self.dir_y * math.tan(math.radians(self.fov/2))
        self.plane_y = self.dir_x * math.tan(math.radians(self.fov/2))

    def set_fov(self, fov):
        self.fov = fov
        self.set_angle(self.angle)

    def set_position(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def set_angle(self, angle):
        self.angle = angle
        self.dir_x = math.cos(math.radians(angle))
        self.dir_y = math.sin(math.radians(angle))
        self.plane_x = self.dir_y * math.tan(math.radians(self.fov/2))
        self.plane_y = self.dir_x * math.tan(math.radians(self.fov/2))

    def rotate(self, value):
        self.set_angle(self.angle + value)
