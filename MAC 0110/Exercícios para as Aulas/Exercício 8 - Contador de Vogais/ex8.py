# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:33:38 2020

@author: Vítor Garcia Comissoli
"""
texto = str(input("Digite um texto: "))

n = len(texto)
cont_vogais = 0
cont = 0
vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ã', 'õ', 'A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ã', 'Õ']

for i in range (0,n,1):
    if texto[i] in vogais:
        cont_vogais += 1
    cont += 1
    
Freq = cont_vogais / cont

print("O número de vogais é de:", cont_vogais)
print("Frequência das vogais =", "%d/%d =" %(cont_vogais, cont), Freq)