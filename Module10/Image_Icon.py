import tkinter
window=tkinter.Tk()
window.title("GUI")
a="D:\\Python assignment\\Module 10\\my.png"
icon=tkinter.PhotoImage(file=a)
label=tkinter.Label(window,image=icon)
label.pack()
label1=tkinter.Label(window,image=icon)
label1.pack()
label2=tkinter.Label(window,image=icon)
label2.pack()
window.mainloop()