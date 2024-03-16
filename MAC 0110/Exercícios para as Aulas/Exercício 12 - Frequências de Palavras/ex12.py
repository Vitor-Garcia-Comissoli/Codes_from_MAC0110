# -*- coding: utf-8 -*-
"""
Created on Tue May 26 08:25:08 2020

@author: vitor
"""
def main():
    nome_arquivo = input("Digite o nome do arquivo: ")
    arq_in = open(nome_arquivo, "r", encoding="utf-8")
    txt = arq_in.read()
    arq_in.close()
    
    print("")
    print(f"Conteudo do arquivo '{nome_arquivo}'")
    print("")
    print(txt)
    
    palavras, frequencia = conte_palavras(txt)
    
    print("")
    for i in range (len(palavras)):
        print (f"{i}: '{palavras[i]}': {frequencia[i]}")
             
def conte_palavras(s):
    
    palavras = []
    frequencia = []
    lst = s.split()
    #print (lst)
    
    for i in range (len(lst)):
        palavra = lst[i]
        if palavra not in palavras:
            palavras += [palavra]
            frequencia += [1]
        elif palavra in palavras:
            k = indice(palavras, palavra)
            frequencia[k] += 1
   
    return palavras, frequencia

def indice(lista, valor):
    
    n = len(lista)
    
    for i in range (n):
        if lista[i] == valor:
            indice = i
    
    return indice

main()