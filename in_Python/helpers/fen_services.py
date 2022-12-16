import numpy as np
import matplotlib.pyplot as plt
import os
from tkinter import *

from helpers.fen_os import sendCursors
from helpers.fen_txt import descrCCFen2, hintsFen2

def quit(fen_princ):
    """ Activated by button.
    Goal: Quit interface and end running of program. """
    fen_princ.destroy()

def backFen1(fen_princ):
    os.system("python in_Python/fen1.py")
    fen_princ.destroy()

def backFen2(fen_princ, scenario:str):
    if scenario == "eg" :
        os.system("python in_Python/fen2.py --fileName in_C/results_python_file.txt --scenario eg")
    if scenario == "eq" :
        os.system("python in_Python/fen2.py --fileName in_C/results_python_file.txt --scenario eq")
    if scenario == "un" :
        os.system("python in_Python/fen2.py --fileName in_C/results_python_file.txt --scenario un")
    fen_princ.destroy()

def moveButton(fen_princ, n,  scenario):

    quit_button = Button(fen_princ, text = "QUIT", borderwidth=0, bg="lightcoral",command = lambda:quit(fen_princ)).place(x=1155, y=25)
    if n==2:
        home_button = Button(fen_princ, text = "HOME", bg='lightskyblue',command = lambda:backFen1(fen_princ)).place(x=1150, y=60)
    if n==3:
        home_button = Button(fen_princ, text = "HOME", bg="navajowhite",command = lambda:backFen1(fen_princ)).place(x=1150, y=60)
        again_button = Button(fen_princ, text = "NEW VALUES",bg='lightgreen', command = lambda:backFen2(fen_princ, scenario)).place(x=1130, y=95)

def cleanTk(w1, w2, w3, w4):
    window = [w1, w2, w3, w4]
    for i in window :
        if i != None: i.destroy()

def readFile(fname:str):
    """Called by main function.
    Goal: Read file sent by HANDY_calculs.c.
    Args: fname (str): file contains variables incremented with time according to Handy Model equations.
    Returns: list: four lists corresponding to each variable.
    """
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

def dispValue(param: str, cursor, label):
    """Displays value for cursors.

    Args:
        param (str): _description_
        cursor (_type_): _description_
        label (_type_): _description_
    """
    value = param + ": " + str(cursor.get())
    label.configure(text= value)

def cursor_CC(fen_princ, scenario):

    txtCC = descrCCFen2()
    labeltxtCC= Label(fen_princ, text = txtCC, fg= 'steelblue', bg="azure", font=('Yu Gothic',40, "bold"), justify=LEFT)
    labeltxtCC.place(x=750, y=150)

    cursorCC = Scale(fen_princ, orient='horizontal', from_=0.1, to=1.0, digits = 2, resolution = 0.1, width=60, length=300, bg="azure")
    cursorCC.place(x=850, y=410)

    labelCC = Label(fen_princ, text = "CC: 0.1", font=('Yu Gothic',10, "bold"))
    labelCC.place(x=850, y=500)
    
    buttonCC = Button(fen_princ, text = "VALIDATE CC", fg= 'steelblue', bg="azure", font=('Yu Gothic',20, "bold"), command = lambda:dispValue("CC",cursorCC,labelCC))
    buttonCC.place(x=910, y=550)

    buttonGO = Button(fen_princ, text = "MODELIZE", fg= 'mediumblue', bg="azure", font=('Yu Gothic',40, "bold"),command = lambda:sendCursors(fen_princ, scenario, cursorCC))
    buttonGO.place(x=900, y=650)

    hintstxt = hintsFen2(scenario)
    labelhints = Label(fen_princ, text = hintstxt, fg= 'lightseagreen', bg="azure", borderwidth=3, relief="solid", font=('Yu Gothic',15, "bold"), justify=LEFT)
    labelhints.place(x=1140, y=220)
        
