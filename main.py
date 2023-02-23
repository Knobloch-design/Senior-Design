  # This is a sample Python script.
import sys

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

import time
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure




def randomData(x):
    return x + random.uniform(-5.0,5.0)


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
class Table:

    conn = sqlite3.connect('DataBase.sqlite')
    cur = conn.cursor()

    #cur.execute('DROP TABLE IF EXISTS temperature')

    """
    Function creates temperature table as well as creates the columns id and temp_c
    """
    def init(self):
        print("hello world")
        self.cur.execute('CREATE TABLE IF NOT EXISTS temperature (Id INTEGER PRIMARY KEY,temp_c REAL)')
        #self.cur.execute('ALTER TABLE temperature ADD COLUMN Temp FLOAT')  # Add new column to table


        #code here creates test data to fill sql table

        xar = [i for i in range(1, 101)]
        yar = [randomData(i) for i in [30] * 300]

        for i in xar:
            self.cur.execute('INSERT INTO temperature (temp_c) VALUES ('+str(yar[i])+')')




fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
xar = [i for i in range(1, 101)]
yar = [randomData(i) for i in [70] * 100]
x= []
y= []
count = 0
test = Table
Table.init(test)


def getNext():
    global count
    x = xar[0:count]
    y = yar[0:count]
    print(x)
    print(y)

    return (x,y)


def animate(i):

    global Table

    Table.cur.execute('SELECT Id FROM temperature')
    Id = Table.cur.fetchall()
    Table.cur.execute('SELECT temp_c FROM temperature')
    temp = Table.cur.fetchall()

    ax1.clear()
    ax1.plot(Id[:i], temp[:i])
    plt.ylim(1, 100)
    plt.xlabel("Time (sec)")
    plt.ylabel("Temp (F)")
    plt.title("Temperature vs Time")





# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()


    """
    for phase in np.linspace(0, 10, 100):
        line1.set_ydata(np.sin(0.5 * x + phase))
        fig.canvas.draw()
        fig.canvas.flush_events()
    """
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
