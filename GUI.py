from tkinter import *
from tkinter import ttk
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
import matplotlib.pyplot as plt

"""In deze klasse wordt de layout geinitialiseerd. 
Er word gebruik gemaakt van een canvas om de grafieken op te tekenen
en er zijn tabbladen gemaakt voor de verschillende arduino's"""

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Centrale')
        self.controller = self

        container = tk.Frame(self)
        container.pack(side="bottom", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.frames["StartPage"] = StartPage(parent=container, controller=self)
        self.frames["Arduino1"] = Arduino1(parent=container, controller=self)
        self.frames["Arduino2"] = Arduino2(parent=container, controller=self)
        self.frames["Arduino3"] = Arduino3(parent=container, controller=self)
        self.frames["Arduino4"] = Arduino4(parent=container, controller=self)
        self.frames["Arduino5"] = Arduino5(parent=container, controller=self)
        self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["Arduino1"].grid(row=0, column=0, sticky="nsew")
        self.frames["Arduino2"].grid(row=0, column=0, sticky="nsew")
        self.frames["Arduino3"].grid(row=0, column=0, sticky="nsew")
        self.frames["Arduino4"].grid(row=0, column=0, sticky="nsew")
        self.frames["Arduino5"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Startpagina", font='Helvetica 18 bold')
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Arduino 1", command=lambda: self.arduino1())
        button1.pack(side="top", pady=5)

        uitrollen = tk.Button(self, text="Arduino 2", command=lambda: self.arduino2())
        uitrollen.pack(side="top", pady=5)

        inhalen = tk.Button(self, text="Arduino 3", command=lambda: self.arduino3())
        inhalen.pack(side="top", pady=5)

        stoppen = tk.Button(self, text="Arduino 4", command=lambda: self.arduino4())
        stoppen.pack(side="top", pady=5)

        stoppen = tk.Button(self, text="Arduino 5", command=lambda: self.arduino5())
        stoppen.pack(side="top", pady=5)

    def add_ui(self):
        uitrollen = tk.Button(self, text="  Uitrollen   ", command=lambda: self.rolluik_uitrollen())
        uitrollen.grid(column=1,row=0,sticky=N,pady=150)

        inhalen = tk.Button(self, text="   Inhalen    ", command=lambda: self.rolluik_inhalen())
        inhalen.grid(column=1,row=0,sticky=N,pady=180)

        stoppen = tk.Button(self, text="  Stoppen   ", command=lambda: self.stoppen())
        stoppen.grid(column=1,row=0,sticky=N,pady=210)

        button1 = tk.Button(self, text="     Terug     ", command=lambda: self.home())
        button1.grid(column=1,row=0,sticky=N,pady=240)

        label = tk.Label(self, text="Instellingen", font='Helvetica 18 bold')
        label.grid(column=1,row=0,sticky=N)

        self.uitrol_label = tk.Label(self, text=" Maximale uitrolstand:")
        self.uitrol_label.grid(column=1,row=0,sticky=N,pady=50)
        self.uitrol_choiceVar = tk.StringVar()
        self.uitrol = ttk.Entry(self, textvariable=self.uitrol_choiceVar)
        self.uitrol.grid(column=2,row=0,sticky=N,pady=50)

        self.inrol_label = tk.Label(self, text="Maximale inrolstand:")
        self.inrol_label.grid(column=1,row=0,sticky=N,pady=80)
        self.inrol_choiceVar = tk.StringVar()
        self.inrol = ttk.Entry(self, textvariable=self.inrol_choiceVar)
        self.inrol.grid(column=2,row=0,sticky=N,pady=80)

        toepassen = tk.Button(self, text="Toepassen", command=lambda: self.toepassen())
        toepassen.grid(column=3,row=0,sticky=N,pady=75,padx=10)

    def arduino1(self):
        self.controller.show_frame("Arduino1")

    def arduino2(self):
        self.controller.show_frame("Arduino2")

    def arduino3(self):
        self.controller.show_frame("Arduino3")

    def arduino4(self):
        self.controller.show_frame("Arduino4")

    def arduino5(self):
        self.controller.show_frame("Arduino5")

    def home(self):
        self.controller.show_frame("StartPage")


class Arduino1(StartPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.add_ui()

        #test graph
        Data = {'Tijd': [14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                'Temperatuur': [11, 10, 9, 8, 7, 5, 4, 4, 4, 4]}
        df = DataFrame(Data, columns=['Tijd', 'Temperatuur'])
        df = df[['Tijd', 'Temperatuur']].groupby('Tijd').sum()
        figure = plt.Figure(figsize=(7, 5), dpi=100)
        ax = figure.add_subplot(111)
        self.graph1 = FigureCanvasTkAgg(figure, self)
        df.plot(kind='line', legend=True, ax=ax, color='b', fontsize=10)
        self.graph1.get_tk_widget().grid(column=0, row=0)

    def rolluik_uitrollen(self):
        print("Aan het uitrollen")

    def rolluik_inhalen(self):
        print("Aan het inhalen")

    def stoppen(self):
        print("De rolluiken stoppen")

class Arduino2(StartPage):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.add_ui()

        Data2 = {'Tijd': [14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                'Lichtintensiteit': [10, 8, 6, 3, 2.5, 2, 1.5, 1, 1, 1]}
        df2 = DataFrame(Data2, columns=['Tijd', 'Lichtintensiteit'])
        df2 = df2[['Tijd', 'Lichtintensiteit']].groupby('Tijd').sum()
        figure2 = plt.Figure(figsize=(7, 5), dpi=100)
        ax2 = figure2.add_subplot(111)
        self.graph2 = FigureCanvasTkAgg(figure2, self)
        df2.plot(kind='line', legend=True, ax=ax2, color='b', fontsize=10)
        self.graph2.get_tk_widget().grid(column=0, row=0)


    def start(self):
        self.controller.show_frame("StartPage")

    def toepassen(self):
        print("De maximale uirolstand is nu:", self.uitrol_choiceVar.get())
        print("De maximale inrolstand is nu:", self.inrol_choiceVar.get())

class Arduino3(StartPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.add_ui()

class Arduino4(StartPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.add_ui()

class Arduino5(StartPage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.add_ui()
