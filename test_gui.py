from tkinter import *
from weather_project import get_days_above_temperatures,get_days_below_temperatures
from plagariasm_checker import get_longest_matching_words

def get_days_above():
    label2.config(text=get_days_above_temperatures(entry1.get()))

def get_days_below():
    min_result.config(text=get_days_below_temperatures(min_entry.get()))

def get_matching_words():
    plagiarism_result.config(text=get_longest_matching_words(file1_entry.get(),file2_entry.get()))


window = Tk()
window.geometry('800x400')
window.title('Data Analysis')
# frame = Frame(window)
# frame.pack()

#Adding objects
label1 = Label(window,text='Days above temp',font=('Arial',30))
label1.pack()
label2 = Label(window,text='',font=('Arial',30))
label2.pack()

#Add input box
entry1 = Entry(window)
entry1.pack()

#Create a button
button1 = Button(window,text='Get max',command=get_days_above)
button1.pack()

min_label1 = Label(window,text='Days below',font=('Arial',30))
min_label1.pack()
min_result = Label(window,text='',font=('Arial',30))
min_result.pack()

#Add input box
min_entry = Entry(window)
min_entry.pack()

#Create a button
get_min = Button(window,text='Get min',command=get_days_below)
get_min.pack()

file1_label = Label(window,text='File 1',font=('Arial',30))
file1_label.pack()
file1_entry = Entry(window)
file1_entry.pack()
file2_label = Label(window,text='File 2',font=('Arial',30))
file2_label.pack()

#Add input box
file2_entry = Entry(window)
file2_entry.pack()

#Create a button
find_pl = Button(window,text='Get plagiarism',command=get_matching_words)
find_pl.pack()

plagiarism_result = Label(window,text='',font=('Arial',30))
plagiarism_result.pack()

window.mainloop()