# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:13:00 2019

@author: psabapathi
"""

import random
for i in range(10):
    print('Beggining of loop iteration',i)
    try:
        r=random.randint(1,3)
        if r==1:
            print(int('Fred'))  #Type Error
        elif