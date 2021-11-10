from tkinter import *
import tkinter.ttk as ttk

class App(Tk):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.title = 'Мониторинг умного дома'
        self.geometry('300x250')
        self.tab_control = ttk.Notebook()
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1,text='Настройки')
        self.lbl01 = Label(self.tab1,text='Count = ')
        self.lbl01.grid(column=0, row=0)
        self.lbl01 = Label(self.tab1,text='')
        self.lbl01.grid(column=1, row=0)

        self.tab_control.add(self.tab2,text='Входы')
        lbl3 = Label(self.tab2,text='Вкладка Входы')
        lbl3.grid(column=0, row=0)

        self.tab_control.add(self.tab3,text='Выходы')
        lbl4 = Label(self.tab3,text='Вкладка Выходы')
        lbl4.grid(column=0, row=0)

        self.tab_control.pack(expand=1,fill='both')

    def update(self):
        self.after(1000,self.update)
        self.count += 1
        self.lbl01['text'] = str(self.count)
        
        

def main():
    app = App()
    app.after_idle(app.update)
    app.mainloop()

if __name__ == '__main__':
    main()
