# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 16:49:48 2020

@author: Vítor Garcia Comissoli
"""

def duzia(s):
    
    s = str(s)
    tamanho = len(s)
    valores = []
    
    # a = 10
    # b = 11
    
    resultado = 0
    j = tamanho - 1
    
    for i in range(tamanho):
        valores += s[i]
        
    # print(tamanho, valores)
    
    for i in range(0, tamanho, 1):
        
        val = (valores[i])
        
        if val == 'a':
            val = 10
            
        elif val == 'b':
            val = 11
        
        else:
            val = int(valores[i])
            
        resultado += val * (12 ** j)
        j -= 1
        
    return resultado