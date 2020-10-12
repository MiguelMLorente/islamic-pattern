import numpy as np
from matplotlib import pyplot as plt
import math as M
from punto import Punto
from segmento import Segmento
from figura import Figura

    


delta = 60
henkins_size = 0.6

MiCuadrado = Figura(4,np.array([[-1, -1], [1, -1], [1, 1], [-1, 1]]))  
MiCuadrado.crear_v_henkins(delta,henkins_size)
#MiCuadrado.show()
MiCuadrado.draw_lados()
MiCuadrado.draw_v_henkins()
plt.show()