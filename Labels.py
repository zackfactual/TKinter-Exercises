from tkinter import *
from tkinter import ttk
root = Tk()
label = ttk.Label(root, text = "Hello, World!")
label.pack()
label.config(text = "Howdy, World!")
label.config(text = "Hello, world. How are you doing today? I hope you're well.")
label.config(wraplength = 150)
label.config(justify = CENTER)
label.config(foreground = 'blue', background = 'yellow')
label.config(font = ('Courier', 18, 'bold'))
label.config(text = "Hello, World!")
logo = PhotoImage(file = 'C:\\Users\\User\\Desktop\\pythonLogo.gif')
label.config(image = logo)
label.config(compound = 'text')
label.config(compound = 'center')
label.config(compound = 'left')
label.img = logo # save reference to logo inside image variable
label.config(image = label.img)
