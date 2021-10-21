# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:59:41 2019

@author: psabapathi
"""

from tkinter import *

canvas_width=500
canvas_height=150

def paint(event):
    python_green="pink"
    x1,y1=(event.x-10),(event.y-10)
    x2,y2=(event.x+10),(event.y+10)
    w.create_rectangle(x1,y1,x2,y2,fill=python_green)
    
master=Tk()
master.title("Painting")
w=Canvas(master,
         width=canvas_width,
         height=canvas_height)
w.pack(expand=YES,fill=BOTH)
w.bind("<B1-Motion>",paint)

message=Label(master,text="Press and Drag the mouse to draw")
message.pack(side=BOTTOM)
mainloop()

