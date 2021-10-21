# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:50:05 2019

@author: psabapathi
"""

from tkinter import *

master=Tk()

w=Canvas(master,width=200,height=100)
w.pack()

w.create_rectangle(50,20,150,80,fill="green")
w.create_rectangle(60,10,135,56,fill="blue")
w.create_rectangle(100,15,175,100,fill="red")
w.create_line(0,0,50,20,fill="pink",width=3)
w.create_line(0,100,50,80,fill="orange",width=3)
w.create_line(150,20,200,0,fill="yellow",width=3)
w.create_line(150,80,200,100,fill="brown",width=3)

mainloop()