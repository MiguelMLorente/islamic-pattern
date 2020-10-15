import numpy as np
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

    def add_poligonos(self, L):
        self.poligonos.append(L)
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
                V = np.array([[i*step_h, j*step_v], [(i+1)*step_h, j*step_v], [(i+1)*step_h, (j+1)*step_v], [i*step_h, (j+1)*step_v]])
                self.poligonos.append(Figura(N,V))
                self.n_poligonos = self.n_poligonos + 1

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