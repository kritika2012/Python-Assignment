import tkinter
window=tkinter.Tk()

def GuiTutorial():
	tkinter.Label(window,text="Simran").pack()
tkinter.Button(window,text="Click me",command=GuiTutorial).pack()
window.mainloop()