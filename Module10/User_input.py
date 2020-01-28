import tkinter
from tkinter import *
window=tkinter.Tk()
window.title("GUI")
tkinter.Label(window,text="Username").grid(row=0,sticky=W)
tkinter.Entry(window).grid(row=0,column=1)
tkinter.Label(window,text="Password").grid(row=1,sticky=W)
tkinter.Entry(window).grid(row=1,column=1)
tkinter,Checkbutton(window,text="Keep me logged in .").grid(columnspan=2)
window.mainloop()