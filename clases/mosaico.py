import numpy as np
import math as M
from clases.punto import Punto
from clases.segmento import Segmento
from clases.vector import Vector
from clases.figura import Figura


class Mosaico:

    def __init__(self, Option = 0):
        self.poligonos = []
        self.n_poligonos = 0
         
        if Option == 1:
            self.mosaico_cuadrado(10,10,5,5)
        if Option == 2:
            self.mosaico_triangular(2,5,3)
        if Option == 3:
            self.cubo(5)

    def add_poligonos(self, L):
        self.poligonos.extend(L)
        self.n_poligonos = self.n_poligonos + len(L)

    def mosaico_cuadrado(self, longitud, altura, n_horizontal, n_vertical):
        self.poligonos.clear()
        self.n_poligonos = 0
        self.__init__
        
        N = 4
        step_h = longitud/n_horizontal
        step_v = altura/n_vertical
        for i in range(0,n_horizontal):
            for j in range(0,n_vertical):
                V = np.array([[i*step_h, j*step_v, 0], [(i+1)*step_h, j*step_v, 0], [(i+1)*step_h, (j+1)*step_v, 0], [i*step_h, (j+1)*step_v, 0]])
                self.poligonos.append(Figura(N,V))
                self.n_poligonos = self.n_poligonos + 1

    def mosaico_triangular(self, lado, n_horizontal, n_vertical):
        self.poligonos.clear()
        self.n_poligonos = 0
        self.__init__
        
        N = 3
        step_h = lado
        step_v = lado*M.sqrt(3)
        for i in range(0, n_horizontal):
            for j in range(0, n_vertical):
                V = np.array([[i*step_h, j*step_v, 0], [(i+1)*step_h, j*step_v, 0], [(i+0.5)*step_h, (j+0.5)*step_v, 0]])
                self.poligonos.append(Figura(N,V))
                V = np.array([[i*step_h, j*step_v, 0], [(i+0.5)*step_h, (j+0.5)*step_v, 0], [(i-0.5)*step_h, (j+0.5)*step_v, 0]])
                self.poligonos.append(Figura(N,V))
                V = np.array([[(i+0.5)*step_h, (j+0.5)*step_v, 0], [(i+1)*step_h, (j+1)*step_v, 0], [i*step_h, (j+1)*step_v, 0]])
                self.poligonos.append(Figura(N,V))
                V = np.array([[(i-0.5)*step_h, (j+0.5)*step_v, 0], [(i+0.5)*step_h, (j+0.5)*step_v, 0], [i*step_h, (j+1)*step_v, 0]])
                self.poligonos.append(Figura(N,V))
                self.n_poligonos = self.n_poligonos + 4

    def cubo(self, lado):
        self.poligonos.clear()
        self.n_poligonos = 0
        self.__init__
        L = []
        L.append(Figura(4,np.array([ [0,0,0] , [0,lado,0] , [lado,lado,0] , [lado,0,0] ])))
        L.append(Figura(4,np.array([ [0,0,lado] , [lado,0,lado] , [lado,lado,lado] , [0,lado,lado] ])))
        L.append(Figura(4,np.array([ [lado,0,0] , [lado,lado,0] , [lado,lado,lado] , [lado,0,lado] ])))
        L.append(Figura(4,np.array([ [0,0,0] , [0,0,lado] , [0,lado,lado] , [0,lado,0] ])))
        L.append(Figura(4,np.array([ [0,0,0] , [lado,0,0] , [lado,0,lado] , [0,0,lado] ])))
        L.append(Figura(4,np.array([ [lado,lado,0] , [0,lado,0] , [0,lado,lado] , [lado,lado,lado] ])))

        self.add_poligonos(L)

    def dibujar_mosaico_sin_henkins(self):
        for i in range(0,self.n_poligonos):
            self.poligonos[i].draw_lados()

    def dibujar_mosaico_con_henkins(self,angle):
        for i in range(0,self.n_poligonos):
            self.poligonos[i].crear_henkins(angle)
            self.poligonos[i].draw_lados()
            self.poligonos[i].draw_henkins()

    def dibujar_mosaico_solo_henkins(self,angle):
        for i in range(0,self.n_poligonos):
            self.poligonos[i].crear_henkins(angle)
            self.poligonos[i].draw_henkins()