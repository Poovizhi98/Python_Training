# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:14:16 2019

@author: psabapathi
"""

def sum_range(n,m=4):
    sum=0
    for val in range(n,m+1):
        sum+=val
    print(sum)

#sum_range(2)
sum_range(2)
#def sum_range(n=0,m) It is not valid