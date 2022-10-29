import math


class MagnetiсVector:
    x = 0
    y = 0
    length = 0
    angle = 0

    def __init__(self, x, y, len=1, angle=0):
        self.x = x
        self.y = y
        self.length = len
        self.angle = angle

    def draw(self, event):
        endx = self.x + self.length * math.cos(self.angle)
        endy = self.y + self.length * math.sin(self.angle)
        event.widget.create_line(self.x, self.y, endx,
                                 endy, fill="black")
        ug = self.angle + math.pi * 1.25
        ug2 = ug - math.pi / 2
        event.widget.create_line(endx,
                                 endy,
                                 endx + self.length / 3 * math.cos(ug),
                                 endy + self.length * math.sin(ug),
                                 fill="black")
        event.widget.create_line(endx,
                                 endy,
                                 endx + self.length / 3 * math.cos(ug2),
                                 endy + self.length * math.sin(ug2),
                                 fill="black")

    def get_X(self):
        return self.x

    def get_Y(self):
        return self.y

    def get_length(self):
        return self.length

    def set_length(self, len):
        self.length = len

    def get_angle(self):
        return self.angle

    def set_angle(self, ang):
        self.angle = ang
