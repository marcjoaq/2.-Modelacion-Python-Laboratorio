# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:58:30 2020

@author: Joaco
"""
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
