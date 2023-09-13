
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

#open window and define functions
class MyWindow:
    def __init__(self, win):
        x0, xt0, y0 = 10, 100, 250
        #first label and entry
        self.lbl0 = Label(win, text='Tempurature')
        self.lbl0.config(font=('Arial', 10))
        self.lbl0.place(x=x0, y=y0)
        self.t0 = Entry(font=(20))
        self.t0.place(x=xt0, y=y0)
        self.t0.insert(END, str(0))
        self.t_0 = float(self.t0.get())

        #second label and entry 
        self.lbl1 = Label(win, text='F or C')
        self.lbl1.config(font=('Arial', 10))
        self.lbl1.place(x=x0, y=y0 + 40)
        self.t1 = Entry(font=(20))
        self.t1.place(x=xt0, y=y0 + 40)
        self.t1.insert(END, str(1))
        self.t_1 = float(self.t1.get())

        #f label
        self.lbl2 = Label(win, text='(Fahrenheit)')
        self.lbl2.config(font=('Arial', 10, 'bold'))
        self.lbl2.place(x=x0 + 250, y=y0 - 100)

        #c label
        self.lbl3 = Label(win, text='(Celsius)')
        self.lbl3.config(font=('Arial', 10, 'bold'))
        self.lbl3.place(x=x0 + 250, y=y0 + 180)

        #compute button
        self.btn = Button(win, text='Compute')
        self.btn.bind('<Button-1>', self.plot)
        self.btn.place(x=xt0, y=y0 + 80)
        self.figure = Figure(figsize=(4.5, 3), dpi=100)

        #graph 1
        self.subplot1 = self.figure.add_subplot(211)
        self.subplot1.set_xlim(self.t_0, self.t_1)
        self.subplot1.set_xlabel('$Time(s)$', fontsize=10)
        self.subplot1.set_xlim(self.t_0, self.t_1)
        self.subplot1.set_ylabel('$Tempurature$', fontsize=10)
        self.subplot1.set_ylim(self.t_0, self.t_1)

        #graph 2
        self.subplot2 = self.figure.add_subplot(212)
        self.subplot2.set_xlabel('$Time(s)$', fontsize=10)
        self.subplot2.set_xlim(self.t_0, self.t_1)
        self.subplot2.set_ylabel('$Tempurature$', fontsize=10)
        self.subplot2.set_ylim(self.t_0, self.t_1)

        #show graphs
        self.plots = FigureCanvasTkAgg(self.figure, win)
        self.plots.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=0)

    def data(self):
        self.t_0 = float(self.t0.get())
        self.t_1 = float(self.t1.get())
        t = np.linspace(self.t_0, self.t_1, 100)
        func1 = t**0.5
        func2 = t**2.
        return t, func1, func2

    def plot(self, event):
        t, func1, func2 = self.data()
        self.t_0 = float(self.t0.get())
        self.t_1 = float(self.t1.get())
        self.subplot1.set_xlim(self.t_0, self.t_1)
        self.subplot1.plot(t, func1, 'r', lw=2.5)
        self.subplot2.set_xlim(self.t_0, self.t_1)
        self.subplot2.plot(t, func2, 'b', lw=2.5)
        self.plots.draw()


window = Tk()
mywin = MyWindow(window)
window.title('Wind Chill')
window.geometry("800x600+10+10")
window.mainloop()