# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 10:55:35 2019

@author: psabapathi
"""

MAX=20
n=1
while n<=MAX:
    factor =1
    print(end=str(n)+':')
    while factor <=n:
        if n%factor==0:
            print(factor,end='')
        factor+=1
    print()
    n+=1