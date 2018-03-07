from tkinter import *
root = Tk()
canvas = Canvas(root)
canvas.pack()
canvas.config(width = 640, height = 480)

# adding a line to a canvas
line = canvas.create_line(160, 360, 480, 120, fill = 'blue', width = 5)
canvas.itemconfigure(line,fill='green')
canvas.coords(line) # returns coordinates
canvas.coords(line, 0, 0, 320, 240, 640, 0) # changes coordinates and adds new segment
canvas.itemconfigure(line, smooth = True) # curves the line
canvas.itemconfigure(line, splinesteps = 5) # curves the line in 5 increments
canvas.itemconfigure(line, splinesteps = 100)
canvas.delete(line)

# adding shapes to a canvas
rect = canvas.create_rectangle(160,120,480,360)
canvas.itemconfigure(rect, fill = 'yellow')
oval = canvas.create_oval(160,120,480,360)
arc = canvas.create_arc(160,1,480,240) # default from 0-90 degrees
canvas.itemconfigure(arc, start = 0, extent = 180, fill = 'green')
# you may use any # of x,y coordinate pairs in a polygon; it will automatically connect the beginning and end pairs
poly = canvas.create_polygon(160,360,320,480,480,360, fill = 'blue')

# adding text to a canvas
text = canvas.create_text(320,240,text='Python',font=('Courier',32,'bold'))

# adding images to a canvas
logo = PhotoImage(file = 'C:\\Users\\User\\Desktop\\pythonLogo.gif')
image = canvas.create_image(320,240,image=logo)

# items added to canvas in order of creation, but can be manipulated with lift and lower
canvas.lift(text)
canvas.lower(image, text)

# add other Tk widgets to canvas
button = Button(canvas, text = 'Click Me')
canvas.create_window(320, 60, window = button)

# using tags with canvas items
canvas.itemconfigure(rect, tag = ('shape'))
canvas.itemconfigure(oval, tag = ('shape','round'))
canvas.itemconfigure('shape', fill = 'grey')
