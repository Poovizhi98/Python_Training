# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:47:45 2019

@author: psabapathi
"""

from tkinter import *

master=Tk()

def var_states():
    print("Python:%d,\nPerl:%d" %(var1.get(),var2.get()))
    
Label(master,text="Your Choice:").grid(row=0,sticky=W)
var1=IntVar()
Checkbutton(master,text="Python",variable=var1).grid(row=1,sticky=W)
var2=IntVar()
Checkbutton(master,text="Perl",variable=var2).grid(row=2,sticky=W)
Button(master,text="Quit",command=master.quit).grid(row=3,sticky=W,pady=4)
Button(master,text="Show",command=var_states).grid(row=4,sticky=W,pady=4)

mainloop()