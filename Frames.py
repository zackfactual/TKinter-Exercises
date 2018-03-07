from tkinter import *
from tkinter import ttk
root = Tk()
frame = ttk.Frame(root, height = 100, width = 200)
frame.pack()
frame.config(relief = RIDGE)
ttk.Button(frame, text = 'Click Me').grid()
frame.config(padding = (30, 15))
ttk.LabelFrame(root, height = 100, width = 200, text = "My LabelFrame").pack()
