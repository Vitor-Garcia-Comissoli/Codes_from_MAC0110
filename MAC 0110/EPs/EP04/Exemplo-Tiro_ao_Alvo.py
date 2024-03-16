# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x = float(input('Digite x: '))
y = float(input('Digite y: '))

fora = True

if -4 <= x <= 6 and 2 <= y <= 10:
    fora = False
    if 2 < x < 4 and 7 < y < 9:
        fora = True
    elif 1 <= x <= 4 and 3 <= y <= 6:
        fora = True
    elif -2 <= x <= 1 and 3 <= y <= 9:
        fora = True
        if -1 <= x <= 0 and 4 <= y <= 5:
            fora = False

if fora:
    print("Fora")
else:
    print("Dentro")





