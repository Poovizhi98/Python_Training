# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:24:18 2019

@author: psabapathi
"""

from tkinter import *

root=tk.Tk()

S=tk.Scrollbar(root)

T=tk.Text(root,height=4,width=50)
S.pack(side=tk.RIGHT,fill=tk.Y)
T.pack(side=tk.LEFT,fill=tk.Y)

S.config(command=T.yview)
T.config(yscrollcommand=S.set)


quote="""Just a text widget\n in two lines\n"""
T.insert(tk.END,quote)
tk.mainloop()

root=tk.Tk()
T=tk.Text(root,height=2,width=30)
S=tk.Scrollbar(root)
S.pack(side=tk.RIGHT,fill=tk.Y)
T.pack(side=tk.LEFT,fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote="""Just a text widget\n in two linesTraceback (most recent call last):
  File "C:/Users/asj2/Desktop/Training/python/tk23.py", line 3, in <module>
    root=tk.Tk()
NameError: name 'tk' is not defined\n"""
T.insert(tk.END,quote)
tk.mainloop()