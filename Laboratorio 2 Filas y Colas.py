# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:22:33 2020

@author: Joaco
"""
#""Colas: Fifo""
#Cola de Clientes en un bacno 
print("Clientes en el banco")
Cola= ["Juan", "Maria"]
#Llega nuevo Cliente
Cola.append("Luis")
#Imprimir Turnos
print("Turnos pendientes en cola")
print(Cola.index("Juan"),Cola.index("Maria"),Cola.index("Luis"))
print("Cola")
#Se atiende un cliente
print("Turno numero",Cola.index("Juan"),Cola.index("Maria"),Cola.index("Luis"))
print(Cola[0],"Fue atendido")
Cola.pop(0)
print(Cola)