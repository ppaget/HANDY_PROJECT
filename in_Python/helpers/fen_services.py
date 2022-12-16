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

    quit_button = Button(fen_princ, text = "QUIT", command = lambda:quit(fen_princ)).place(x=1155, y=25)
    if n==2:
        home_button = Button(fen_princ, text = "HOME", command = lambda:backFen1(fen_princ)).place(x=1150, y=60)
    if n==3:
        home_button = Button(fen_princ, text = "HOME", command = lambda:backFen1(fen_princ)).place(x=1150, y=60)
        again_button = Button(fen_princ, text = "NEW VALUES", command = lambda:backFen2(fen_princ, scenario)).place(x=1130, y=95)

def cleanTk(w1, w2, w3):
    window = [w1, w2, w3]
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
    labeltxtCC= Label(fen_princ, text = txtCC)
    labeltxtCC.place(x=750, y=90)

    cursorCC = Scale(fen_princ, orient='horizontal', from_=0.0, to=1.0, digits = 2, resolution = 0.1)
    cursorCC.place(x=970, y=240)

    labelCC = Label(fen_princ, text = "CC: 0.0")
    labelCC.place(x=1000, y=280)
    
    buttonCC = Button(fen_princ, text = "VALIDATE CC", command = lambda:dispValue("CC",cursorCC,labelCC))
    buttonCC.place(x=940, y=320)

    buttonGO = Button(fen_princ, text = "MODELISE", command = lambda:sendCursors(fen_princ, scenario, cursorCC))
    buttonGO.place(x=950, y=360)

    hintstxt = hintsFen2(scenario)
    labelhints = Label(fen_princ, text = hintstxt, bg="lightgreen")
    labelhints.place(x=960, y=500)
        
