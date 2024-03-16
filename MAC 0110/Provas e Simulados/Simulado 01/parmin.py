# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 18:15:36 2020

@author: vitor
"""


def parmin(lista):
    
    distancia_min = 0
    
    for i in range(0, len(lista)-1):
        a = lista[i]
        
        for j in range(i+1, len(lista)):
            
                b = lista[j] 
        
                distancia = a - b
                
                if distancia < 0:
                    distancia = -distancia
        
                if i == 0 and j == 1:
                    distancia_min = distancia
                    a_min = a
                    b_min = b
        
                elif distancia < distancia_min:
                    distancia_min = distancia
                    a_min = a
                    b_min = b
        
    return a_min, b_min