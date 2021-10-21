# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:17:02 2019

@author: psabapathi
"""

from tkinter import *

master=Tk()
w=Scale(master,from_=0,to=42)
w.pack()
w=Scale(master,from_=0,to=200,orient=HORIZONTAL)
w.pack()
mainloop()