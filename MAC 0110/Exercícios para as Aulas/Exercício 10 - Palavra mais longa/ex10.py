# -*- coding: utf-8 -*-
"""
Created on Tue May 19 08:23:01 2020

@author: vitor
"""

Maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Minusculas = "abcdefghijklmnopqrstuvwxyz"
Vogais = "áâãéêíóõôúûÁÂÃÉÊÍÓÕÔÚÛ"
Letras = Maiusculas + Minusculas + Vogais


def main():
    
    txt = input("Digite um texto: ")
    
    """
    # nome do arquivo
    nome = input("Digite o nome do arquivo: ")
    # abra o arquivo
    arquivo = open(nome, "r", encoding="utf-8")
    # leia o texto
    txt = arquivo.read()
    # feche o arquivo
    arquivo.close()
    # print (txt)
    """
    p = maior_palavra(txt)
    print(f"Maior palavra é {p} e seu comprimento é {len(p)}")
    
def maior_palavra(s):
    
    len_maior = 0
    maior = ""
    
    len_p = 0
    palavra = ""
    
    n = len(s)
    for i in range(0, n, 1):
        c = s[i]
    
    # for c in s:    
        if c.isalpha(): # in Letras:
            len_p += 1
            palavra = palavra + c
            
        else:
            len_p = 0
            palavra = ""
            
        if len_p > len_maior:
            len_maior = len_p
            maior = palavra
    
    return maior

def letra(c):
    
    # return c in Letras
    
    for letra in Letras:
        
        if c == letra:
            return True
        
    return False

main()