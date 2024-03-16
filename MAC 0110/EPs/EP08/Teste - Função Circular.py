# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:37:33 2020

@author: vitor
"""
def main():
    ''' (list) -> bool 
    Recebe uma lista de "amigo secreto" e retorna True caso exista 
    um único ciclo na lista (a lista seja circular).
    Retorna False caso contrário.
    
    Sempre começa pela pessoa 0 dando o presente para a pessoa de índice [0], e a pessoa de índice [0]
    entrega o presente para a pessoa de índice [1]
    '''
    # modifique o código abaixo para conter a sua solução.
    n = int(input("Digite n: "))
    amigo_de = []
    
    for k in range(0, n, 1):
        N = int(input("Digite um num: "))
        amigo_de += [N]
        
    print(amigo_de)
    print(circular(amigo_de))
    
#--------------------------------------------------------------------------------------------------------------------------------------------------- 
def circular(amigo_de):
    
    ocorrencias = []
    n = len(amigo_de)
    lista = amigo_de
    
    if n == 1:
        return True
    
    if lista[0] == 0:
        return False
    
    i = 0
    while len(ocorrencias) < n:
        if i not in ocorrencias:
            ocorrencias += [i]
            i = lista[i]
        elif i in ocorrencias:
            return False
    
    return True
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
main()