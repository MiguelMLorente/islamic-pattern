import numpy as np
from clases.punto import Punto
from clases.segmento import Segmento

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

    def crear_v_henkins(self,angle,size=0.5):
        for i in range(0,self.n_vertices):
            self.lados[i].crear_v_henkins(angle,size)


    def draw_lados(self):
        for i in range(0,self.n_vertices):
            self.lados[i].draw()

    def draw_v_henkins(self):
        for i in range(0,self.n_vertices):
            self.lados[i].draw_v_henkins()
