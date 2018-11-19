from Tkinter import *

#setting up your class
class Application(Frame):
    def _init_(self,master):
        #Frame._init_(self,master)
        self.grid()
        self.create_widgets()

    
    def create_widgets(self):
        Label(self,text = "Choose your favourite movie").grid(row=0, column=0, sticky = W)
        Label(self,text = "Select One: ").grid(row=1, column=0, sticky=W)

        #create variable to store favourite movie
        self.favorite=StringVar()

      
        
        #create the button itself
        Radiobutton(self, text="A New Hope", variable=self.favorite, value="Star Wars Episode VI: A New Hope", command = self.update_text).grid(row=2, column=0, sticky=W)

        #create another radio button
        Radiobutton(self, text="The Empire Strikes Back", variable=self.favorite, value="Star Wars Episode V: The Empire Strikes Back", command = self.update_text).grid(row=3, column=0, sticky=W)

        #create yet another radio button
        Radiobutton(self, text="Return of the Jedi", variable=self.favorite, value="Star Ware Episode VI: Return of the Jedi", command = self.update_text).grid(row=4, column=0, sticky=W)


        #create text field to display results
        self.results_txt=Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=5, column=0, columnspan=3)
        

    def update_text(self):
        message = "Your favorite movie is "
        message += self.favorite.get()
        self.results_txt.delete(0.0,END)
        self.results_txt.insert(0.0, message)

#main program
root=Tk()
root.title("Favourite Movie")
app=Application(root)
app._init_(root)
root.mainloop()
        
        
        
