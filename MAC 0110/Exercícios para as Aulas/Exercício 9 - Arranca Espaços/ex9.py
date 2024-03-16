# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:20:28 2020

@author: Vítor Garcia Comissoli
"""
branco = " "

def limpe(t):
    
    n = len(t)
    ini = 0
    
    while ini < n and t[ini] == branco:
        ini += 1
        
    fim = len(t) - 1
    while fim > ini and t[fim] == branco:
        fim -= 1

    T = ""
    
    for i in range(ini, fim+1):
        T += t[i] 
        
    return T
