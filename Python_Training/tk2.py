# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:21:35 2019

@author: psabapathi
"""

import tkinter as tk
root=tk.Tk()

logo=tk.PhotoImage(file="download.gif")

w1=tk.Label(root,image=logo).pack(side="right")

explanation="""Only gif/PPM and Pgm will show."""

w2=tk.Label(root,justify=tk.LEFT,padx=10,text=explanation).pack(side="left")

root.mainloop()