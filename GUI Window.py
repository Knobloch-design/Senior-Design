# This is a sample Python script.
import sys

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import tkinter as tk
import time
import random

import mysql.connector
from mysql.connector import Error
import pandas as pd


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import sqlite3


"""
Function Creates random Data to test with
"""
def randomData(x):
    return x + random.uniform(-5.0, 5.0)


"""
Class initializes sql table call temperature
"""
"""
class Table:

    conn = sqlite3.connect('DataBase.sqlite')
    cur = conn.cursor()

    
    #Function creates temperature table as well as creates the columns id and temp_c
    
    def init(self):
        print("hello world")
        self.cur.execute('CREATE TABLE IF NOT EXISTS temperature (Id INTEGER PRIMARY KEY,temp_c REAL)')
        #self.cur.execute('ALTER TABLE temperature ADD COLUMN Temp FLOAT')  # Add new column to table


        #code here creates test data to fill sql table

        xar = [i for i in range(1, 101)]
        yar = [randomData(i) for i in [30] * 300]

        for i in xar:
            self.cur.execute('INSERT INTO temperature (temp_c) VALUES ('+str(yar[i])+')')

"""

#this code is ment for mySQL 
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("ALTER TABLE mydatabase ADD COLUMN Time INT ")
mycursor.execute("ALTER TABLE mydatabase ADD COLUMN Temp INT ")



#fig = plt.figure()
#ax1 = fig.add_subplot(1, 1, 1)
Celsius = True
test = Table
Table.init(test)
tempScale  = "C"


#does nothing now
def handle_click(event):
    plt.draw()
    plt.show()
"""
def restart():
    ani.frame_seq = ani.new_frame_seq()
    ani.event_source.start()
"""

def celcius_to_f(temp_c):
    return temp_c*(9/5)+32



def graph_F(event):
    global Celsius
    global tempScale
    global fig
    global ax1
    Celsius = False
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    tempScale = "F"
    anim = animation.FuncAnimation(fig, animate, interval=1000)
    plt.draw()
    plt.show()






def graph_C(event):
    global Celsius
    global tempScale
    global fig
    global ax1
    Celsius = True
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    tempScale = "C"
    anim = animation.FuncAnimation(fig, animate, interval=1000)
    plt.draw()
    plt.show()


def animate(i):
    global Table

    Table.cur.execute('SELECT Id FROM temperature')
    Id = Table.cur.fetchall()
    Table.cur.execute('SELECT temp_c FROM temperature')
    temp = Table.cur.fetchall()
    #ax1.clear()
    ax1.plot(Id[:i], temp[:i])
    plt.ylim(1, 100)
    plt.xlabel("Time (sec)")
    plt.ylabel("Temp ("+tempScale+")")
    plt.title("Temperature vs Time")


#ani = animation.FuncAnimation(fig, animate, interval=1000)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    SensorStatus = "Sensor Plugged in"
    BoxStatus = "Box OFF"




    window = tk.Tk()
    for i in range(4):
        window.columnconfigure(i, weight=1, minsize=75)
        window.rowconfigure(i, weight=1, minsize=50)

        for j in range(0, 3):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j, padx=5, pady=5)
            #label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
            #label.pack(padx=5, pady=5)

    greeting = tk.Label(text=SensorStatus)
    greeting.grid(row =0, column=0)
    #frame = tk.Frame(master=window, height=200, width=200)
    labelBox = tk.Label(
        text=BoxStatus,
        width=10,
        height=5,
    )

    FButton = tk.Button(
        text="Fahrenheit",
        width=10,
        height=5,
        bg="red",
        fg="yellow",
    )
    CButton = tk.Button(
        text="Celsius",
        width=10,
        height=5,
        bg="yellow",
        fg="black",
    )
    FButton.bind("<Button-1>", graph_F)
    CButton.bind("<Button-1>", graph_C)

    #frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    labelBox.grid(row =1, column=0)
    greeting.grid(row =2, column=0)

    FButton.grid(row=1, column=1)
    CButton.grid(row=2, column=1)
    window.mainloop() #blocks code after it till the window is closed

    #5. Run your application's event loop
    #sys.exit(app.exec())
    #ani = animation.FuncAnimation(fig, animate, interval=1000)
    #plt.show()

    """
    for phase in np.linspace(0, 10, 100):
        line1.set_ydata(np.sin(0.5 * x + phase))
        fig.canvas.draw()
        fig.canvas.flush_events()
    """
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
