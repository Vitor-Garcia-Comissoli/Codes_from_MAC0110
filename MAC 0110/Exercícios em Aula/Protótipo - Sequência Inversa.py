# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:18:39 2020

@author: vitor

Sequência Inversa
"""
n = int(input("Digite n: "))
cont = 0
Soma = ""
Sobra = 0

while cont < n:
    a = str(input("Digite um número: "))
    Soma += a
    cont += 1

Soma = int(Soma)

while Soma > 0:
    Sobra = Soma % 10
    Soma = Soma // 10
    print(Sobra)
