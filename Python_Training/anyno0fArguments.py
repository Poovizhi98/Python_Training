# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 09:47:07 2019

@author: psabapathi
"""

def sum(*nums):
    s=0
    for num in nums:
        s+=num
    return s

print(sum(3,4))
print(sum(3,3,3,3,3,-5))