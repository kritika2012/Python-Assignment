import tkinter.messagebox
window=tkinter.Tk()
window.title("GUI")

tkinter.messagebox.showinfo("Alert Message","This just a alert message")
response=tkinter.messagebox.askquestion("Tricky Question","Do you love Deep Learning")

if response=='yes':
	tkinter.Label(window,text="Yes, offcourse").pack()
else:
	tkinter.Label(window,text="NO, i hate it").pack()
window.mainloop()