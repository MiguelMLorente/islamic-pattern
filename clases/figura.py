import numpy as np
from clases.punto import Punto
from clases.segmento import Segmento
from clases.vector import Vector
from clases.geometria import interseccion2D
from clases.geometria import interseccion3D
from clases.geometria import cross_product
from clases.geometria import rotate


class Figura:

    def __init__(self, N, V):
        self.vertices = []
        self.n_vertices = N
        self.lados = []
        self.v_henkins = {}
        self.henkins = []
        self.n_henkins = 0
        for i in range(0,N):
            P = Punto(V[i,0],V[i,1],V[i,2])
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
            #v_henkins['i,j'] donde i es el lado y j es 1 o 2 (direccion escogida)

            self.v_henkins[str(i)+','+str(0)] = rotate(self.lados[i].direccion, angle, self.v_normal).normalize(size)
            self.v_henkins[str(i)+','+str(1)] = rotate(self.lados[i].direccion.invert(), -angle, self.v_normal).normalize(size)
            #v_henkins es un vector

    def intersecar_henkins(self):
        Lista_de_puntos = []
        distancia = []
        for i in range(0, self.n_vertices):
            P = self.lados[i].centro
            for j in range(0,2):
                u = self.v_henkins[str(i)+','+str(j)]
                for k in range(0, self.n_vertices): 
                    if (k==i):
                        continue
                    Q = self.lados[k].centro
                    for l in range(0,2):
                        v = self.v_henkins[str(k)+','+str(l)]
                        dummy = interseccion3D(P, u, Q, v)
                        result = dummy[0]

                        mu_u = dummy[1][0]
                        mu_v = dummy[1][1]
                        if (mu_u >= 0) and (mu_v >= 0):
                            Lista_de_puntos.append(result)
                            distancia.append(mu_u * u.modulo() + mu_v * v.modulo())
                # Seleccionar el mejor de la lista    
                indice  = distancia.index(min(distancia))
                h = Lista_de_puntos[indice]
                self.henkins.append(Segmento(P, h))
                self.n_henkins = self.n_henkins + 1


                Lista_de_puntos.clear()
                distancia.clear()
    
    def crear_henkins(self, angle, size = 0.5):
        self.crear_v_henkins(angle,size)
        self.intersecar_henkins()

    def draw_lados(self):
        for i in range(0,self.n_vertices):
            self.lados[i].draw()

    def draw_henkins(self):
        for i in range(0,self.n_henkins):
            self.henkins[i].draw()       


