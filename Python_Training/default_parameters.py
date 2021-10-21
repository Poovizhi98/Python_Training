# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:19:14 2019

@author: psabapathi
"""

def sum_parameters(a,b=1,c=1,d=1,e=1):
    sum=0
    for n in range(a,e+1):
      sum+=n
    print(sum)
sum_parameters(9)