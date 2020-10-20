import numpy as np
from matplotlib import pyplot as plt
from clases.punto import Punto
from clases.vector import Vector
from mpl_toolkits.mplot3d import Axes3D
from clases.geometria import rotate
from mpl_toolkits import mplot3d

class Segmento:

    def __init__(self, A, B):
        self.inicial = A
        self.final = B
        self.centro = Punto( (A.x + B.x)/2, (A.y + B.y)/2, (A.z + B.z)/2 )
        self.direccion = Vector( B.x - A.x, B.y - A.y, B.z - A.z )
        self.henkins_final = []
        self.henkins = []

    def show(self):
        print("Desde: ( x , y , z ) = (", self.inicial.x, ",", self.inicial.y, ",", self.inicial.z, ")")
        print("\t Hasta: ( x , y , z ) = (", self.final.x, self.final.y, ",", self.final.z, ")")
        print("\t Centro: ( x , y ,z ) = (", self.centro.x, ",", self.centro.y, ",", self.centro.z, ")")
        print("\t Direccion: v = (", self.direccion.x, ",", self.direccion.y, ",", self.direccion.z, ")")

    def draw(self):
        x = np.array([self.inicial.x, self.final.x])
        y = np.array([self.inicial.y, self.final.y])
        z = np.array([self.inicial.z, self.final.z])
        plt.plot(x, y, "xkcd:navy")

    # def draw_v_henkins(self):
    #     x1 = np.array([self.centro.x, self.centro.x + self.v_henkins[0].x])
    #     y1 = np.array([self.centro.y, self.centro.y + self.v_henkins[0].y])
    #     x2 = np.array([self.centro.x, self.centro.x + self.v_henkins[1].x])
    #     y2 = np.array([self.centro.y, self.centro.y + self.v_henkins[1].y])

    #     plt.plot(x1,y1,"xkcd:goldenrod")
    #     plt.plot(x2,y2,"xkcd:goldenrod")
    #     #plt.plot(np.array([inicial.x, final_1[0]]), np.array([inicial.y, final_1[1]]))
    #     #plt.plot(np.array([inicial.x, final_2[0]]), np.array([inicial.y, final_2[1]]))
