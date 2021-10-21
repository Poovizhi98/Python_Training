# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:35:07 2019

@author: psabapathi
"""

import tkinter as tk
root=tk.Tk()
tk.Label(root,text="Red text in Times Font",
         fg="red",
         font="Times").pack()
tk.Label(root,text="Green text in Helvetica Font",
         fg="light green",
         bg="dark green",
         font="Helvetica 16 bold italic").pack()
tk.Label(root,text="Blue text in Verdana bold",
         fg="blue",
         bg="yellow",
         font="verdana 16 bold italic").pack()
root.mainloop()