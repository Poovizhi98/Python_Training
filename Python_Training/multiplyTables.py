# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 10:36:35 2019

@author: psabapathi
"""

for n in range (1,11):
    for m in range (1,11):
        print('{0:>3}'.format(m*n),end=' ')
    print('\n')