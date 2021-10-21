# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:37:21 2019

@author: psabapathi
"""

from tkinter import *
from tkinter.messagebox import*

def answer():
    showerror("Answer","Sorry, no answer available")

def callback():
    if askyesno('verify','Really quit?'):
        showwarning('Yes','Not yet implemented')
    else:
        showinfo('No','Quit has been cancelled')
        
Button(text='Quit',command=callback).pack(fill=X)
Button(text='Answer',command=answer).pack(fill=X)

mainloop()