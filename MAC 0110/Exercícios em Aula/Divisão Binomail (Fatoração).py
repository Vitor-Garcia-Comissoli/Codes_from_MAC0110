# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:16:22 2020

@author: Vítor Garcia Comissoli

Combinação binômial (Fatoração)
"""

"""
Devemos Calcular:
                
               m!
        ----------------
          n! * (m - n)!

"""

"""
m = int(input('Digite m: '))
n = int(input('Digite n: '))

k = m
kfat = 1
i = 2
while i <= k:
    kfat *= i
    i += 1
mfat = kfat

k = n
kfat = 1
i = 2
while i <= k:
    kfat *= i
    i += 1
nfat = kfat

k = m - n
kfat = 1
i = 2
while i <= k:
    kfat *= i
    i += 1
mnfat = kfat

bi = mfat // (nfat*mnfat)
print("Bin (",m,",",n,") =",bi)
"""
# isso tudo pode ser representado usando funções:

def main():
    
    m = int(input('Digite m: '))
    n = int(input('Digite n: '))
    
    mfat= fatorial(m)
    nfat = fatorial (n)
    mnfat = fatorial(m-n)

    bi = mfat // (nfat*mnfat)
    print("binomial (%d,%d) = %d" %(m,n,bi))
    
def fatorial(k):
    kfat = 1
    i = 2
    while i <= k:
        kfat *= i
        i += 1
    return kfat

main()             # Chama a inicialização da função Main

"""
No Phyton Shell:
    
Main() --> para rodar o programa principal

fatorial(k) --> para calcular o fatorial de qualquer número

         exemplos:
                   in: fatorial(5)
                   out: 120
                   
                   in fatorial (3)
                   out: 6
"""
