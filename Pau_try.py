import numpy as np
from matplotlib import pyplot as plt
import math as M
#def setup


#class Punto:
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
    
#class Figura:
#    vertices = np.array(0)
#    def __init__(self, N, vertices):
#        for i in range(0,N):
#            self.vertices[i] = Punto(vertices[i,0], vertices[i,1])

#MiCuadrado = Figura(4,np.array([[-1, -1], [1, -1], [1, 1], [-1, 1]]))  
        
#figura.vertices.x = np.array([-1, 1, 1, -1])
#figura.vertices.y = np.array([-1, -1, 1, 1])

#pl.plot(figura.vertices.x,figura.vertices.y)














vertices = np.array([[-1, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]])
centros = np.zeros((5,2))
plt.plot(vertices[:,0],vertices[:,1])


for i in range(0,4):
    centros[i,:] = (vertices[i,:] + vertices[i+1,:])/2
    #print(centros[i,:])


delta = np.radians(60)
Rotacion_izq = [[M.cos(delta), -M.sin(delta)], [M.sin(delta), M.cos(delta)]]
Rotacion_der = [[M.cos(delta), M.sin(delta)], [-M.sin(delta), M.cos(delta)]]

vector_inicial = np.zeros((4,2))
vector_rotado_izq = np.zeros((4,2))
vector_rotado_der = np.zeros((4,2))


for i in range(0,4):
    vector_inicial = centros[i,:] - vertices[i,:]
    vector_rotado_izq[i,:] = np.matmul(Rotacion_izq,vector_inicial)
    vector_rotado_der[i,:] = np.matmul(Rotacion_der,-vector_inicial)
    print(centros[i,:])

    plt.plot(np.array([centros[i,0], centros[i,0] + vector_rotado_izq[i,0]]) ,
    np.array([centros[i,1], centros[i,1] + vector_rotado_izq[i,1]]))

    plt.plot(np.array([centros[i,0], centros[i,0] + vector_rotado_der[i,0]]) ,
    np.array([centros[i,1], centros[i,1] + vector_rotado_der[i,1]]))

    #plt.quiver([centros[i,:]], vector_rotado_izq[i,0], vector_rotado_izq[i,1])
    #plt.quiver([centros[i,:]], vector_rotado_der[i,0], vector_rotado_der[i,1])

plt.scatter(centros[0:-1,0],centros[0:-1,1])
plt.grid()
plt.show()