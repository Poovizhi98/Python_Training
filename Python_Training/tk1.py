# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:11:35 2019

@author: psabapathi
"""

import tkinter as tk #no need to install 
root=tk.Tk() #Root window Here Tk is class name
w =tk.Label(root,text="Heloo Tkinter!") #label within root window
w.pack() #It has to pack together not separately
 
root.mainloop()