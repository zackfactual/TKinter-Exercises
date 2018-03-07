from tkinter import *
from tkinter import ttk
root = Tk()
notebook = ttk.Notebook(root)
notebook.pack()
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1,text = 'One')
notebook.add(frame2,text = 'Two')
ttk.Button(frame1, text = "Click Me").pack()
frame3 = ttk.Frame(notebook)
notebook.insert(1,frame3,text = "Three")
notebook.forget(1)
notebook.add(frame3,text="Three")
notebook.select()
notebook.index(notebook.select()) #convert result of notebook select method into tab #
notebook.select(2) # select 3rd index tab
notebook.tab(1,state='disabled')
notebook.tab(1,state='hidden')
notebook.tab(1,state='normal')
notebook.tab(1,'text') # check state of text property of tab at index 1
notebook.tab(1) # check state of all properties of tab at index 1
