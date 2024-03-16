# -*- coding: utf-8 -*-
"""
Created on Tue May 26 08:18:09 2020

@author: Vítor Garcia Comissoli
"""
txt = input("Digite um texto csv:")
texto = txt.split()
n = len(texto)

for i in range (0, n , 1):
    a = texto[i].strip()
    print (a)