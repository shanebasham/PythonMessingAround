
from tkinter import *

def donothing(var=''):
    pass

class Interface(Tk):
    def __init__(self, name='Interface', size=None):
        super(Interface, self).__init__()
        if size:
            self.geometry(size)
        self.title(name)
        self.frame = Frame(self)
        self.frame.pack()

    def gui_print(self, text='This is some text', command=donothing):
        self.frame.destroy()
        self.frame = Frame(self)
        self.frame.pack()
        Label(self.frame, text=text).pack()
        Button(self.frame, text='Ok', command=command).pack()

    def gui_input(self, text='Enter something', command=donothing):
        self.frame.destroy()
        self.frame = Frame(self)
        self.frame.pack()        
        Label(self.frame, text=text).pack()
        entry = StringVar(self)
        Entry(self.frame, textvariable=entry).pack()
        Button(self.frame, text='Ok', command=lambda: command(entry.get())).pack()

    def end(self):
        self.destroy()

    def start(self):
        mainloop()


# -- Testing Stuff --

def name(value):
    global main
    main.gui_print(f'Your name is {value}.', main.end)


def bar():
    global main
    main.gui_input('What is your name?', name)


if __name__ == '__main__':
    main = Interface('Window')
    bar()
    main.start()


# import tkinter as tk
# from tkinter import *

# class App:
#     def __init__(self):
#         self.HEIGHT = 600
#         self.WIDTH = 600    
#         root = tk.Tk()
#         root.width = self.WIDTH
#         root.height = self.HEIGHT
#         self.dialogroot = root
#         self.strDialogResult = ""    
#         self.canvas = tk.Canvas(root, height=self.HEIGHT, width=self.WIDTH)
#         self.canvas.pack()    
#         frame = tk.Frame(root, bg='#42c2f4')
#         frame.place(relx=0.5, rely=0.02, relwidth=0.96, relheight=0.95, anchor='n')  
#         # Here is the button call to the InputBox() function
#         buttonInputBox = tk.Button(frame, text="Input Box", bg='#cccccc', font=60, 
#         command=lambda: self.InputBox())    
#         buttonInputBox.place(relx=0.05, rely=0.1, relwidth=0.90, relheight=0.8)    
#         root.mainloop()

#     def InputBox(self):        
#         dialog = tk.Toplevel(self.dialogroot)
#         dialog.width = 600
#         dialog.height = 100

#         frame = tk.Frame(dialog,  bg='#42c2f4', bd=5)
#         frame.place(relwidth=1, relheight=1)

#         entry = tk.Entry(frame, font=40)
#         entry.place(relwidth=0.65, rely=0.02, relheight=0.96)
#         entry.focus_set()

#         submit = tk.Button(frame, text='OK', font=16, command=lambda: self.DialogResult(entry.get()))
#         submit.place(relx=0.7, rely=0.02, relheight=0.96, relwidth=0.3)

#         root_name = self.dialogroot.winfo_pathname(self.dialogroot.winfo_id())
#         dialog_name = dialog.winfo_pathname(dialog.winfo_id())

#         # These two lines show a modal dialog
#         self.dialogroot.tk.eval('tk::PlaceWindow {0} widget {1}'.format(dialog_name, root_name))
#         self.dialogroot.mainloop()

#         #This line destroys the modal dialog after the user exits/accepts it
#         dialog.destroy()

#         #Print and return the inputbox result
#         print(self.strDialogResult)
#         return self.strDialogResult

#     def DialogResult(self, result):
#         self.strDialogResult = result
#         #This line quits from the MODAL STATE but doesn't close or destroy the modal dialog
#         self.dialogroot.quit()

# # Launch ...
# if __name__ == '__main__':
#     app = App()

##########################################################

# import tkinter as tk
# from collections import deque

# first = deque([])
# last = deque([])
# nom = 0

# class Application(tk.Frame):
#     def __init__(self, master=None, nom=0, priono=1, prio=1):
#         super().__init__(master)

#         self.pack()
#         self.create_widgets()
#         self.nom = nom
#         self.priono= priono
#         self.prio=prio

#     def create_widgets(self):
#         self.add = tk.Button(self, bg ="black", fg="teal")
#         self.add["text"] =   "-----Add to queue-----\n"
#         self.add["command"] = self.create_window
#         self.add.pack(side="top", pady = 10, padx = 20)
#         self.add["font"] = "Times 16 bold"

#         self.remov = tk.Button(self, bg ="black", fg="teal")
#         self.remov["text"]= "---Remove in queue---\n"
#         self.remov["command"] = self.remov_
#         self.remov.pack(side="top", pady = 10, padx = 20)
#         self.remov["font"] = "Times 16 bold"

#         self.quit = tk.Button(self, text="QUIT", fg="white", bg = "red",
#         command=root.destroy)
#         self.quit.pack(side="bottom")

#     def create_window(self):
#         def inputer():
#             print('inputer ', end=': ')
#             print(self.E1.get())

#         win2 = tk.Toplevel(self)
#         win2_button = tk.Button(win2, text='Ready?\nClick Here', command=inputer)
#         win2_button.pack()
#         self.L1 = tk.Label(win2, text = "Name")
#         self.L1.pack( side=tk.LEFT)
#         self.E1 = tk.Entry(win2, bd =5)
#         self.E1.pack(side=tk.RIGHT)

#     def say_hi(self):
#         print("hi there, everyone!")

#     def add_1(self):
#         name=input("What is your name? ")
#         first.append(name)
#         print("Good Day!",first[self.nom])
#         print("Your priority number is:","%03d" % (self.priono))
#         self.priono+=1
#         self.nom+= 1

#     def remov_(self):
#         if (len(first)) >= 1:
#             first.popleft()
#         else:
#             print("No one left in queue")


# root = tk.Tk()
# root.config(background="black")

# app = Application(master=root)
# app.master.title("ID QUEUEING SYSTEM beta")
# app.master.minsize(540, 360)
# app.master.maxsize(600, 500)
# app.mainloop()