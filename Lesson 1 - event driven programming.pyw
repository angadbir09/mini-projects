from Tkinter import *
root = Tk()
root.title("simple GUI")
root.geometry("200x200")
app = Frame(root)
app.grid()
lable=Label(app, text="I'm a label!")
lable.grid()
button = Button(app)
button["text"]="This does nothing"
button.grid()
root.mainloop()




