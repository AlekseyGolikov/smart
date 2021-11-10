from tkinter import *

class App(Tk):

    def __init__(self):
        super().__init__()
        self.geometry('200x150')
        self.x = 0
        self.label = Label(self,text=str(self.x))
        self.label.pack()

    def update(self):
        self.after(1000,self.update)
        self.x += 1
        self.label['text'] = self.x
    
app = App()
app.after_idle(app.update)
app.mainloop()