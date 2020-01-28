import tkinter
from tkinter import *

top=tkinter.Tk()
checkVar1=IntVar()
checkVar2=IntVar()
tkinter.Checkbutton(top,text="Machine Learning",variable=checkVar1,onvalue=1,offvalue=0).grid(row=0,sticky=W)
tkinter.Checkbutton(top,text="Deep Learning",variable=checkVar2,onvalue=0,offvalue=1).grid(row=1,sticky=W)
top.mainloop()