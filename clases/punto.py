import numpy as np
import math as M

class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("x =", self.x, ", y =", self.y)