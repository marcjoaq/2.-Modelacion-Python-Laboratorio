# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:40:52 2020

@author: Joaco
"""
#Laboratorio 2 Ejercicio 2 Con Librerias
from collections import deque
#Cola de un CarWash 
cola= deque (["Tesla", "Honda", "Toyota" ])
print("carros en espera de carwash")
print("Turno 1: " ,cola[0])
print("Turno 2: " ,cola[1])
print("Turno 3: " ,cola[2])
cola.append("Ford")
print("Nuevo turno 4: ", cola[3])
cola.popleft()

#Trabajar el for, Recursividad con el for y funciones que nos permitan agregar y quitar 
#indices de clientes que lleguen a esa cola. 

from collections import deque

cola= deque (["Tesla", "Honda", "Toyota" ])
print("Carros en espera")

#Cola en Ford 

def VistadeCola(cola):
    i=0
    for carros in cola:
        print("Turno", i+1, cola[i])
        i=i+1

VistadeCola(cola)