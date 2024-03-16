# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 10:26:29 2020

@author: vitor
"""

def busque(valor, lista):
    
    n = len(lista)
    i = 0
    indice = None
    
    while i < n and valor >= lista[i]:
        if valor == lista[i]:
            indice = i
            return indice
        else:
            i += 1
    
    return indice
        