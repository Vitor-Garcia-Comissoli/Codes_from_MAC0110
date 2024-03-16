# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 16:18:58 2020

@author: Vítor Garcia Comissoli
"""

def fatias_nulas(lst):
    
    '''
    (list) -> int 
    RECEBE uma lista `lst`.
    RETORNA o número de fatias nulas de `lst`.
    '''
    
    n = len(lst)
    
    cont_nulos = 0
    
    soma = 0
    
    for j in range(n):
        for i in range(j, n):
            soma += lst[i]
            if soma == 0:
                cont_nulos += 1
        soma = 0
        
    return cont_nulos