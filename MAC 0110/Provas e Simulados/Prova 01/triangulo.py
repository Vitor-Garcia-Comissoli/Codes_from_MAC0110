# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 16:19:15 2020

@author: Vítor Garcia Comissoli
"""
def main():
    
    números = input('Digite 3 inteiros positivos: ')
    
    # colocar A, B e C tendo A como maior valor, seguido de B e de C
    
    lst_num = números.split()
    
    max_valor = int(lst_num[0])
    min_valor = int(lst_num[0])
    
    for i in range(3):
        lst_num[i] = int(lst_num[i])
        
        if lst_num[i] > max_valor:
            max_valor = lst_num[i]
        elif lst_num[i] < min_valor:
            min_valor = lst_num[i]
        else:
            medio_valor = lst_num[i]
        
    a = max_valor
    b = medio_valor
    c = min_valor
    
    if a >= b >= c and a < b + c:
        print('triângulo')
        
        if a**2 == b**2 + c**2:
            print('retângulo')
            x = lados(a,b,c)
            print(x)
            
        elif a**2 > b**2 + c**2:
            print('obtusângulo')
            x = lados(a,b,c)
            print(x)
            
        else:
            print('acutângulo')
            x = lados(a,b,c)
            print(x)
            
    else:
        print('não triângulo')
        
def lados(a,b,c):
    
    if a == b and a == c:
        str = 'equilátero'
        return str
    
    else:
        if a == b or a == c or b == c:
             str = 'isóceles'
             return str
        else:
             str = 'escaleno'
             return str
         
main()