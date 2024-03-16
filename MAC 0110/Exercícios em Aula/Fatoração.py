# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 08:39:08 2020

@author: vitor

Decomposição em Fatores Primos (Fatoração)
"""

n =int(input("Digite n: "))

fator = 2

while n > 1:
    mult = 0
    while n % fator == 0:
        mult += 1
        n = n // fator
    if mult != 0:
        print ( "fator %d tem multiplicidade %d" %(fator, mult))
    fator += 1