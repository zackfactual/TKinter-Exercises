from tkinter import *
from tkinter import ttk
root = Tk()
month = StringVar()
combobox = ttk.Combobox(root,textvariable = month)
combobox.pack()
combobox.config(values = ('January','February','March','April','May','June','July','August','September','October','November','December'))

year = StringVar()
Spinbox(root, from_ = 1990, to = 2014, textvariable = year).pack()
