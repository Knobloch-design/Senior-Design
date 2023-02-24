# This is a sample Python script.

import socket
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import tkinter as tk

import random

matplotlib.use('Qt5Agg')


"""
Function Creates random Data to test with
"""
def randomData(x):
    return x + random.uniform(-5.0, 5.0)


#fig = plt.figure()
#ax1 = fig.add_subplot(1, 1, 1)
Celsius = True

tempScale  = "C"
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('172.17.30.81', 4000))
print(socket.gethostname())
server_socket.listen(1)
client_socket, address = server_socket.accept()
arr = []
max = 100
min = 0


def celcius_to_f(temp_c):
    return temp_c*(9/5)+32

def graph_F(event):
    global Celsius
    global tempScale
    global fig
    global ax1
    global arr
    arr = []
    Celsius = False
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    plt.ylim(50,122)
    tempScale = "F"
    anim = animation.FuncAnimation(fig, animate, interval=1000)
    plt.draw()
    plt.show()


def graph_C(event):
    global Celsius
    global tempScale
    global fig
    global ax1
    global arr
    arr = []
    Celsius = True
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    plt.ylim(10,50)
    tempScale = "C"
    anim = animation.FuncAnimation(fig, animate, interval=1000)
    plt.draw()
    plt.show()


def animate(i):

    data = client_socket.recv(1024)
    print(data)
    if (data.decode('utf-8') == ''):
        #client_socket.close()
        #the lab manual says if I don't get data I should leave a null space in the graph
        data = '000.000'
    if Celsius == False:
        data = celcius_to_f(eval(data[:5]))
    else:
        data = eval(data[:5])
    arr.append(data)

    ax1.plot(arr)

    plt.xlabel("Time (sec)")
    plt.ylabel("Temp ("+tempScale+")")
    plt.title("Temperature vs Time")


"""
this function runs when the power button is pressed
"""
def LCDPower():
    return None

"""
this function runs when the 'Set MAX' Button is pressed
 """
def maxButtonPress(self):
    global max
    temp =Tmax.get(0.0, "end-1c")
    max  = eval(temp)
    print(max)

"""
this function runs when the 'Set MIN' Button is pressed
"""
def minButtonPress(self):
    global min
    temp = Tmin.get(0.0,"end-1c")
    min = eval(temp)
    print(min)




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

    greeting = tk.Label(text=SensorStatus)
    greeting.grid(row =0, column=0)
    #frame = tk.Frame(master=window, height=200, width=200)
    labelBox = tk.Label(text=BoxStatus)
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
    LCDButton = tk.Button(
        text="LCD Power",
        width=10,
        height=5,
        bg="Blue",
        fg="White",
    )

    maxLabel = tk.Button(text="Set MAX")
    Tmax = tk.Text(height=2, width=20)
    minLabel = tk.Button(text="Set MIN")
    Tmin = tk.Text(height=2, width=20)
    FButton.bind("<Button-1>", graph_F)
    CButton.bind("<Button-1>", graph_C)
    LCDButton.bind("<Button-1>", LCDPower)
    maxLabel.bind("<Button-1>", maxButtonPress)
    minLabel.bind("<Button-1>", minButtonPress)


    #I think we need 1 number in the GUI that just displays the current temp
    #This will only run once
    data = client_socket.recv(1024)
    currentTemp = tk.Label(text=data[0:5])

    currentTemp.grid(row=0, column=0)
    labelBox.grid(row =1, column=0)
    greeting.grid(row =2, column=0)
    maxLabel.grid(row=0, column=3)
    Tmax.grid(row=1,column=3)
    minLabel.grid(row=2, column=3)
    Tmin.grid(row=3,column=3)
    FButton.grid(row=1, column=1)
    CButton.grid(row=2, column=1)
    LCDButton.grid(row=1, column=2)
    window.mainloop() #blocks code after it till the window is closed



