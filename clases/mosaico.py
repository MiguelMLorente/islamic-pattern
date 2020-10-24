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
        if Option == 4:
            self.mosaico_octogonos_cuadrados(5,3,5)
        if Option == 6:
            self.mosaico_hexagonos_cuadrados_triangulos(4,4,5)
        if Option == 7:
            self.mosaico_dodecagonos_triangulos(8,3,3)   


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

    def mosaico_octogonos_cuadrados(self, apotema, filas, columnas):
        self.poligonos.clear()
        self.n_poligonos = 0
        self.__init__
        
        N_cuadrado = 4
        N_octogono = 8

        lado = 2*apotema*(M.sqrt(2)-1)
        diagonal = lado*M.sqrt(2)

        V_octogono = np.array([ [apotema, -lado/2, 0],
                                [apotema, lado/2, 0], 
                                [lado/2, apotema, 0], 
                                [-lado/2, apotema, 0], 
                                [-apotema, lado/2, 0],
                                [-apotema, -lado/2, 0], 
                                [-lado/2, -apotema, 0], 
                                [lado/2, -apotema, 0] ])
        V_cuadrado = np.array([ [diagonal/2 + apotema, apotema, 0],
                                [apotema, diagonal/2 + apotema, 0],
                                [-diagonal/2 + apotema, apotema, 0],
                                [apotema, -diagonal/2 + apotema, 0] ])

        for i in range(0,columnas):
            for j in range(0,filas):
                V_oct = np.outer(np.ones(N_octogono) * 2 * apotema, np.array([i, j, 0])) + V_octogono
                V_cuad = np.outer(np.ones(N_cuadrado) * 2 * apotema, np.array([i, j, 0])) + V_cuadrado

                self.poligonos.append(Figura(N_octogono, V_oct))
                self.poligonos.append(Figura(N_cuadrado, V_cuad))
                self.n_poligonos = self.n_poligonos + 2

    def mosaico_cuadrados_triangulos(self):
        None

    def mosaico_hexagonos_cuadrados_triangulos(self, lado, filas, columnas):

        self.poligonos.clear()
        self.n_poligonos = 0
        self.__init__
        
        N_hexagono = 6
        N_cuadrado = 4
        N_triangulo = 3

        altura = lado * M.sqrt(3)/2

        V_hexagono = np.array([ [lado, 0, 0],
                                [lado/2, altura, 0], 
                                [-lado/2, altura, 0], 
                                [-lado, 0, 0], 
                                [-lado/2, -altura, 0],
                                [lado/2, -altura, 0] ])

        V_cuadrado_1 = np.array([ [lado/2, altura, 0],
                                [lado/2, altura + lado, 0],
                                [-lado/2, altura + lado, 0],
                                [-lado/2, altura, 0] ])

        V_cuadrado_2 = np.array([ [lado, 0, 0],
                                [lado + altura, lado/2, 0],
                                [lado/2 + altura, lado/2 + altura, 0],
                                [lado/2, altura, 0] ])                        

        V_cuadrado_3 = np.array([ [-lado, 0, 0],
                                [-lado/2, altura, 0],
                                [-lado/2 - altura, lado/2 + altura, 0],
                                [-lado - altura, lado/2, 0] ])  

        V_triangulo_1 = np.array([ [lado/2, altura, 0],
                                [lado/2 + altura, lado/2 + altura, 0],
                                [lado/2, lado + altura, 0] ]) 

        V_triangulo_2 = np.array([ [-lado/2, altura, 0],
                                [-lado/2, lado + altura, 0],
                                [-lado/2 - altura, lado/2 + altura, 0] ]) 

        for i in range(0,columnas):
            for j in range(0,filas):
                V_hex_1 = np.outer(np.ones(N_hexagono) , np.array([i*(3*lado + 2*altura), j*(lado + 2*altura), 0])) + V_hexagono
                V_hex_2 = np.outer(np.ones(N_hexagono) , np.array([(i+0.5)*(3*lado + 2*altura), (j+0.5)*(lado + 2*altura), 0])) + V_hexagono

                V_cuad_1_1 = np.outer(np.ones(N_cuadrado) , np.array([i*(3*lado + 2*altura), j*(lado + 2*altura), 0])) + V_cuadrado_1
                V_cuad_1_2 = np.outer(np.ones(N_cuadrado) , np.array([(i+0.5)*(3*lado + 2*altura), (j+0.5)*(lado + 2*altura), 0])) + V_cuadrado_1
                V_cuad_2_1 = np.outer(np.ones(N_cuadrado) , np.array([i*(3*lado + 2*altura), j*(lado + 2*altura), 0])) + V_cuadrado_2
                V_cuad_2_2 = np.outer(np.ones(N_cuadrado) , np.array([(i+0.5)*(3*lado + 2*altura), (j+0.5)*(lado + 2*altura), 0])) + V_cuadrado_2
                V_cuad_3_1 = np.outer(np.ones(N_cuadrado) , np.array([i*(3*lado + 2*altura), j*(lado + 2*altura), 0])) + V_cuadrado_3
                V_cuad_3_2 = np.outer(np.ones(N_cuadrado) , np.array([(i+0.5)*(3*lado + 2*altura), (j+0.5)*(lado + 2*altura), 0])) + V_cuadrado_3
                
                V_tri_1_1 = np.outer(np.ones(N_triangulo) , np.array([i*(3*lado + 2*altura), j*(lado + 2*altura), 0])) + V_triangulo_1
                V_tri_1_2 = np.outer(np.ones(N_triangulo) , np.array([(i+0.5)*(3*lado + 2*altura), (j+0.5)*(lado + 2*altura), 0])) + V_triangulo_1
                V_tri_2_1 = np.outer(np.ones(N_triangulo) , np.array([i*(3*lado + 2*altura), j*(lado + 2*altura), 0])) + V_triangulo_2
                V_tri_2_2 = np.outer(np.ones(N_triangulo) , np.array([(i+0.5)*(3*lado + 2*altura), (j+0.5)*(lado + 2*altura), 0])) + V_triangulo_2

                self.poligonos.append(Figura(N_hexagono, V_hex_1))
                self.poligonos.append(Figura(N_hexagono, V_hex_2))
                self.poligonos.append(Figura(N_cuadrado, V_cuad_1_1))
                self.poligonos.append(Figura(N_cuadrado, V_cuad_1_2))
                self.poligonos.append(Figura(N_cuadrado, V_cuad_2_1))
                self.poligonos.append(Figura(N_cuadrado, V_cuad_2_2))
                self.poligonos.append(Figura(N_cuadrado, V_cuad_3_1))
                self.poligonos.append(Figura(N_cuadrado, V_cuad_3_2))
                self.poligonos.append(Figura(N_triangulo, V_tri_1_1))
                self.poligonos.append(Figura(N_triangulo, V_tri_1_2))
                self.poligonos.append(Figura(N_triangulo, V_tri_2_1))
                self.poligonos.append(Figura(N_triangulo, V_tri_2_2))

                self.n_poligonos = self.n_poligonos + 12

    def mosaico_hexagonos_triangulos(self):
        None

    def mosaico_dodecagonos_hexagonos_cuadrados(self):
        None

    def mosaico_dodecagonos_triangulos(self, radio, filas, columnas):
        self.poligonos.clear()
        self.n_poligonos = 0
        self.__init__
        
        N_dodecagono = 12
        N_triangulo = 3

        lado = 2 * radio * M.sin(np.radians(360/24))
        apotema = radio * M.cos(np.radians(360/24))
        altura = lado * M.sqrt(3)/2
        angle = (np.arange(0,N_dodecagono)+0.5)*M.pi/6

        V_dodecagono = np.zeros((N_dodecagono,3))
        for i in range(0,N_dodecagono):
            V_dodecagono[i,0] = radio*M.sin(angle[i])
            V_dodecagono[i,1] = radio*M.cos(angle[i])
        
        V_triangulo_1 = np.array([ [apotema, -lado/2, 0],
                                [apotema+altura, 0, 0],
                                [apotema, lado/2, 0] ]) 

        V_triangulo_2 = np.array([ [-apotema, -lado/2, 0],
                                [-apotema, lado/2, 0],
                                [-apotema-altura, 0, 0], ]) 

        for i in range(0,columnas):
            for j in range(0,filas):
                V_dod_1 = np.outer(np.ones(N_dodecagono) , np.array([i*(2*apotema+2*altura+lado), j*(2*apotema), 0])) + V_dodecagono
                V_dod_2 = np.outer(np.ones(N_dodecagono) , np.array([(i+0.5)*(2*apotema+2*altura+lado), (j+0.5)*(2*apotema), 0])) + V_dodecagono

                V_tri_1_1 = np.outer(np.ones(N_triangulo) , np.array([i*(2*apotema+2*altura+lado), j*(2*apotema), 0])) + V_triangulo_1
                V_tri_1_2 = np.outer(np.ones(N_triangulo) , np.array([(i+0.5)*(2*apotema+2*altura+lado), (j+0.5)*(2*apotema), 0])) + V_triangulo_1
                V_tri_2_1 = np.outer(np.ones(N_triangulo) , np.array([i*(2*apotema+2*altura+lado), j*(2*apotema), 0])) + V_triangulo_2
                V_tri_2_2 = np.outer(np.ones(N_triangulo) , np.array([(i+0.5)*(2*apotema+2*altura+lado), (j+0.5)*(2*apotema), 0])) + V_triangulo_2

                self.poligonos.append(Figura(N_dodecagono, V_dod_1))
                self.poligonos.append(Figura(N_dodecagono, V_dod_2))
                self.poligonos.append(Figura(N_triangulo, V_tri_1_1))
                self.poligonos.append(Figura(N_triangulo, V_tri_1_2))
                self.poligonos.append(Figura(N_triangulo, V_tri_2_1))
                self.poligonos.append(Figura(N_triangulo, V_tri_2_2))

                self.n_poligonos = self.n_poligonos + 6


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