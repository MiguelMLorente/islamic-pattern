import numpy as np
from matplotlib import pyplot as plt
from clases.punto import Punto
from clases.segmento import Segmento
from clases.figura import Figura
from clases.mosaico import Mosaico
    


delta = 20
henkins_size = 0.6

# MiCuadrado = Figura(4,np.array([[-1, -1], [1, -1], [1, 1], [-1, 1]]))  
# MiCuadrado.crear_henkins(delta,henkins_size)
# #MiCuadrado.show()
# MiCuadrado.draw_lados()
# MiCuadrado.draw_henkins()
# plt.grid()
# plt.show()

# Mosaico_cuadrado = Mosaico(1)
# # Mosaico_cuadrado.dibujar_mosaico_sin_henkins()
# Mosaico_cuadrado.dibujar_mosaico_con_henkins(delta)
# # Mosaico_cuadrado.dibujar_mosaico_solo_henkins(delta)
# plt.grid()
# plt.show()

# Mosaico_triangular = Mosaico(2)
# # Mosaico_triangular.dibujar_mosaico_sin_henkins()
# Mosaico_triangular.dibujar_mosaico_con_henkins(delta)
# # Mosaico_triangular.dibujar_mosaico_solo_henkins(delta)
# plt.grid()
# plt.show()

Cubo = Mosaico(3)
Cubo.dibujar_mosaico_con_henkins(delta)
plt.grid()
plt.show()