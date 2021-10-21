# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 13:49:39 2019

@author: psabapathi
"""

def factorial(n):
    fact=1
    for a in range(1,n+1,1):
      fact=fact*a
    return fact

print(factorial(6))