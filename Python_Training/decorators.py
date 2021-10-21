# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:02:16 2019

@author: psabapathi
"""

def say_hello(name):
    return f"hello{name}"

def be_awesome(name):
    return f"Yo {name}"

def follow(something):
    return something("Bob")

follow(say_hello)
follow(be_awesome)