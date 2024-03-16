# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 08:18:46 2020

@author: vitor

Programa que Imprima Tabuadas
"""

n =int(input("Digite n: "))
m =int(input("Digite m: "))

print('')

i = 1
while i <= n:
    print("Tabuada do", i)
    j=1
    while j <= m:
        print(i, "X", j, "=", i*j)     # print ("%d X %d = %d" %(i,j,i*j))
        j += 1
    i += 1
    print ('')