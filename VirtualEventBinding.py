from tkinter import *
from tkinter import ttk
root = Tk()

entry = ttk.Entry(root)
entry.pack()

# native virtual events
entry.bind('<<Copy>>',lambda e:print('Copy'))
entry.bind('<<Paste>>',lambda e:print('Paste'))

# custom virtual events
entry.event_add('<<OddNumber>>','1','3','5','7','9')
entry.bind('<<OddNumber>>',lambda e:print('Odd Number'))

print(entry.event_info('<<OddNumber>>')) # returns ('1','3','5','7','9')

# programatically trigger virtual events
entry.event_generate('<<OddNumber>>')
entry.event_generate('<<Paste>>')
entry.event_generate('<<Copy>>')

# delete virtual events
entry.event_delete('<<OddNumber>>')

root.mainloop()
