import numpy as np
import math as M

class Punto:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def show(self):
        print("x =", self.x, ", y =", self.y, ", z =", self.z)