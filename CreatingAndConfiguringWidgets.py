from tkinter import *
from tkinter import ttk
root = Tk()
button = ttk.Button(root, text = 'Click me')
button.pack()
button['text'] # 'Click me'
button['text'] = 'Press Me'
button.config(text = 'Push Me')
button.config() # shows all properties available for a widget
ttk.Label(root, text = "Hello, world!").pack()
