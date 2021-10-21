# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:55:25 2019

@author: psabapathi
"""

import sys
sum=0
while True:
    x=int(input('Enter a number (999 ends):'))
    if x==999:
        sys.exit(0)
    sum+=x
    print('Sum is ',sum)