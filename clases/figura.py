import numpy as np
from clases.punto import Punto
from clases.segmento import Segmento
from clases.vector import Vector
from clases.geometria import interseccion2D
from clases.geometria import interseccion3D
from clases.geometria import cross_product


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

        self.v_normal = cross_product(self.lados[0].direccion, self.lados[1].direccion).normalize()

    def show(self):
        for i in range(0,self.n_vertices):
            print("Punto",i, end =  ': ')
            self.vertices[i].show()

        for i in range(0,self.n_vertices):
            print("Segmento",i, end =  ': ')
            self.lados[i].show()

    def crear_v_henkins(self,angle,size):
        for i in range(0,self.n_vertices):
            self.lados[i].crear_v_henkins(angle,size)

    def intersecar_henkins(self):
        Lista_de_puntos = []
        distancia = []
        for i in range(0, self.n_vertices):
            P = self.lados[i].centro
            for j in range(0,2):
                u = self.lados[i].v_henkins[j]
                for k in range(0, self.n_vertices): 
                    if (k==i):
                        continue
                    Q = self.lados[k].centro
                    for l in range(0,2):
                        v = self.lados[k].v_henkins[l]
                        dummy = casi_interseccion(P, u, Q, v)
                        result = dummy[0]

                        mu_u = dummy[1][0]
                        mu_v = dummy[1][1]
                        if (mu_u >= 0) and (mu_v >= 0):
                            Lista_de_puntos.append(result)
                            distancia.append(mu_u * u.modulo() + mu_v * v.modulo())
                # Seleccionar el mejor de la lista    
                indice  = distancia.index(min(distancia))
                self.lados[i].henkins_final.append(Lista_de_puntos[indice])
                
                Lista_de_puntos.clear()
                distancia.clear()
    
    def crear_seg_henkins(self):
        for i in range(0, self.n_vertices):
            for j in range(0,2):
                self.lados[i].henkins.append(Segmento(self.lados[i].centro, self.lados[i].henkins_final[j]))

    def crear_henkins(self, angle, size = 0.5):
        self.crear_v_henkins(angle,size)
        self.intersecar_henkins()
        self.crear_seg_henkins()

    def draw_lados(self):
        for i in range(0,self.n_vertices):
            self.lados[i].draw()

    def draw_henkins(self):
        for i in range(0,self.n_vertices):
            for j in range(0,2):
                self.lados[i].henkins[j].draw()       


