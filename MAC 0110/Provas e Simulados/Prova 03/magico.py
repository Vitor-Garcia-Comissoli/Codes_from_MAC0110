# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 14:21:33 2020

@author: Vítor Garcia Comissoli
"""

def magico (matriz):
    
    nlin = len(matriz)
    ncol = len(matriz[0])
    
    cont = nlin #já que nlin é sempre == ncol
    
    while cont > 0:
        
        i = nlin - cont
        j = ncol - cont
        
        soma_lin = 0
        soma_col = 0
        
        for x in range (nlin):
            
            soma_lin += matriz[x][j]
            
            soma_col += matriz[i][x]
        
        if soma_lin == soma_col:
            cont -= 1
        
        else:
            return False
    
    return True