import numpy as np
import math as M

class Vector:

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
        result = Vector(rotated[0], rotated[1])
        return result

    def invert(self):
        result = Vector(-self.x, -self.y)
        return result

    def normalize(self, size=1):
        d = M.sqrt(pow(self.x,2)+pow(self.y,2))/size
        result = Vector(self.x/d, self.y/d)
        return result

    def modulo(self):
        return M.sqrt(pow(self.x,2)+pow(self.y,2))

    # def cross_prod(self, other)
    #     x = self.y * other.z - self.z * other.y
    #     y = self.z * other.x - self.x * other.z
    #     z = self.x * other.y - self.y * other.x
    #     result = Vector(x,y,z)
    #     return result

    # def dot_product(self,other)
    #     return self.x * other.x + self.y * other.y + self.z * other.z