# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:29:15 2019

@author: psabapathi
"""

import tkinter as tk
root=tk.Tk()

v=tk.IntVar()
v.set(1)  #Initializing the choice,as 1 that is Python

languages=[
        ("Python",1),
        ("Perl",2),
        ("Java",3),
        ("C++",4),
        ("C",5),
        ]

def ShowChoice():
    print(v.get())
    
tk.Label(root,
         text="""Choose your favourite programming language:""",
         justify=tk.LEFT,
         padx=20).pack()

for val,language in enumerate(languages):
    tk.Radiobutton(root,
                   text=language,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)
root.mainloop()

    