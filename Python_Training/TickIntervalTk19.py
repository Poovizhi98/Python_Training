# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:19:51 2019

@author: psabapathi
"""

from tkinter import *


def show_values():
    print(w1.get(),w2.get())
    
master=Tk()
w1=Scale(master,from_=0,to=42,tickinterval=8)
w1.set(19)
w1.pack()
w2=Scale(master,from_=0,to=200,tickinterval=10,orient=HORIZONTAL)
w2.set(23)
w2.pack()
Button(master,text='Show',command=show_values).pack()
mainloop()