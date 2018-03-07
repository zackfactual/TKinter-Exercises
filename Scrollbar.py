from tkinter import *
from tkinter import ttk
root = Tk()

'''
text = Text(root,width=40,height=10,wrap='word')
text.grid(row=0,column=0)

# yview tells the text widget how far the scroll bar has been moved, so the text widget can change the view accordingly
scrollbar = ttk.Scrollbar(root,orient=VERTICAL,command=text.yview)
scrollbar.grid(row=0,column=1,sticky='ns')
# set tells the scrollbar where to place the top and bottom of the scroll pad as a % of its position in the text area
text.config(yscrollcommand = scrollbar.set)
'''

canvas = Canvas(root,scrollregion=(0,0,640,480),bg='white')
xscroll = ttk.Scrollbar(root,orient=HORIZONTAL,command=canvas.xview)
yscroll = ttk.Scrollbar(root,orient=VERTICAL,command=canvas.yview)
canvas.config(xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

canvas.grid(row=1,column=0)
xscroll.grid(row=2,column=0,sticky='ew')
yscroll.grid(row=1,column=1,sticky='ns')

def canvas_click(event):
    x = canvas.canvasx(event.x) # adding canvas.canvasx() tells bind method that canvas has been scrolled
    y = canvas.canvasy(event.y)
    canvas.create_oval((x-5,y-5,x+5,y+5),fill='green')

canvas.bind('<1>',canvas_click)

root.mainloop()
