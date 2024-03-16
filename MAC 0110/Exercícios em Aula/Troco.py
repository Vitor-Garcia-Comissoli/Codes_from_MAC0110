# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 09:14:53 2020

@author: vitor

Troco (dinheiro)
"""
a =int(input("Digite a: "))
b =int(input("Digite b: "))
c =int(input("Digite c: "))

print("")

possível = False

na = 0
while na * a <= c:
    nb = 0
    while nb * b < c - na * a:
        nb += 1
    if na * a + nb * b == c:
        print("%d nota(s) de %d e %d nota(s) de %d" %(na, a, nb, b))
        possível = True
    na += 1
if not possível:
     print("Não é possível fornecer esse valor")