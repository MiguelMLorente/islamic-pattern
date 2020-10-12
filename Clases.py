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
    
class Segmento:

    def __init__(self, A, B):
        self.inicial = A
        self.final = B
        self.centro = Punto( (A.x + B.x)/2, (A.y + B.y)/2 )
        self.direccion = Punto( B.x - A.x, B.y - A.y )

    def show(self):
        print("Desde: ( x , y ) = (", self.inicial.x, ",", self.inicial.y, ")")
        print("\t Hasta: ( x , y ) = (", self.final.x, self.final.y, ")")
        print("\t Centro: ( x , y ) = (", self.centro.x, ",", self.centro.y, ")")
        print("\t Direccion: v = (", self.direccion.x, ",", self.direccion.y, ")")

    def crear_v_henkins(self,angle):
        #v_henkins es un vector (class Punto)
        self.v_henkins = []
        self.v_henkins.append(self.direccion.rotate(angle))
        self.v_henkins.append(self.direccion.invert().rotate(-angle))

    def draw(self):
        x = np.array([self.inicial.x, self.final.x])
        y = np.array([self.inicial.y, self.final.y])
        plt.plot(x, y)

    def draw_v_henkins(self):
        inicial = np.array([self.centro.x, self.centro.y])
        final_1 = np.array([self.centro.x + self.v_henkins[0].x, self.centro.y + self.v_henkins[0].y])
        final_2 = np.array([self.centro.x + self.v_henkins[1].x, self.centro.y + self.v_henkins[1].y])
        #plt.plot(np.array([inicial.x, final_1[0]]), np.array([inicial.y, final_1[1]]))
        #plt.plot(np.array([inicial.x, final_2[0]]), np.array([inicial.y, final_2[1]]))

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

    def crear_v_henkins(self,angle):
        for i in range(0,self.n_vertices):
            self.lados[i].crear_v_henkins(angle)


    def draw_lados(self):
        for i in range(0,self.n_vertices):
            self.lados[i].draw()

    def draw_v_henkins(self):
        for i in range(0,self.n_vertices):
            self.lados[i].draw_v_henkins()

delta = 60

MiCuadrado = Figura(4,np.array([[-1, -1], [1, -1], [1, 1], [-1, 1]]))  
MiCuadrado.crear_v_henkins(delta)
MiCuadrado.show()
MiCuadrado.draw_lados()
MiCuadrado.draw_v_henkins()
plt.show()