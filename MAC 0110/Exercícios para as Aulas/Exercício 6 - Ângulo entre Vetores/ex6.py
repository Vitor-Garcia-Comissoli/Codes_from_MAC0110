# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:14:43 2020

@author: Vítor Garcia Comissoli
"""
import math

def main():
    '''
    Programa que lÃª dois vetores em 2D e calcula o cosseno do Ã¢ngulo entre eles.
    '''
    # Teste o programa com d = 1, 2, 3, 4, ...
    print("Programa que calcula o cosseno e Ã¢ngulo entre dois vetores")
    # leia um vetor
    v1 = leia_vetor() # sem parÃ¢metro d = 2
    print("v1 =", v1)
    
    # normalize o vetor lido
    normalize(v1)
    print("v1 normalizado=", v1)
    
    # leia outro vetor
    v2 = leia_vetor()
    print("v2 =", v2)
    
    # normalize o vetor lido
    normalize(v2)
    print("v1 normalizado=", v2)
    
    # calcule o cosseno entre os vetores
    cos = produto_escalar(v1, v2)
    print("cosseno entre v1 e v2 = %.2f"%(cos))
    
    # calcule o Ã¢ngulo em radianos entre os vetores
    a_rad = math.acos(cos) # acos(x) Ã© o arco cujo cosseno Ã© x
    print("Ã¢ngulo entre v1 e v2 = %.2f radianos"%(a_rad))
    
    # converta de radianos para graus
    a_graus = (a_rad * 180)/math.pi
    print("Ã¢ngulo entre v1 e v2 = %.2f graus"%(a_graus))

#----------------------------------------------------
def leia_vetor(d=2): # d Ã© 2 se nÃ£o for especificado na chamada
    '''(None) -> list

    LÃª as coordenadas de um vetor de dimensÃ£o d.
    RETORNA uma lista com as coordenadas do vetor.
    '''
    v = [0]*d # v = [0] + [0], v = [0, 0]
    for i in range(0, d, 1):
        c = float(input("Digite a %da-coordenada: "%(i+1)))
        v[i] = c  
    return v

 
#----------------------------------------------------
def normalize(v):  #v = w ATENÃ‡ÃƒO !!!!!!!!!!!! !!!!!!!
    '''(list) -> None
    
    RECEBE uma lista v representando um vetor e transforma v em um
    vetor de norma 1. 

    PrÃ©-condiÃ§Ã£o: a funÃ§Ã£o supÃµe que o vetor nÃ£o tem norma 0.

    In [6]: v = [1, 1]
    In [7]: normalize(v)
    In [8]: v
    Out[8]: [0.7071067811865475, 0.7071067811865475]
    '''
    # dimensÃ£o
    d = len(v)
    
    # calcule a somados quadrados
    soma = 0
    for i in range(d): # range(0, d, 1)
        soma += v[i]*v[i]  # v[i]**2
        
    # calcule a norma=comprimento
    norma = math.sqrt(soma)
    
    # tranforme v para unitÃ¡rio
    for i in range(d):
        v[i] /= norma  # v[i] = v[i] / norma
    
    
#----------------------------------------------------
def produto_escalar(a, b):
    ''' (list, list) -> float

    PrÃ©_condiÃ§Ã£o: a funÃ§Ã£o que a e b tem a mesma dimensÃ£o.

    In [15]: v = [3, 1]
    In [16]: w = [3, 7]
    In [17]: produto_escalar(v,w)
    Out[17]: 16
    '''
    d = len(a)
    soma = 0
    i = 0
    while i < d:
        soma += a[i]*b[i] # soma = soma + a[i]*b[i]
        i += 1 # i = i + 1
    return soma
    ''' equivalentemente: 
    soma = 0
    for i in range(len(a)):
        soma += a[i]*b[i]
    return soma
    '''
#----------------------------------------------------
main()

    