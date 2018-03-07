from tkinter import *
from tkinter import ttk
root = Tk()
panedwindow = ttk.Panedwindow(root,orient=HORIZONTAL)
panedwindow.pack(fill = BOTH, expand = True)

# panedwindow expands frame to fit size vertically
frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = SUNKEN)
frame2 = ttk.Frame(panedwindow, width = 400, height = 400, relief = SUNKEN)
frame3 = ttk.Frame(panedwindow, width = 50, height = 400, relief = SUNKEN)

# weight specifies how much frame is scaled when panedwindow is resized
panedwindow.add(frame1, weight = 1)
panedwindow.add(frame2, weight = 4)

# if weight isn't specified it'll be 0
panedwindow.insert(1, frame3)

panedwindow.forget(1)
