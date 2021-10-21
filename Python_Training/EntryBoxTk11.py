# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:25:36 2019

@author: psabapathi
"""

import tkinter as tk

#def show():
 #   print("FirstName=%s\n,)
master=tk.Tk()
tk.Label(master,text="First Name").grid(row=0)
tk.Label(master,text="Last Name").grid(row=1)

e1=tk.Entry(master)  #text entry 
e2=tk.Entry(master)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)


master.mainloop()