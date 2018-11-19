#click counter

from Tkinter import *

# application class definition
class Application (Frame):
    def _init_(self, master):
        #Frame._init_(self, master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()

    #building the event handler
    def create_widget(self):
        self.bttn = Button(self)
        self.bttn["text"]="total clicks: 0"
        self.bttn["command"]=self.update_count
        self.bttn.grid()

    #creating the event handler
    def update_count(self):
        self.bttn_clicks+=1
        self.bttn["text"]="total clicks: "+str(self.bttn_clicks)


#main
root = Tk()
root.title("Click Counter")
root.geometry("200x50")
app = Application(root)
#call the constructor
app._init_(root)

root.mainloop()
