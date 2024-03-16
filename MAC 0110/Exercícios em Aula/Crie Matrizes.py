# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:51:39 2020

@author: Vítor Garcia Comissoli
"""

def main():
    
    nlin = int (input('Digite nlin: '))
    ncol = int (input('Digite ncol: '))
    val = int (input('Digite val: '))

    matriz = crie_matriz(nlin, ncol, val)
    
    print('A matriz é :', matriz)

def crie_matriz(nlin, ncol, val=0):
    
    matriz = []
    
    for i in range(nlin):
        linha = [val] * ncol
        matriz += [linha]
    
    return matriz

main()