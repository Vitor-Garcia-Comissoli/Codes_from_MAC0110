# -*- coding: utf-8 -*-
"""
Created on Thu May 28 10:24:33 2020

@author: Vítor Garcia Comissoli
"""
CHAVES  = 'chaves'
VALORES = 'valores'
ITENS   = 'itens'
LENGHT  = 'len'
MAX     = 'max'
SAIR    = 'sair'
IN      = 'In [%d]:'
OUT     = 'Out [%d]:'


def main():
    
    dicio_palavras = crie_dicio()
    i = 0
    comando = input(IN%i).strip()
    while comando != SAIR:
        if comando in dicio_palavras:
            chave = comando
            print(OUT%i, dicio_palavras[chave])
            
        elif comando == LENGHT:
            print(OUT%i, len(dicio_palavras))
            
        elif comando == CHAVES:
            print(OUT%i, dicio_palavras.keys())
            
        elif comando == VALORES:
            print(OUT%i, dicio_palavras.values())
            
        elif comando == ITENS:
            print(OUT%i, dicio_palavras.items())
            
        elif comando == MAX:
            print(OUT%i, maior_frequencia(dicio_palavras))
            
        else:
            print(OUT%i, "ERRO")
            
        i += 1
        comando = input(IN%i).strip()
    
def crie_dicio():
    
    dicio = {}
    nome = input('Digite o nome do arquivo: ')
    arquivo = open(nome,'r', encoding = 'utf-8')
    
    for linha in arquivo:
        lst = linha.split(',')
        chave = lst[0]
        chave = chave.strip()
        valor = int(lst[1])
        dicio[chave] = valor
        
    arquivo.close()
    return dicio

def maior_frequencia(dicio):
    max_chave = ''
    max_valor = 0
    
    for chave in dicio:
        valor = dicio[chave]
        if valor > max_valor:
            max_valor = valor
            max_chave = chave
        
    return max_chave

main()