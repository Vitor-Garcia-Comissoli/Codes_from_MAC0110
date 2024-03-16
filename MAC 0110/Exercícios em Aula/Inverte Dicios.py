# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:35:22 2020

@author: vitor
"""
def main():
    len_dicio = int(input('Digite o tamanho de um Dicionário: '))
    
    dicio = {}
    
    for i in range(0, len_dicio, 1):
        chave = input('Digite a %da Chave: ' %(i+1))
        valor = input('Digite o valor da %da Chave: ' %(i+1))
        dicio[chave] = valor
      
    inv_dicio = inverta(dicio)
    
    print('')
    print('O inverso do Dicionário é: ',inv_dicio)

def inverta(dicio):
    
    inv = {}
    
    for i in dicio.keys(): # Percorre as chaves do Dicionário
        inv[dicio[i]] = i
    
    return inv

main()