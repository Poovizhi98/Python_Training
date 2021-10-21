# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:49:41 2019

@author: psabapathi
"""

import tkinter as tk 
from tkinter import filedialog,Button,mainloop,X

def fn():
    name=filedialog.askopenfilename()
    print(name)
    
errmsg='Error!'
Button(text='File open',command=fn).pack(fill=X)
mainloop()