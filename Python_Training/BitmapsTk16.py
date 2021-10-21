# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:11:50 2019

@author: psabapathi
"""

from tkinter import *

canvas_width=300
canvas_height=80
master=Tk()

canvas=Canvas(master,
         width=canvas_width,
         height=canvas_height)
canvas.pack()

bitmaps=["error","gray75","gray50","gray25","gray12","hourglass"]
nsteps=len(bitmaps)
step_x=int(canvas_width/nsteps)

for i in range(0,nsteps):
    canvas.create_bitmap((i+1)*step_x/2,50,bitmap=bitmaps[i])
    
mainloop()
