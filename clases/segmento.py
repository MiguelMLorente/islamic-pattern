import numpy as np
from matplotlib import pyplot as plt
import math as M
from clases.punto import Punto


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

    def crear_v_henkins(self,angle,size = 1):
        #v_henkins es un vector (class Punto)
        self.v_henkins = []

        self.v_henkins.append(self.direccion.rotate(angle).normalize(size))
        self.v_henkins.append(self.direccion.invert().rotate(-angle).normalize(size))

    def draw(self):
        x = np.array([self.inicial.x, self.final.x])
        y = np.array([self.inicial.y, self.final.y])
        plt.plot(x, y,"xkcd:navy")

    def draw_v_henkins(self):
        x1 = np.array([self.centro.x, self.centro.x + self.v_henkins[0].x])
        y1 = np.array([self.centro.y, self.centro.y + self.v_henkins[0].y])
        x2 = np.array([self.centro.x, self.centro.x + self.v_henkins[1].x])
        y2 = np.array([self.centro.y, self.centro.y + self.v_henkins[1].y])

        plt.plot(x1,y1,"xkcd:goldenrod")
        plt.plot(x2,y2,"xkcd:goldenrod")
        #plt.plot(np.array([inicial.x, final_1[0]]), np.array([inicial.y, final_1[1]]))
        #plt.plot(np.array([inicial.x, final_2[0]]), np.array([inicial.y, final_2[1]]))
