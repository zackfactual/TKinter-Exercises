from tkinter import messagebox
messagebox.showinfo(title='A Friendly Message',message='Hello, World!')

# store response as a bool
messagebox.askyesno(title="Hungry?",message="Do you want SPAM?") 

from tkinter import filedialog

# store filepath in filename variable
filename = filedialog.askopenfile()
filename.name

from tkinter import colorchooser
colorchooser.askcolor(initialcolor='#FFFFFF') # returns a list of 2 items: a list of the RGB values, and the hex value
