import tkinter as tk
import pandas as pd
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

input1=[]
#input2=[]
#save entries, apend to list, and destroy window
def enter_details_quit():
    global temp
    #global f_or_c
    temp=int(entry1.get())
    input1.append(temp)
    # f_or_c=entry2.get()
    # input2.append(f_or_c)
    win.destroy()

#find wind chill
def find_windchill(temp, wind):
    windchill=35.74 + (0.6215 * temp) - 35.75 * (wind ** 0.16) + (0.4275 * temp) * (wind ** 0.16)
    return windchill

# convert celsius to fahrenheit
def c_to_f(temp):
    temp = temp * (9/5) + 32
    return temp

#convert celsius to fahrenheit, find wind chill, and fahrenheit back to celsius
def find_celsius(temp, wind):
    windchill = 35.74 + (0.6215 * c_to_f(temp)) - 35.75 * (wind ** 0.16) + (0.4275 * c_to_f(temp)) * (wind ** 0.16)
    return windchill

#create new window
global temp
#global f_or_c
win=Tk()
win.geometry('500x400')
#add first label
Label(win,text='What is the tempurature?',font=(20)).grid(row = 0)
#add and get first entry
entry1=Entry(win,font=(20))
entry1.grid(row=0,column=1)
temp=entry1.get()
# #add second label
# Label(win,text='Fahrenheit or Celsius?(F or C)',font=(20)).grid(row = 1)
# #add and get second entry
# entry2=Entry(win,font=(20))
# entry2.grid(row=1,column=1)
# f_or_c=entry2.get()
# #add button to save entries and destroy window
Button(win, text='Compute',command=enter_details_quit).grid(row=16,column=1)
win.mainloop()

#create error window if f or c not entered
# while f_or_c != 'f' or f_or_c != 'c':
#     if f_or_c.lower() == 'f':
#         #add button to save entries and destroy window
#         Button(win, text='Compute',command=enter_details_quit).grid(row=16,column=1)
#         win.mainloop()
#         break
#     elif f_or_c.lower() == 'c':
#         #add button to save entries and destroy window
#         Button(win, text='Compute',command=enter_details_quit).grid(row=16,column=1)
#         win.mainloop()
#         break
#     else:
#         newwin=Tk()
#         newwin.title('ERROR')
#         Label(newwin,text='Please enter Fahrenheit or Celsius:(F or C)',font=(20)).grid(row = 1)
#         #add and get second entry
#         entry2=Entry(newwin,font=(20)).grid(row=1,column=1)
#         f_or_c=entry2.get().lower()
#         Button(newwin, text='Compute',command=enter_details_quit).grid(row=1,column=2)
#         newwin.mainloop()

#append all wind speeds and wind chill fahrenheit tempuratures to lists
windspeed=[]
templist=[]
for wind in range(5,70,5):
    windspeed.append(wind)
    windchill=find_windchill(temp, wind)
    templist.append(float(f'{windchill:.2f}'))
data1={'Wind Speed': windspeed,'Wind Chill': templist}  
df1=pd.DataFrame(data1)

#append all wind speeds and wind chill celsius tempuratures to lists
windspeed=[]
ctemplist=[]
for wind in range(5,70,5):
    windspeed.append(wind)
    cwindchill = find_celsius(temp, wind)
    ctemplist.append(float(f'{cwindchill:.2f}'))
data2={'Wind Speed': windspeed,'Wind Chill': ctemplist}  
df2=pd.DataFrame(data2)

#create new window
def root(df1, df2):
    root = tk.Tk()
    #create conversion label
    Label(root,text=f'{temp}C is equal to {c_to_f(temp)}F',font=(20)).pack(side=tk.TOP, fill=tk.BOTH)
    #add button to destroy window
    Button(root, text='Done',command=root.destroy).pack(side=tk.TOP, fill=tk.BOTH)
    #create figure and plot graph points
    figure1 = plt.Figure(figsize=(5, 5), dpi=100)
    ax1 = figure1.add_subplot(111)
    line1 = FigureCanvasTkAgg(figure1, root)
    line1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df1 = df1[['Wind Speed', 'Wind Chill']].groupby('Wind Speed').sum()
    df1.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=10, ylabel='Tempurature')
    ax1.set_title('Fahrenheit\nWind Speed Vs. Wind Chill')
    # #plot points with coordinates shown
    # plt.rcParams['figure.figsize'] = [7, 4]
    # plt.rcParams['figure.autolayout'] = True
    # plt.plot(windspeed, templist, 'r*')
    # plt.axis([0, max(windspeed)+5, min(templist)-5, max(templist)+5])
    # for i, j in zip(windspeed, templist):
    #     plt.text(i, j+0.5, '{}MPH, {}F'.format(i, j))

    #create second figure and plot graph points
    figure2 = plt.Figure(figsize=(5, 5), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2 = df2[['Wind Speed', 'Wind Chill']].groupby('Wind Speed').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10, ylabel='Tempurature')
    ax2.set_title('Celsius\nWind Speed Vs. Wind Chill')
    # #plot points with coordinates shown
    # plt.rcParams['figure.figsize'] = [7, 4]
    # plt.rcParams['figure.autolayout'] = True
    # plt.plot(windspeed, ctemplist, 'r*')
    # plt.axis([0, max(windspeed)+5, min(ctemplist)-5, max(ctemplist)+5])
    # for i, j in zip(windspeed, ctemplist):
    #     plt.text(i, j+0.5, '{}MPH, {}C'.format(i, j))
    # plt.show()
    root.mainloop()

root(df1, df2)