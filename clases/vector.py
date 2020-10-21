import numpy as np
import math as M

class Vector:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def show(self):
        print("x =", self.x, ", y =", self.y, ", z =", self.z)

    def invert(self):
        result = Vector(-self.x, -self.y, -self.z)
        return result

    def normalize(self, size=1):
        d = M.sqrt(pow(self.x,2)+pow(self.y,2)+pow(self.z,2))/size
        result = Vector(self.x/d, self.y/d, self.z/d)
        return result

    def modulo(self):
        return M.sqrt(pow(self.x,2)+pow(self.y,2)+pow(self.z,2))
