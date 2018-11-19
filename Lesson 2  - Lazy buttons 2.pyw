#previous program rewritten using a class. restructured.


# import Tkinter Module
from Tkinter import *



# Defining the Application Class
class Application(Frame):
    def _init_(self,master):
        #Frame._init_(self,master)
        self.grid()
        self.create_widgets()

    #defining a method to create the widgets
    def create_widgets(self):
        #creates button
        self.bttn1=Button(self, text = "I do nothing!")
        #insert button to grid
        self.bttn1.grid()

        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text="Me Too!")

        self.bttn3=Button(self)
        self.bttn3.grid()
        self.bttn3["text"]="Same here!"



#main
root = Tk()
root.title("lazy buttons 2")
root.geometry("200x85")


app=Application(root)
app._init_(root)

root.mainloop()









