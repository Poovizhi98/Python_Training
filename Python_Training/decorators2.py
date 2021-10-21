# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:06:31 2019

@author: psabapathi
"""

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

def say_wee():
    print("Whee!")
    
my_decorator(say_wee)
say_wee()