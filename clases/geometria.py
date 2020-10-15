import numpy as np
from clases.punto import Punto
from clases.vector import Vector



def interseccion(P, u, Q, v):
    if u.x * v.y != u.y * v.x:
        mu_u = ((P.x - Q.x) * v.y + (Q.y-P.y) * v.x) / (u.y*v.x - u.x*v.y)
        mu_v = 0
        if v.x != 0:
            mu_v = (P.x - Q.x + mu_u*u.x) / v.x
        else:
            mu_v = (P.y - Q.y + mu_u*u.y) / v.y
            
        result = Punto(P.x + mu_u*u.x, P.y + mu_u*u.y)
        return result, mu_u, mu_v