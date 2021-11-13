from tkinter import *
import tkinter.ttk as ttk

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.constants import Defaults
Defaults.RetryOnEmpty = True
Defaults.Timeout = 5
Defaults.Retries = 5

manage = { 0: 'мест', 1:'дист'}
status = { 0: 'false', 1: 'true'}
values = []

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title = 'Мониторинг умного дома'
        self.geometry('300x620')
        self.tab_control = ttk.Notebook()
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.ERROR = ''

        self.lbl00 = Label(self.tab1,text='Связь с А1 отсутствует', fg='red')
        self.lbl00.grid(column=0, row=0, sticky='w')
        self.lbl01 = Label(self.tab1,text='Связь с А2 отсутствует', fg='red')
        self.lbl01.grid(column=0, row=1, sticky='w')
        self.lbl10 = Label(self.tab2,text='Связь с А1 отсутствует', fg='red')
        self.lbl10.grid(column=0, row=0, sticky='w')
        self.lbl11 = Label(self.tab2,text='Связь с А2 отсутствует', fg='red')
        self.lbl11.grid(column=0, row=1, sticky='w')
        self.lbl20 = Label(self.tab3,text='Связь с А1 отсутствует', fg='red')
        self.lbl20.grid(column=0, row=0, sticky='w')
        self.lbl21 = Label(self.tab3,text='Связь с А2 отсутствует', fg='red')
        self.lbl21.grid(column=0, row=1, sticky='w')

        self.tab_control.add(self.tab1,text='Настройки')

        self.lbl12 = Label(self.tab1,text='Управление А1 = ')
        self.lbl12.grid(column=0, row=2, sticky='w')
        self.lbl13 = Label(self.tab1,text='мест')
        self.lbl13.grid(column=1, row=2)

        self.lbl14 = Label(self.tab1,text='Управление А2 = ')
        self.lbl14.grid(column=0, row=3, sticky='w')
        self.lbl15 = Label(self.tab1,text='мест')
        self.lbl15.grid(column=1, row=3)

        self.combobox1 = ttk.Combobox(self.tab1,values = ['COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9'])
        self.combobox1.grid(column=0,row=4)
        self.combobox1.current(2)

        self.tab_control.add(self.tab2,text='Входы')

        self.lbl002 = Label(self.tab2,text='T жидкости контура безопасности = ')
        self.lbl002.grid(column=0, row=2, sticky='w')
        self.lbl003 = Label(self.tab2,text='нет датчика')
        self.lbl003.grid(column=1, row=2)

        self.lbl004 = Label(self.tab2,text='T обратная теплого пола = ')
        self.lbl004.grid(column=0, row=3, sticky='w')
        self.lbl005 = Label(self.tab2,text='нет датчика')
        self.lbl005.grid(column=1, row=3)

        self.lbl006 = Label(self.tab2,text='T воздуха в котельной = ')
        self.lbl006.grid(column=0, row=4, sticky='w')
        self.lbl007 = Label(self.tab2,text='нет датчика')
        self.lbl007.grid(column=1, row=4)

        self.lbl008 = Label(self.tab2,text='T воздуха в задней = ')
        self.lbl008.grid(column=0, row=5, sticky='w')
        self.lbl009 = Label(self.tab2,text='нет датчика')
        self.lbl009.grid(column=1, row=5)

        self.lbl010 = Label(self.tab2,text='T воздуха в передней = ')
        self.lbl010.grid(column=0, row=6, sticky='w')
        self.lbl011 = Label(self.tab2,text='нет датчика')
        self.lbl011.grid(column=1, row=6)

        self.lbl012 = Label(self.tab2,text='T воздуха в мансарде = ')
        self.lbl012.grid(column=0, row=7, sticky='w')
        self.lbl013 = Label(self.tab2,text='нет датчика')
        self.lbl013.grid(column=1, row=7)

        self.lbl014 = Label(self.tab2,text='T наружная = ')
        self.lbl014.grid(column=0, row=8, sticky='w')
        self.lbl015 = Label(self.tab2,text='нет датчика')
        self.lbl015.grid(column=1, row=8)

        self.lbl016 = Label(self.tab2,text='T в печи = ')
        self.lbl016.grid(column=0, row=9, sticky='w')
        self.lbl017 = Label(self.tab2,text='нет датчика')
        self.lbl017.grid(column=1, row=9)

        self.lbl018 = Label(self.tab2,text='Т в туалете = ')
        self.lbl018.grid(column=0, row=10, sticky='w')
        self.lbl019 = Label(self.tab2,text='нет датчика')
        self.lbl019.grid(column=1, row=10)

        self.lbl020 = Label(self.tab2,text='Пож сигнализация = ')
        self.lbl020.grid(column=0, row=11, sticky='w')
        self.lbl021 = Label(self.tab2,text='нет датчика')
        self.lbl021.grid(column=1, row=11)

        self.lbl022 = Label(self.tab2,text='Газоанализатор = ')
        self.lbl022.grid(column=0, row=12, sticky='w')
        self.lbl023 = Label(self.tab2,text='нет датчика')
        self.lbl023.grid(column=1, row=12)

        self.lbl024 = Label(self.tab2,text='Уровень 1 = ')
        self.lbl024.grid(column=0, row=13, sticky='w')
        self.lbl025 = Label(self.tab2,text='нет датчика')
        self.lbl025.grid(column=1, row=13)

        self.lbl026 = Label(self.tab2,text='Уровень 2 = ')
        self.lbl026.grid(column=0, row=14, sticky='w')
        self.lbl027 = Label(self.tab2,text='нет датчика')
        self.lbl027.grid(column=1, row=14)

        self.lbl028 = Label(self.tab2,text='Уровень 3 = ')
        self.lbl028.grid(column=0, row=15, sticky='w')
        self.lbl029 = Label(self.tab2,text='нет датчика')
        self.lbl029.grid(column=1, row=15)

        self.lbl030 = Label(self.tab2,text='Уровень 4 = ')
        self.lbl030.grid(column=0, row=16, sticky='w')
        self.lbl031 = Label(self.tab2,text='нет датчика')
        self.lbl031.grid(column=1, row=16)

        self.lbl032 = Label(self.tab2,text='Состояния реле 1 А1 = ')
        self.lbl032.grid(column=0, row=17, sticky='w')
        self.lbl033 = Label(self.tab2,text='нет датчика')
        self.lbl033.grid(column=1, row=17)

        self.lbl034 = Label(self.tab2,text='Состояния реле 2 А1 = ')
        self.lbl034.grid(column=0, row=18, sticky='w')
        self.lbl035 = Label(self.tab2,text='нет датчика')
        self.lbl035.grid(column=1, row=18)

        self.lbl036 = Label(self.tab2,text='Состояния реле 1 MR1 = ')
        self.lbl036.grid(column=0, row=19, sticky='w')
        self.lbl037 = Label(self.tab2,text='нет датчика')
        self.lbl037.grid(column=1, row=19)

        self.lbl038 = Label(self.tab2,text='Состояния реле 2 MR1 = ')
        self.lbl038.grid(column=0, row=20, sticky='w')
        self.lbl039 = Label(self.tab2,text='нет датчика')
        self.lbl039.grid(column=1, row=20)

        self.lbl040 = Label(self.tab2,text='Состояния реле 3 MR1 = ')
        self.lbl040.grid(column=0, row=21, sticky='w')
        self.lbl041 = Label(self.tab2,text='нет датчика')
        self.lbl041.grid(column=1, row=21)

        self.lbl042 = Label(self.tab2,text='Состояния реле 4 MR1 = ')
        self.lbl042.grid(column=0, row=22, sticky='w')
        self.lbl043 = Label(self.tab2,text='нет датчика')
        self.lbl043.grid(column=1, row=22)

        self.lbl044 = Label(self.tab2,text='Состояния реле 5 MR1 = ')
        self.lbl044.grid(column=0, row=22, sticky='w')
        self.lbl045 = Label(self.tab2,text='нет датчика')
        self.lbl045.grid(column=1, row=22)

        self.lbl046 = Label(self.tab2,text='Состояния реле 6 MR1 = ')
        self.lbl046.grid(column=0, row=23, sticky='w')
        self.lbl047 = Label(self.tab2,text='нет датчика')
        self.lbl047.grid(column=1, row=23)

        self.lbl048 = Label(self.tab2,text='Состояния реле 7 MR1 = ')
        self.lbl048.grid(column=0, row=24, sticky='w')
        self.lbl049 = Label(self.tab2,text='нет датчика')
        self.lbl049.grid(column=1, row=24)

        self.lbl050 = Label(self.tab2,text='Состояния реле 8 MR1 = ')
        self.lbl050.grid(column=0, row=25, sticky='w')
        self.lbl051 = Label(self.tab2,text='нет датчика')
        self.lbl051.grid(column=1, row=25)

        self.lbl052 = Label(self.tab2,text='Состояния реле 1 А2 = ')
        self.lbl052.grid(column=0, row=26, sticky='w')
        self.lbl053 = Label(self.tab2,text='нет датчика')
        self.lbl053.grid(column=1, row=26)

        self.lbl054 = Label(self.tab2,text='Состояния реле 2 А2 = ')
        self.lbl054.grid(column=0, row=27, sticky='w')
        self.lbl055 = Label(self.tab2,text='нет датчика')
        self.lbl055.grid(column=1, row=27)

        self.tab_control.add(self.tab3,text='Управление выходами')


        self.var01 = BooleanVar()
        self.var02 = BooleanVar()
        self.var03 = BooleanVar()
        self.var04 = BooleanVar()
        self.var05 = BooleanVar()
        self.var06 = BooleanVar()
        self.var07 = BooleanVar()
        self.var08 = BooleanVar()
        self.var09 = BooleanVar()
        self.var10 = BooleanVar()
        self.var11 = BooleanVar()
        self.var12 = BooleanVar()
        cb01 = Checkbutton(self.tab3, text="Вкл/выкл реле 1 А1: ", variable=self.var01)
        cb02 = Checkbutton(self.tab3, text="Вкл/выкл реле 2 А1: ", variable=self.var02)
        cb03 = Checkbutton(self.tab3, text="Вкл/выкл реле 1 MR1: ", variable=self.var03)
        cb04 = Checkbutton(self.tab3, text="Вкл/выкл реле 2 MR1: ", variable=self.var04)
        cb05 = Checkbutton(self.tab3, text="Вкл/выкл реле 3 MR1: ", variable=self.var05)
        cb06 = Checkbutton(self.tab3, text="Вкл/выкл реле 4 MR1: ", variable=self.var06)
        cb07 = Checkbutton(self.tab3, text="Вкл/выкл реле 5 MR1: ", variable=self.var07)
        cb08 = Checkbutton(self.tab3, text="Вкл/выкл реле 6 MR1: ", variable=self.var08)
        cb09 = Checkbutton(self.tab3, text="Вкл/выкл реле 7 MR1: ", variable=self.var09)
        cb10 = Checkbutton(self.tab3, text="Вкл/выкл реле 8 MR1: ", variable=self.var10)
        cb11 = Checkbutton(self.tab3, text="Вкл/выкл реле 1 A2: ", variable=self.var11)
        cb12 = Checkbutton(self.tab3, text="Вкл/выкл реле 1 A2: ", variable=self.var12)
        cb01.deselect()
        cb02.deselect()
        cb03.deselect()
        cb04.deselect()
        cb05.deselect()
        cb06.deselect()
        cb07.deselect()
        cb08.deselect()
        cb09.deselect()
        cb10.deselect()
        cb11.deselect()
        cb12.deselect()
        cb01.grid(column=0,row=2,sticky='w')
        cb02.grid(column=0,row=3,sticky='w')
        cb03.grid(column=0,row=4,sticky='w')
        cb04.grid(column=0,row=5,sticky='w')
        cb05.grid(column=0,row=6,sticky='w')
        cb06.grid(column=0,row=7,sticky='w')
        cb07.grid(column=0,row=8,sticky='w')
        cb08.grid(column=0,row=9,sticky='w')
        cb09.grid(column=0,row=10,sticky='w')
        cb10.grid(column=0,row=11,sticky='w')
        cb11.grid(column=0,row=13,sticky='w')
        cb12.grid(column=0,row=14,sticky='w')
        self.lbl22 = Label(self.tab3,text='False')
        self.lbl23 = Label(self.tab3,text='False')
        self.lbl24 = Label(self.tab3,text='False')
        self.lbl25 = Label(self.tab3,text='False')
        self.lbl26 = Label(self.tab3,text='False')
        self.lbl27 = Label(self.tab3,text='False')
        self.lbl28 = Label(self.tab3,text='False')
        self.lbl29 = Label(self.tab3,text='False')
        self.lbl30 = Label(self.tab3,text='False')
        self.lbl31 = Label(self.tab3,text='False')
        self.lbl32 = Label(self.tab3,text='False')
        self.lbl33 = Label(self.tab3,text='False')
        self.lbl22.grid(column=1,row=2)
        self.lbl23.grid(column=1,row=3)
        self.lbl24.grid(column=1,row=4)
        self.lbl25.grid(column=1,row=5)
        self.lbl26.grid(column=1,row=6)
        self.lbl27.grid(column=1,row=7)
        self.lbl28.grid(column=1,row=8)
        self.lbl29.grid(column=1,row=9)
        self.lbl30.grid(column=1,row=10)
        self.lbl31.grid(column=1,row=11)
        self.lbl32.grid(column=1,row=13)
        self.lbl33.grid(column=1,row=14)

        self.tab_control.pack(expand=1,fill='both')
    

    def show_work_status_A1(self):
        self.lbl00['text'] = 'Связь с А1 установлена'
        self.lbl10['text'] = 'Связь с А1 установлена'
        self.lbl20['text'] = 'Связь с А1 установлена'
        self.lbl00['fg'] = 'green'
        self.lbl10['fg'] = 'green'
        self.lbl20['fg'] = 'green'
    
    def show_work_status_A2(self):

        self.lbl01['text'] = 'Связь с А2 установлена'
        self.lbl11['text'] = 'Связь с А2 установлена'
        self.lbl21['text'] = 'Связь с А2 установлена'
        self.lbl01['fg'] = 'green'
        self.lbl11['fg'] = 'green'
        self.lbl21['fg'] = 'green'

    def show_error_status_A1(self):
        self.lbl00['text'] = 'Связь с А1 отсутствует'
        self.lbl10['text'] = 'Связь с А1 отсутствует'
        self.lbl20['text'] = 'Связь с А1 отсутствует'
        self.lbl00['fg'] = 'red'
        self.lbl10['fg'] = 'red'
        self.lbl20['fg'] = 'red'

    def show_error_status_A2(self):
        self.lbl01['text'] = 'Связь с А2 отсутствует'
        self.lbl11['text'] = 'Связь с А2 отсутствует'
        self.lbl21['text'] = 'Связь с А2 отсутствует'
        self.lbl01['fg'] = 'red'
        self.lbl11['fg'] = 'red'
        self.lbl21['fg'] = 'red'

    def update(self):
        # Подключение к MODBUS серверу
        # и получение данных регистров карты
        
        client = ModbusClient(method = 'rtu', 
                        port = str(self.combobox1.get()), 
                        timeout = 2, 
                        stopbits = 1, 
                        bytesize = 8, 
                        parity = 'N', 
                        baudrate = 115200)
        try:
            client.connect()
            self.show_work_status_A1()
        except:
            self.show_error_status_A1()

        try:
            ir = client.read_input_registers(address=0,count=22,unit=1)

            self.lbl003['text'] = str(ir.registers[0])
            self.lbl005['text'] = str(ir.registers[1])
            self.lbl007['text'] = str(ir.registers[2])
            self.lbl009['text'] = str(ir.registers[3])
            self.lbl011['text'] = str(ir.registers[4])
            self.lbl021['text'] = status[ir.registers[5]]
            self.lbl023['text'] = status[ir.registers[6]]
            self.lbl025['text'] = status[ir.registers[7]]
            self.lbl027['text'] = status[ir.registers[8]]
            self.lbl029['text'] = status[ir.registers[9]]
            self.lbl031['text'] = status[ir.registers[10]]
            self.lbl033['text'] = status[ir.registers[11]]
            self.lbl035['text'] = status[ir.registers[12]]
            self.lbl037['text'] = status[ir.registers[13]]
            self.lbl039['text'] = status[ir.registers[14]]
            self.lbl041['text'] = status[ir.registers[15]]
            self.lbl043['text'] = status[ir.registers[16]]
            self.lbl045['text'] = status[ir.registers[17]]
            self.lbl047['text'] = status[ir.registers[18]]
            self.lbl049['text'] = status[ir.registers[19]]
            self.lbl051['text'] = status[ir.registers[20]]
            self.lbl13['text'] = manage[ir.registers[21]]
            self.show_work_status_A1()
        except:
            self.show_error_status_A1()
        
        try:
            values.append(int(self.var01.get()))
            values.append(int(self.var02.get()))
            values.append(int(self.var03.get()))
            values.append(int(self.var04.get()))
            values.append(int(self.var05.get()))
            values.append(int(self.var06.get()))
            values.append(int(self.var07.get()))
            values.append(int(self.var08.get()))
            values.append(int(self.var09.get()))
            values.append(int(self.var10.get()))
            client.write_registers(address=0,values=values,unit=1)
            values.clear()
            self.show_work_status_A1()
        except:
            self.show_error_status_A1()
        client.close()

        try:
            client.connect()
            self.show_work_status_A2()
        except:
            self.show_error_status_A2()

        try:
            ir = client.read_input_registers(address=0,count=14,unit=2)

            self.lbl013['text'] = str(ir.registers[0])
            self.lbl015['text'] = str(ir.registers[1])
            self.lbl017['text'] = str(ir.registers[2])
            self.lbl019['text'] = str(ir.registers[3])

            self.lbl053['text'] = status[ir.registers[11]]
            self.lbl055['text'] = status[ir.registers[12]]
            self.lbl15['text'] = manage[ir.registers[13]]
            self.show_work_status_A2()
        except:
            self.show_error_status_A2()

        try:
            values.append(int(self.var11.get()))
            values.append(int(self.var12.get()))
            client.write_registers(address=0,values=values,unit=2)
            values.clear()
            self.show_work_status_A2()
        except:
            self.show_error_status_A2()
        client.close()

        self.lbl22['text'] = status[self.var01.get()]
        self.lbl23['text'] = status[self.var02.get()]
        self.lbl24['text'] = status[self.var03.get()]
        self.lbl25['text'] = status[self.var04.get()]
        self.lbl26['text'] = status[self.var05.get()]
        self.lbl27['text'] = status[self.var06.get()]
        self.lbl28['text'] = status[self.var07.get()]
        self.lbl29['text'] = status[self.var08.get()]
        self.lbl30['text'] = status[self.var09.get()]
        self.lbl31['text'] = status[self.var10.get()]
        self.lbl32['text'] = status[self.var11.get()]
        self.lbl33['text'] = status[self.var12.get()]
        
        self.after(1000,self.update)
        

def main():
    app = App()
    app.after_idle(app.update)
    # app.after(1000,app.update)
    app.mainloop()

if __name__ == '__main__':
    main()
