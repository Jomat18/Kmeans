#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy
import pylab
import math
import random

colors = ['green','red','yellow','black','cyan','magenta']

def crear_datos(n, k):
    coordenadas = numpy.zeros(shape=(n, 2))
    centros = numpy.zeros(shape=(k, 2))
    coordenadas2 = numpy.zeros(shape=(n+k, 2))
    color = numpy.empty(shape=[n+k, 1],dtype=object)

    for i in range(n):
        coordenadas[i][0]=random.random()
        coordenadas[i][1]=random.random()
        coordenadas2[i][0]=coordenadas[i][0]
        coordenadas2[i][1]=coordenadas[i][1]
        color[i][0]='blue'
    
    for i in range(k):
        centros[i][0]=random.choice(coordenadas[:,0])
        centros[i][1]=random.choice(coordenadas[:,1])
        coordenadas2[n+i][0]=centros[i][0]
        coordenadas2[n+i][1]=centros[i][1]
        color[n+i][0]=colors[i]
    
    grafico(coordenadas2, color)    
        
    return coordenadas, centros, color


def agregar(coordenadas, centros):
    m, n = coordenadas.shape
    k, n = centros.shape
    coordenadas2 = numpy.zeros(shape=(m+k, n))
    
    for i in range(m):
        coordenadas2[i][0]=coordenadas[i][0]
        coordenadas2[i][1]=coordenadas[i][1]

    for i in range(k):
        coordenadas2[m+i][0]=centros[i][0]
        coordenadas2[m+i][1]=centros[i][1]

    return coordenadas2


def distancia(coordenadas, centros, color):

    m, n = coordenadas.shape
    k, n = centros.shape
    #colores = empty(shape=[m+k, 1],dtype=object)
    minimo = 1000000000000
    media = numpy.zeros(shape=(k, n+1))

    for i in range(m):
        for j in range(k):
            dist = math.sqrt(math.pow(coordenadas[i][0] - centros[j][0],2)+math.pow(coordenadas[i][1] - centros[j][1],2))
            if dist<minimo:
                minimo=dist
                pos=j
        minimo = 1000000000000            
        color[i]=color[m+pos]        
        media[pos][0]=media[pos][0]+coordenadas[i][0]
        media[pos][1]=media[pos][1]+coordenadas[i][1]
        media[pos][2]=media[pos][2]+1
       
    for i in range(k):
        if media[i][2]!= 0:
            centros[i][0] = media[i][0]/media[i][2]
            centros[i][1] = media[i][1]/media[i][2]
        
    return centros, color


def grafico(coordenadas, colores):    
    pylab.scatter(coordenadas[:, 0], coordenadas[:, 1], marker='o', c=colores[:,0])  
    pylab.title('Kmeans')
    pylab.xlabel('X')
    pylab.ylabel('Y')
    pylab.show()  


def kmeans():

    print ("Ingrese #datos")
    n = int(input())
    print ("Ingrese #clusters entre 1-6")
    k = int(input())
    dist = 1
    coordenadas, centros, color = crear_datos(n, k)
    n=0
    while dist>0.2:
        n = n+1 
        new_centros, colores = distancia(coordenadas, centros, color)
        dist=0
        for i in range(k):
            dist = dist + math.sqrt(math.pow(centros[i][0] - new_centros[i][0],2)+math.pow(centros[i][1] - new_centros[i][1],2))   
        coordenadas2 = agregar(coordenadas,new_centros)
        centros = new_centros
        grafico(coordenadas2, colores)

if __name__ == '__main__':
    kmeans()


