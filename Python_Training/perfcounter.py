# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:12:43 2019

@author: psabapathi
"""
from time import perf_counter

print("Enter your name",end='')
start_time=perf_counter()
name=input()
elapsed=perf_counter()-start_time
print(perf_counter())
print(start_time)
print(name,"it took you",elapsed,"seconds to respond")