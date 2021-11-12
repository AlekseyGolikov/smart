from tkinter import *

class App(Tk):

    def __init__(self):
        super().__init__()
        self.geometry('200x150')
        self.x = 0
        self.label = Label(self,text=str(self.x))
        self.label2 = Label(self,text='12345676890',justify=LEFT)
        self.label3 = Label(self,text='123',justify=LEFT)

        canvas = Canvas(self)
        canvas.create_line(15,25,100,25, dash=(4, 2))
        canvas.pack(fill=BOTH, expand=1)

        self.label.pack()
        self.label2.pack()
        self.label3.pack()

    def update(self):
        self.after(1000,self.update)
        self.x += 1
        self.label['text'] = self.x
    
app = App()
app.after_idle(app.update)
app.mainloop()