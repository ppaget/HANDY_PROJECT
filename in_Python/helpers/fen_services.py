# Helper for Tkinter windows.

import numpy as np
import os
from tkinter import *

from helpers.fen_os import sendCursors
from helpers.fen_txt import descrCCFen2, hintsFen2

def quit(fen_princ:Tk):
    """Immediately ends program by destroying window.

    Args:
        fen_princ (Tk): displayed window.
    """

    fen_princ.destroy()

def backFen1(fen_princ:Tk):
    """Back to window 1, Fen1.

    Args:
        fen_princ (Tk): displayed window.
    """

    os.system("python in_Python/fen1.py")
    fen_princ.destroy()

def backFen2(fen_princ:Tk, scenario:str):
    """ BAack to window 2, Fen2.

    Args:
        fen_princ (Tk): displayed window.
        scenario (str): type of scenario.
    """

    if scenario == "eg" :
        os.system("python in_Python/fen2.py --fileName in_C/results_python_file.txt --scenario eg")
    if scenario == "eq" :
        os.system("python in_Python/fen2.py --fileName in_C/results_python_file.txt --scenario eq")
    if scenario == "un" :
        os.system("python in_Python/fen2.py --fileName in_C/results_python_file.txt --scenario un")
    fen_princ.destroy()

def moveButton(fen_princ:Tk, n:int,  scenario:str):
    """Buttons always displayed on right top to move from
    window to another.

    Args:
        fen_princ (Tk): displayed window.
        n (int): number of actual window.
        scenario (str): type of scenario.
    """

    quit_button = Button(fen_princ, text = "QUIT", borderwidth=0, bg="lightcoral",command = lambda:quit(fen_princ)).place(x=1155, y=25)
    if n==2:
        home_button = Button(fen_princ, text = "HOME", bg='lightskyblue',command = lambda:backFen1(fen_princ)).place(x=1150, y=60)
    if n==3:
        home_button = Button(fen_princ, text = "HOME", bg="navajowhite",command = lambda:backFen1(fen_princ)).place(x=1150, y=60)
        again_button = Button(fen_princ, text = "NEW VALUES",bg='lightgreen', command = lambda:backFen2(fen_princ, scenario)).place(x=1130, y=95)

def cleanTk(w1, w2, w3, w4):
    """Cleans window from old widgets.

    Args: widgets displayed
    """

    window = [w1, w2, w3, w4]
    for i in window :
        if i != None: i.destroy()

def readFile(fname:str):
    """Read file sent by HANDY_calculs.c.
    Args: fname (str): file contains variables incremented with time according to Handy Model equations.
    Returns: list: four lists corresponding to each variable.
             header: variables at t=0 and fixed parameters.
    """

    # For variables datas
    array = np.genfromtxt(fname, delimiter=', ', skip_header=3, dtype=float)
    XC = array[:,0]
    XE = array[:,1]
    N = array[:,2]
    W = array[:,3]
    # For header
    f = open(fname, "r")
    variables = [f.readline()]
    variables = variables[0].split(", ")
    parameters = [f.readline()]
    parameters = parameters[0].split(", ")
    
    return [XC, XE, N ,W, variables, parameters]

def dispValue(fen_princ:Tk, cursor:Tk, label:Tk):
    """Displays value for cursors.

    Args:
        fen_princ (str): displayed window.
        cursor (Tk): given cursor.
        label (Tk): label to change.
    """

    value = "CC: " + str(cursor.get())
    label.configure(text= value)

def cursor_CC(fen_princ:Tk, scenario:str):
    """Displays explanation, hints and cursor for Carrying Capacity.
    Button MODELIZE is a path to go to HANDY_calculs.c.

    Args:
        fen_princ (Tk): displayed window.
        scenario (str): type of scenario.
    """

    # Explanation
    txtCC = descrCCFen2()
    labeltxtCC= Label(fen_princ, text = txtCC, fg= 'steelblue', bg="azure", font=('Yu Gothic',40, "bold"), justify=LEFT)
    labeltxtCC.place(x=750, y=150)

    cursorCC = Scale(fen_princ, orient='horizontal', from_=0.1, to=1.0,resolution=0.1,digits = 2, width=60, length=300, bg="azure")
    cursorCC.place(x=850, y=410)

    labelCC = Label(fen_princ, text = "CC: 0.1", font=('Yu Gothic',10, "bold"))
    labelCC.place(x=850, y=500)
    
    # Displays current value of cursor
    buttonCC = Button(fen_princ, text = "VALIDATE CC", fg= 'steelblue', bg="azure", font=('Yu Gothic',20, "bold"), command = lambda:dispValue(fen_princ,cursorCC,labelCC))
    buttonCC.place(x=910, y=550)
    
    # Leads to HANDY_calculs.c
    buttonGO = Button(fen_princ, text = "MODELIZE", fg= 'mediumblue', bg="azure", font=('Yu Gothic',40, "bold"),command = lambda:sendCursors(fen_princ, scenario, cursorCC.get()))
    buttonGO.place(x=900, y=650)

    # Hints to chose interesting value for CC
    hintstxt = hintsFen2(scenario)
    labelhints = Label(fen_princ, text = hintstxt, fg= 'lightseagreen', bg="azure", borderwidth=3, relief="solid", font=('Yu Gothic',15, "bold"), justify=LEFT)
    labelhints.place(x=1140, y=220)

        
