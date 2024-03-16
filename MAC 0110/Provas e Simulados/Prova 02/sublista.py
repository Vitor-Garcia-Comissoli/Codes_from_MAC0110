# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 16:29:10 2020

@author: Vítor Garcia Comissoli
"""

def sublista(lstA, lstB):
    
    nb = len(lstB)
    na = len(lstA)
    j = 0
    
    for i in range(nb):
        if lstA[j] == lstB[i]:
            j += 1
            if j == na:
                return True
            
    return False