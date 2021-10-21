# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:02:58 2019

@author: psabapathi
"""
import tkinter as tk
master=tk.Tk()
message="Time is precious.Don't waste it"
msg=tk.Message(master,text=message)
msg.config(bg='lightgreen',font=('times',24,'italic'))
msg.pack()
tk.mainloop()