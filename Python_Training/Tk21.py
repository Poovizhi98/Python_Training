# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:42:57 2019

@author: psabapathi
"""

from tkinter import *
from tkinter.colorchooser import askcolor

def callback():
    result=askcolor(color="green",
                    title="Bernd's color chooser")
    print(result)

root=Tk()
Button(root,
       text='Choose color',
       fg='darkgreen',
       command=callback).pack(side=LEFT,padx=10)
Button(
       text='Quit',
       fg='darkgreen',
       command=root.quit).pack(side=LEFT,padx=10)
mainloop()