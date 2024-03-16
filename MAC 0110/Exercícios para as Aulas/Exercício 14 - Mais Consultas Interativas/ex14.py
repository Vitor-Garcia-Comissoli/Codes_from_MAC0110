# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 08:18:37 2020

@author: Vítor Garcia Comissoli
"""

MOSTRE = 'mostre'
SAIR   = 'sair'
LEN    = 'len'
MAX    = 'max'
LIMPE  = 'limpe'
CRIE   = 'crie'
IN     = 'IN [%d]:'
OUT    = 'OUT [%d]:'

def main():
    
    nome = input('Digite o nome do arquivo com pi: ')
    arq = open(nome, 'r', encoding='utf-8')
    pi = arq.read()
    arq.close()
    print(f"arquivo '{nome}' lido.")
    
    pi = pi.strip()
    
    k = int(input('Digite o número de dígitos: '))
    subnumeros = crie_dicionário(pi, k)
    
    i = 1
    comando = input(IN%i)
    while comando != SAIR:
        
        if comando == LEN:
            resp = len(subnumeros)
        elif comando == MOSTRE:
            resp = subnumeros
        elif comando in subnumeros:
            resp = subnumeros[comando]
        elif comando == LIMPE:
            subnumeros = {}
            resp = "Dicionário limpo"
        elif comando == MAX:
            maior, lst_chaves = maior_valor(subnumeros)
            resp = str(maior) + ': ' + str(lst_chaves)
        else:
            resp = 0
        
        print(OUT%i, resp)
        i += 1
        comando = input(IN%i)
        
def maior_valor(dicio):
    maior = 0
    lst_chaves = []
    for chave in dicio:
        valor = dicio[chave]
        if valor > maior:
            maior = valor
            lst_chaves = [chave]
        elif valor == maior:
            lst_chaves += [chave]
    
    return maior, lst_chaves

def crie_dicionário(txt, k):
    
    d = {}
    for i in range(k, len(txt) + 1, 1):
        chave = txt[i-k : i]
        #print(f"examinando chave = '{chave}'")
        #pause()
        
        if chave in d:
            d[chave] += 1
        else:
            d[chave] = 1
        
       #print (f"dicio = {d}")
       #pause()
        
    return d

def pause():
    input('Tecle ENTER para continuar')
    
main()