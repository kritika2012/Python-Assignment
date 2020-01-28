import tkinter
window=tkinter.Tk()
window.title("GUI")
top_frame=tkinter.Frame(window).pack()
bottom_frame=tkinter.Frame(window).pack(side="bottom")

btn1=tkinter.Button(top_frame,text="Button1",fg="red").pack()
btn2=tkinter.Button(top_frame,text="Button2",fg="green").pack()
btn3=tkinter.Button(bottom_frame,text="Button3",fg="blue").pack(side="bottom")
btn4=tkinter.Button(bottom_frame,text="Button4",fg="orange").pack(side="bottom")
window.mainloop()