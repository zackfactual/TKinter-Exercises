from tkinter import *
root = Tk()
text = Text(root,width=40,height=10)
text.pack()

text.config(wrap = 'char')
text.config(wrap = 'none')
text.config(wrap = 'word')

text.get('1.0','end') # get whole text box input
text.get('1.0','1.end') # get first logical line of text box input

text.insert('1.0 + 2 lines', 'C-c-c-combo breaker!') # insert text
text.insert('1.0 + 2 lines lineend', 'and\nmore and\n more') # insert multi-line text

text.delete('1.0') # delete 1st character
text.delete('1.0','1.0 lineend') # delete 1st line
text.delete('1.0','3.0 lineend + 1 chars') # delete 1st line plus line break character

text.replace('1.0', '1.0 lineend', 'This is the first line.')

text.config(state = 'disabled')
text.config(state = 'normal')

# tags
text.tag_add('my_tag','1.0','1.0 wordend')
text.tag_configure('my_tag',background='yellow')
text.tag_remove('my_tag','1.1','1.3')
text.tag_ranges('my_tag')
text.tag_names() # return all tags that exist in widget
text.tag_names('1.0') # return all tags that exist at index
text.replace('my_tag.first','my_tag.last','That')
text.tag_delete('my_tag') # removes tag

# marks
text.mark_names()
text.insert('insert','All aboard the gravy train!') # use mark name as base for an index
text.mark_set('my_mark','end') # set a custom mark, which retains relative location
text.mark_gravity('my_mark',LEFT)
text.mark_unset('my_mark')

# images in a Text widget
image = PhotoImage(file = 'C:\\Users\\User\\Desktop\\pythonLogo.gif')
text.image_create('insert',image = image)

# other widgets in the Text widget
button = Button(text, text = 'Click me')
text.window_create('insert', window = button)
