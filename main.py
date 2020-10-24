import numpy as np
from matplotlib import pyplot as plt
from clases.punto import Punto
from clases.segmento import Segmento
from clases.figura import Figura
from clases.mosaico import Mosaico
    


delta = 50
henkins_size = 0.6

# Mosaico_cuadrado = Mosaico(1)
# # Mosaico_cuadrado.dibujar_mosaico_solo_henkins(delta)
# plt.grid()
# plt.show()

# Mosaico_triangular = Mosaico(2)
# #Mosaico_triangular.dibujar_mosaico_solo_henkins(delta)
# plt.grid()
# plt.show()

# Cubo = Mosaico(3)
# Cubo.dibujar_mosaico_con_henkins(delta)
# plt.grid()
# plt.show()

# Mosaico_octogonos_cuadrados = Mosaico(4)
# Mosaico_octogonos_cuadrados.dibujar_mosaico_solo_henkins(delta)
# plt.grid()
# plt.show()

# Mosaico_hexagonos_cuadrados_triangulos = Mosaico(6)
# Mosaico_hexagonos_cuadrados_triangulos.dibujar_mosaico_solo_henkins(delta)
# plt.grid()
# plt.show()

Mosaico_dodecagonos_triangulos = Mosaico(7)
Mosaico_dodecagonos_triangulos.dibujar_mosaico_solo_henkins(delta)
plt.grid()
plt.show()