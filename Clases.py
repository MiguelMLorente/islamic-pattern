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
    
class Segmento:

    def __init__(self, A, B):
        self.inicial = A
        self.final = B
        self.centro = Punto( (A.x + B.x)/2, (A.y + B.y)/2 )
        self.direccion = Punto( B.x - A.x, B.y - A.y )
        self.salientes = []

    def show(self):
        print("Desde: ( x , y ) = (", self.inicial.x, ",", self.inicial.y, ")")
        print("\t Hasta: ( x , y ) = (", self.final.x, self.final.y, ")")
        print("\t Centro: ( x , y ) = (", self.centro.x, ",", self.centro.y, ")")
        print("\t Direccion: v = (", self.direccion.x, ",", self.direccion.y, ")")


class Figura:

    def __init__(self, N, V):
        self.vertices = []
        self.n_vertices = N
        self.lados = []
        for i in range(0,N):
            P = Punto(V[i,0],V[i,1])
            self.vertices.append(P)

        for i in range(0,N):
            if i!=N-1: 
                L = Segmento(self.vertices[i], self.vertices[i+1])
            else:
                L = Segmento(self.vertices[N-1], self.vertices[0])
            self.lados.append(L)


    def show(self):
        for i in range(0,self.n_vertices):
            print("Punto",i, end =  ': ')
            self.vertices[i].show()

        for i in range(0,self.n_vertices):
            print("Segmento",i, end =  ': ')
            self.lados[i].show()


MiCuadrado = Figura(4,np.array([[-1, -1], [1, -1], [1, 1], [-1, 1]]))  
MiCuadrado.show()