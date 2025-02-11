import math
import time
class Electricity:
    def __init__(self, x, y, clockwise):
        self.x = x
        self.y = y
        self.clockwise = clockwise

    def get_vector_angle(self, vector_x, vector_y):
        x = vector_x - self.x
        y = vector_y - self.y
        angle = math.atan(y / x)
        if x <= 0:
            angle += math.pi
        if self.clockwise:
            angle += math.pi / 2
            return angle
        angle -= math.pi / 2
        return angle

    def get_clockwise(self):
        return self.clockwise

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_vector_length(self, vector_x, vector_y):
        x = self.x-vector_x
        y = self.y-vector_y
        num = x*x + y*y
        len = 1250000/num
        
        if len>625.0 or num<=400.0:
            return 0
        return math.sqrt(len)

