import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np
from matplotlib import pyplot as plt
from clases.punto import Punto
from clases.segmento import Segmento
from clases.figura import Figura
from clases.mosaico import Mosaico
    


vertices = [
    (1,-1,-1),
    (1,1,-1),
    (-1,1,-1),
    (-1,-1,-1),
    (1,-1,1),
    (1,1,1),
    (-1,-1,1),
    (-1,1,1),
    ]
lados = [
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    ]
superficies = [
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6),
    ]
colores = [
    # Colores en RGB, 0 es minimo 1 máximo
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,1,0),
    (1,0,1),
    (0,1,1),
    (1,1,1),
    (0,0,0),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,1,0),
    ]

delta = 50

def ConstructorCuboHenkins(delta):
    cuboHenkins = Mosaico(3)
    cuboHenkins.crear_henkins(delta)
    verticesCuboHenkins = []
    henkinsCuboHenkins = []

    for poligons in cuboHenkins.poligonos:
        for edges in poligons.lados:
            vertexToAppend =[edges.inicial.x,
                            edges.inicial.y,
                            edges.inicial.z]
            verticesCuboHenkins.append(vertexToAppend)
            vertexToAppend = [edges.final.x,
                            edges.final.y,
                            edges.final.z]
            verticesCuboHenkins.append(vertexToAppend)

    for poligons in cuboHenkins.poligonos:
        for henkins in poligons.henkins:
            vertexToAppend =[henkins.inicial.x,
                            henkins.inicial.y,
                            henkins.inicial.z]
            henkinsCuboHenkins.append(vertexToAppend)
            vertexToAppend =[henkins.final.x,
                            henkins.final.y,
                            henkins.final.z]
            henkinsCuboHenkins.append(vertexToAppend)
    return verticesCuboHenkins,henkinsCuboHenkins


def printVertices():
    for poligons in cuboHenkins.poligonos:
        for edges in poligons.lados:
            print(
                str(edges.inicial.x) + ', ' + str(edges.final.x) +',' +
                str(edges.inicial.y) + ', ' + str(edges.final.y) +',' +
                str(edges.inicial.z) + ', ' + str(edges.final.z) )

def Cube():
    glBegin(GL_QUADS)
    # glColor3fv((0,1,0))
    
    for surface in superficies:
        x = 0
        
        for vertex in surface:
            glColor3fv(colores[x])
            glVertex3fv(vertices[vertex])
            x+=1
    glEnd()

def CubeWireframe():
    glBegin(GL_LINES)
    for edge in lados:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()


def MosaicCubo(verticesCuboHenkins,henkinsCuboHenkins):
    glBegin(GL_LINES)
    for vertex in verticesCuboHenkins:
        glVertex3fv(vertex)
    for henkins in henkinsCuboHenkins:
        glVertex3fv(henkins)
    glEnd()
    



def main():
    

   
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    #               FOV     AspectRatio     ClippingRange
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0,-5)

    glRotatef(0, 0, 0, 0)

    step = 0.1
    x_move = 0
    y_move = 0
    x_rotate = 0
    y_rotate = 0
    z_rotate = 0

    delta = 40
    deltaFlag = 0
    verticesCuboHenkins,henkinsCuboHenkins = ConstructorCuboHenkins(delta)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    # glTranslatef(-step,0,0)
                    x_move = -step
                if event.key == pygame.K_d:
                    # glTranslatef(step,0,0)
                    x_move = step
                if event.key == pygame.K_w:
                    # glTranslatef(0,step,0)
                    y_move = step
                if event.key == pygame.K_s:
                    # glTranslatef(0,-step,0)
                    y_move = -step
                if event.key == pygame.K_j:
                    x_rotate = step
                if event.key == pygame.K_l:
                    x_rotate = -step
                if event.key == pygame.K_i:
                    y_rotate = step
                if event.key == pygame.K_k:
                    y_rotate = -step
                if event.key == pygame.K_u:
                    z_rotate = step
                if event.key == pygame.K_o:
                    z_rotate = -step
                if event.key == pygame.K_q:
                    deltaFlag = step
                if event.key == pygame.K_e:
                    deltaFlag = -step
                
            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        x_move = 0
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        y_move = 0
                    if event.key == pygame.K_q or event.key == pygame.K_e:
                        deltaFlag = 0
                    if event.key == pygame.K_j or event.key == pygame.K_l:
                        x_rotate = 0
                    if event.key == pygame.K_i or event.key == pygame.K_k:
                        y_rotate = 0
                    if event.key == pygame.K_u or event.key == pygame.K_o:
                        z_rotate = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,step)
                if event.button ==5:
                    glTranslatef(0,0,-step)   
        if x_move != 0:
            glTranslatef(x_move,0,0)
        if y_move != 0:
            glTranslatef(0,y_move,0)
        if x_rotate != 0 or y_rotate != 0 or z_rotate != 0:
            glRotate(1,x_rotate,y_rotate,z_rotate)
        if deltaFlag != 0:
            delta += deltaFlag * 10
            if delta > 0 and delta < 90:
                verticesCuboHenkins,henkinsCuboHenkins = ConstructorCuboHenkins(delta)

        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        MosaicCubo(verticesCuboHenkins,henkinsCuboHenkins)
        
        pygame.display.flip()
        pygame.time.wait(10)




main()