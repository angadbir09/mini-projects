from Tkinter import *

class Application(Frame):
    def _init_(self,master):
        #Frame._init_(self,master)
        self.grid()
        self.create_widgets()

    #placing a Widget with the Grid Layout Manager
    def create_widgets(self):
        self.inst_lbl=Label(self, text = "Enter password for secret of longevity")
        #specify where you want the label
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)
        #
        self.pw_lbl = Label(self, text = "password: ")
        self.pw_lbl.grid(row=1, column=0, sticky = W)
        #creating an Entry Widget to accept password       
        self.pw_ent=Entry(self)
        #position the Entry Widget
        self.pw_ent.grid(row=1, column=1, sticky = W)

        #create a button that lets user submit password
        self.submit_bttn = Button(self, text = "Submit")
        #place the button on the grid
        self.submit_bttn.grid(row=2,column=0, sticky=W)




root = Tk()
root.title("longevity")
root.geometry("250x150")
app=Application(root)
# explicitlly invoke constructor
app._init_(root)
root.mainloop()
