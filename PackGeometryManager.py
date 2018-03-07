from tkinter import *
from tkinter import ttk
root = Tk()

label = ttk.Label(root,text="Hello, world!",background='yellow')
label.pack(side= LEFT, anchor = 'nw') # better to pack separate if you'll be changing the label later in the program

ttk.Label(root,text="Hello, world!",
      background='blue').pack(side= LEFT, padx = 10, pady = 10)
ttk.Label(root,text="Hello, world!",
      background='green').pack(side= LEFT, ipadx = 10, ipady = 10)

for widget in root.pack_slaves():
    widget.pack_configure(fill = BOTH, expand = True)
    print(widget.pack_info())

label.pack_forget()

root.mainloop()
