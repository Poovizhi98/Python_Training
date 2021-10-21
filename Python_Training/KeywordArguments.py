# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:08:41 2019

@author: psabapathi
"""

def f(**args):
    a=args['a']
    b=args['b']
    c=args['c']
    return 2*a*a +3*b+c
x=f(a=2,b=11,c=3)
print(x)
#x=f(4,11,c)-->It is illegal