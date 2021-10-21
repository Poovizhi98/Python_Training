# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:04:27 2019

@author: psabapathi
"""

translator={'uno':'one',
            'dos':'two',
            'tres':'three'
            }
word='*'
while word!='':
    word=input('Enter spanish word')
    if word in translator:
        print(translator[word])
    else:
        print('There is no word')