import numpy as np
from matplotlib import pyplot as plt
from clases.punto import Punto
from clases.segmento import Segmento
from clases.figura import Figura

    


delta = 80
henkins_size = 0.6

MiCuadrado = Figura(4,np.array([[-1, -1], [1, -1], [1, 1], [-1, 1]]))  
MiCuadrado.crear_henkins(delta,henkins_size)
#MiCuadrado.show()
MiCuadrado.draw_lados()
MiCuadrado.draw_henkins()
plt.grid()
plt.show()