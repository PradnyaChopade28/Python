from tkinter import *
from tkinter import Tk,mainloop,Top
from tkinter.ttk import Button
root=Tk()
root.geometry('200x100')
button=Button(root,text='submit')
button.pack(set=Top,pady=5)
root.mainloop ()