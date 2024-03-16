# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:06:28 2020

@author: vitor
"""

n = int(input("Digite o valor de n: "))

pit = False

if n % 12 == 0:
    a = 3
    b = 4
    c = 5
    
elif n % 30 == 0:
    a = 5
    b = 12
    c = 13
    
elif n % 56 == 0:
    a = 7
    b = 24
    c = 25
    
elif n % 40 == 0:
    a = 8
    b = 15
    c = 17
    
elif n % 90 == 0:
    a = 9
    b = 40
    c = 41
    
elif n % 132 == 0:
    a = 11
    b = 60
    c = 61
    
elif n % 84 == 0:
    a = 12
    b = 35
    c = 37
    
elif n % 182 == 0:
    a = 13
    b = 84
    c = 85
    
elif n % 144 == 0:
    a = 16
    b = 63
    c = 65
    
elif n % 70 == 0:
    a = 20
    b = 21
    c = 29
    
elif n % 126 == 0:
    a = 28
    b = 45
    c = 53
    
elif n % 154 == 0:
    a = 33
    b = 56
    c = 65
    
elif n % 198 == 0:
    a = 36
    b = 77
    c = 85
    
elif n % 208 == 0:
    a = 39
    b = 80
    c = 89
    
elif n % 176 == 0:
    a = 48
    b = 55
    c = 73
    
elif n % 234 == 0:
    a = 65
    b = 72
    c = 97
    
else:
    a = n+1
    b = n+1
    c = n+1  
      
if pit:
    print("%d é a soma do trio (%d, %d, %d)" % (n, n, n, n))
else:
    print("%d não é soma de trio Pitagoreano" % (n))