# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 14:21:35 2020

@author: Vítor Garcia Comissoli
"""

def movel (lst):
    
    n = len(lst)
    
    if n == 1:
        return None
    
    else:
        
        lst_media = n * [0]
        
        for i in range (n):
            
            if i == 0:
                lst_media[i] = (lst[i] + lst[i+1])/2
            
            elif i == n-1:
                lst_media[i] = (lst[i-1] + lst[i])/2
            
            else:
                lst_media[i] = (lst[i-1] + lst[i] + lst[i+1])/3
            
        for j in range (n):
            lst[j] = lst_media[j]
            
        return None