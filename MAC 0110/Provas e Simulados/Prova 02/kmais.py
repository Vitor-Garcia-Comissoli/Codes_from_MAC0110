# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 16:29:13 2020

@author: Vítor Garcia Comissoli
"""

def kmais(seq, k):
    
    n = len(seq)
    
    dicio = {}
    
    for i in range(n):
        num = seq[i]
        if num in dicio:
            dicio[num] += 1
            
        else:
            dicio[num] = 1
        
        if dicio[num] == k:
                return num
            
    return None