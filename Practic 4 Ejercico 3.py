# -*- coding: utf-8 -*-
"""
Created on Tue May 10 13:56:33 2022

@author: Mateo
"""
horas=8
tarifa=1.66
tasa=0.35
pagabruta=horas*tarifa
impuestos=pagabruta*tasa
paganeta=pagabruta-impuestos

nombre=input("Ingrese el nombre del trabajador: ")
print(f"El emplado {nombre} recibe una paga neta de {paganeta} dolares")



