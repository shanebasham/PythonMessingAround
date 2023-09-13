
# # import tkinter as tk

# # window = tk.Tk()
# # label = tk.Label(text='What is the temperature?', fg='teal',bg='white', width=50, height=20)
# # label.pack()

# # entry = tk.Entry(fg='teal', bg='white', width=20)
# # entry.pack()
# # temp = entry.get()

# # entry.insert(0, temp)

# # window.mainloop()

# import tkinter as tk
# from tkinter import Canvas

# win= tk.Tk()

# frame_a = tk.Frame()
# frame_b = tk.Frame()

# label_a = tk.Label(master=frame_a, text="I'm in Frame A")
# label_a.pack()

# label_b = tk.Label(master=frame_b, text="I'm in Frame B")
# label_b.pack()

# frame_a.pack()
# frame_b.pack()

# win.geometry("600x400")
# c= Canvas(win,width=400, height=400)
# c.pack()
# c.create_rectangle(60,60,50,50)

# win.mainloop()

from tkinter import *
global e1_input
enter_details = Tk()
enter_details.title("Fill details here")
enter_details.geometry("500x700")
Label(enter_details,text = "Name :").grid(row = 0)
e1=Entry(enter_details)
e1.grid(row=0,column=1)
e1_input = e1.get()
Label(enter_details,text ="Enrollment no. :").grid(row=1)
e2=Entry(enter_details)
e2.grid(row=1,column=1)
Label(enter_details,text = "Father's name :").grid(row=2)
e3=Entry(enter_details)
e3.grid(row=2,column=1)
Label(enter_details,text = "Previous CGPA :").grid(row=3)
e4=Entry(enter_details)
e4.grid(row = 3,column=1)
Label(enter_details,text = "Semester :").grid(row=4)
e5=Entry(enter_details)
e5.grid(row = 4,column=1)

input = []

def enter_details_quit():
    global e1_input
    e1_input = e1.get()
    input.append(e1_input.upper())
    enter_details.destroy()

def show():
    Label(enter_details,text="Name : "+e1.get()).grid(row=6)
    Label(enter_details,text="Enrollment no. : "+e2.get()).grid(row=7)
    Label(enter_details,text="Father's name : "+e3.get()).grid(row=8)
    Label(enter_details,text="previous CGPA : "+e4.get()).grid(row=9)
    Label(enter_details,text="Semester : "+e5.get()).grid(row=10)
Button(enter_details, text='Check',command=show).grid(row=16,column=6)
Button(enter_details, text='Done',command=enter_details_quit).grid(row=16,column=1)
enter_details.mainloop()


marksheet = Tk()
marksheet.title("Third sem marksheet")
marksheet.geometry("500x400")

clg_name= Label(marksheet)
clg_name.config(text='TECHNOCRATS INSTITUTE OF TECHNOLOGY')
clg_name.config(font=('times',10,'bold'))
clg_name.config(fg='red')
clg_name.pack()
show_name=Label(text=input)
show_name.pack()
b1=Button(marksheet, text='Done',command=marksheet.destroy)
b1.pack(expand=YES)


marksheet.mainloop()