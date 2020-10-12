import numpy as np
from matplotlib import pyplot as plt
import math as M

class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("x =", self.x, ", y =", self.y)

    def rotate(self, theta):
        delta = np.radians(theta)
        A = [[M.cos(delta), -M.sin(delta)], [M.sin(delta), M.cos(delta)]]
        v = np.array([self.x, self.y])
        rotated = np.matmul(A,v)
        result = Punto(rotated[0], rotated[1])
        return result

    def invert(self):
        result = Punto(-self.x, -self.y)
        return result

    def normalize(self, size=1):
        d = M.sqrt(pow(self.x,2)+pow(self.y,2))/size
        result = Punto(self.x/d, self.y/d)
        return result
