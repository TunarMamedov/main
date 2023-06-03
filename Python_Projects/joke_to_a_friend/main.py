from tkinter import *
from tkinter import messagebox
import random

def yes():
    messagebox.showinfo('YOU IDIOT', 'I KNEW:)')
    quit()

def motionMouse(event):
    btnn.place(x=random.randint(0, 500), y=random.randint(0, 500))

root = Tk()
root.geometry('600x600')
root.title('Question')
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = Label(root, text='ARE U STUPID?', font='Arial 20 bold', bg='black').pack()
btnn = Button(root, text='NO', font='arial 20 bold')
btnn.place(x=170, y=100)
btnn.bind('<Enter>', motionMouse)
btny = Button(root, text='YES', font='Arial 20 bold', command=yes).place(x=350, y=100)

root.mainloop()

