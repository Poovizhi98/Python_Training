# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:42:32 2019

@author: psabapathi
"""

from tkinter import *
master=Tk()

canvas_width=80
canvas_height=40

w=Canvas(master,
         width=canvas_width,
         height=canvas_height)
w.pack()
x=int(canvas_height/2)
y=int(canvas_width)

w.create_line(x,0,canvas_width,y,fill="red")
mainloop()