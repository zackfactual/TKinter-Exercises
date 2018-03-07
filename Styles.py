from tkinter import *
from tkinter import ttk
root = Tk()
button1 = ttk.Button(root, text='Button 1')
button2 = ttk.Button(root, text='Button 2')
button1.pack()
button2.pack()

style = ttk.Style()
style.theme_names() # returns list of all available themes on system: ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
style.theme_use() # returns current theme: 'vista'
style.theme_use('clam') # changes current theme to 'clam'
button1.winfo_class() # get default style name of widget

style.configure('TButton',foreground='blue') # change a style
style.configure('Alarm.TButton', foreground='orange',font=('Arial',24,'bold')) # define a new derived style
button2.config(style = 'Alarm.TButton')
style.map('Alarm.TButton',foreground=[('pressed','pink'),('disabled','grey')])
button2.state(['disabled'])

style.layout('TButton') # return list of all elements w/i style
style.element_options('Button.label') # return list of all options available for that element
style.lookup('TButton','foreground') # return current value of property
