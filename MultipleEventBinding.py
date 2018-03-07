from tkinter import *
from tkinter import ttk
root = Tk()

label1 = ttk.Label(root,text='Label 1')
label2 = ttk.Label(root,text='Label 2')
label1.pack()
label2.pack()

label1.bind('<ButtonPress>',lambda e:print('<ButtonPress> Label'))
label1.bind('<1>',lambda e:print('<1> Label'))

# an event bound to a parent widget will run on all the parent's children widgets
root.bind('<1>',lambda e:print('<1> Root'))

# to remove an event binding
label1.unbind('<1>')
label1.unbind('<ButtonPress>')

# to bind to multiple top level windows
root.bind_all('<Escape>', lambda e:print('Escape!'))

root.mainloop()
