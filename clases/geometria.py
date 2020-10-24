import numpy as np
from clases.punto import Punto
from clases.vector import Vector
import math as M

def interseccion3D(P, u, Q, v):
    result = []
    perp = cross_product(u,v)

    if (perp.modulo()>0.0001):
        X = Q.x - P.x
        Y = Q.y - P.y
        Z = Q.z - P.z

        w = np.array([X,Y,Z])

        perp = perp.normalize()

        A = np.array([[u.x , -v.x , perp.x],
                    [u.y , -v.y , perp.y],
                    [u.z , -v.z , perp.z]])

        if np.absolute(np.linalg.det(A))<=0.001:
            print('aqui')
            print(u.x * v.y - u.y * v.x)

        mu = np.matmul(np.linalg.inv(A) , w)
        
        A = Punto(P.x + mu[0]*u.x , P.y + mu[0]*u.y , P.z + mu[0]*u.z)
        B = Punto(Q.x + mu[1]*v.x , Q.y + mu[1]*v.y , Q.z + mu[1]*v.z)
        centro = Punto((A.x+B.x)/2 , (A.y+B.y)/2 , (A.z+B.z)/2)


        result.append(centro)
        result.append(mu)

        if mu[2] >= 0.1:
            print("WARNING: ESTAS RECTAS ESTAN DEMASIADO LEJOS DE CORTARSE")
        
        return result

    else:
        result = []
        result.append(Punto())
        result.append(np.array([-1,-1,-1]))
        return result

def interseccion2D(P, u, Q, v):
    if u.x * v.y != u.y * v.x:
        mu_u = 0
        mu_v = 0

        mu_u = ((P.x - Q.x) * v.y + (Q.y-P.y) * v.x) / (u.y*v.x - u.x*v.y)
        
        if v.x != 0:
            mu_v = (P.x - Q.x + mu_u*u.x) / v.x
        else:
            mu_v = (P.y - Q.y + mu_u*u.y) / v.y
        result = []
        
        result.append(Punto(P.x + mu_u*u.x, P.y + mu_u*u.y))
        result.append(np.array([mu_u, mu_v]))
        return result
    
    else:
        result = []
        result.append(Punto())
        result.append(np.array([-1,-1]))
        return result

def rotate(u, theta, v = Vector(0,0,1)):
    v =v.normalize()
    delta = np.radians(theta)
    c = M.cos(delta)
    s = M.sin(delta)
        
    R = [[c + v.x*v.x*(1-c) , v.x*v.y*(1-c) - v.z*s , v.x*v.y*(1-c) + v.y*s],
        [v.y*v.z*(1-c) + v.z*s , c + v.y*v.y*(1-c) , v.y*v.z*(1-c) - v.x*s],
        [v.x*v.z*(1-c) - v.y*s , v.y*v.z*(1-c) + v.x*s , c + v.z*v.z*(1-c)]]

    b = np.array([u.x, u.y, u.z])
    rotated = np.matmul(R,b)
    result = Vector(rotated[0], rotated[1], rotated[2])
    return result

def cross_product(u, v):
        x = u.y * v.z - u.z * v.y
        y = u.z * v.x - u.x * v.z
        z = u.x * v.y - u.y * v.x
        result = Vector(x,y,z)
        return result

def dot_product(u, v):
    return u.x * v.x + u.y * v.y + u.z * v.z