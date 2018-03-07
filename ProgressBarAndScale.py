from tkinter import *
from tkinter import ttk
root = Tk()

progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200)
progressbar.pack()

# if you don't know how many steps are in your operation
progressbar.config(mode = 'indeterminate')
progressbar.start()
progressbar.stop()

# if you know how many steps are in your operation
progressbar.config(mode = 'determinate', maximum = 11.0, value = 4.2)

progressbar.config(value = 8.0)

progressbar.step() # increase vaule by 1

progressbar.step(5) # if progress bar exceeds max, it'll wrap back around

# set progressbar to a variable
value = DoubleVar()
progressbar.config(variable = value)

# create a scale
scale = ttk.Scale(root, orient = HORIZONTAL, length = 400, variable = value, from_ = 0.0, to = 11.0)
scale.pack()
scale.set(4.2)
