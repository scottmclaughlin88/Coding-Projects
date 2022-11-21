

# from classes import Printer3

# test = Printer3('Hello', 2)
# test.showMessage()

from tkinter import *

def change_text():
    label1.configure(text = 'Sad!')

window = Tk()
label1 = Label(window, text = 'Happy')
label1.grid(column = 0, row = 0)
btn1 = Button(window, text = 'Click here', command = change_text)
btn1.grid(column = 0, row = 1)


window.mainloop()