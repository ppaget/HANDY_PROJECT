from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time
from tkinter import *


def readFile(fname):

    array = np.genfromtxt(fname, delimiter=', ', skip_header=3, dtype=float)
    XC = array[:,0]
    XE = array[:,1]
    N = array[:,2]
    W = array[:,3]
    f = open(fname, "r")
    variables = [f.readline()]
    variables = variables[0].split(", ")
    parameters = [f.readline()]
    parameters = parameters[0].split(", ")
    
    return [XC, XE, N ,W, variables, parameters]

def print_d() :
    text_d = "d : " + str(curseurd.get())
    d_label.configure(text= text_d)

def sendCursors():
    text = curseurd.get()
    c_label = Label(fen_princ, text = text, width=70).grid(row=8, column=1)

if __name__=='__main__':
    fen_princ = Tk()
    curseurd = Scale(fen_princ, orient='horizontal', from_=5, to=100, resolution = 5)
    curseurd.grid(row=4, column=1)
    d_label = Label(fen_princ, text = "Value for d", width=70)
    d_label.grid(row=5, column=1)
    monBoutond = Button(fen_princ, text = "Validate value for D", command = print_d).grid(row=6, column=1)
    monBoutongo = Button(fen_princ, text = "Launch scenario", command = sendCursors).grid(row=7, column=1)

    fen_princ.mainloop()
