from tkinter import *
root = Tk()
window = Toplevel(root) # default size of new window is 200x200

window.title('New Window')
window.lower()
window.lift(root)

window.state('zoomed') # expand to max allowed size
window.state('withdrawn') # hide even from taskbar
window.state('iconic') # minimize but keep in task bar
window.state('normal') # return to zoomed
window.state() # check state
window.state('normal') # return to normal
window.iconify()
window.deiconify()

window.geometry('640x480+50+100')
window.resizable(False,False)
window.maxsize(640,480)
window.minsize(200,200)
window.resizable(True,True) # default


root.destroy()
