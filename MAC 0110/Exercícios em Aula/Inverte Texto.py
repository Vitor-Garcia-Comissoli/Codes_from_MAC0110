# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:55:38 2020

@author: Vítor Garcia Comissoli
"""
def inv(text):

    # text = input("Digite um texto:")

    n = len(text)
    novo = ''
    
    for i in range (n-1, -1, -1): # ou (-1, -n-1, -1)
        print (text[i], end="")
        novo += text[i]
    
    print ("")
    return novo