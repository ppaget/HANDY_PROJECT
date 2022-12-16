from tkinter import *

from helpers.fen_os import sendScenario
from helpers.fen_services import moveButton, cleanTk
from helpers.fen_txt import welcomeTxtFen1, question1Fen1, summaryTxtFen1, question2Fen1

def startScenario(scenario:str, w1, w2, w3):
    
    if scenario=="eg":
        cleanTk(w1, w2, w3)
    if scenario=="eq" or scenario=="un":
        cleanTk(w1,w2,w3)

    summaryTxt = summaryTxtFen1(scenario)
    startlabel = Label(fen_princ, text = summaryTxt)
    startlabel.pack()
    startbutton = Button(fen_princ, text = "START!", command = lambda : sendScenario(fen_princ, scenario))
    startbutton.pack()

def questionK(w1,w2,w3):
    """ Activated by button.
    Goal: Ask second question about inequality factor to lead either to equitable or unequal scenario. """

    cleanTk(w1,w2,w3)

    question2 = question2Fen1()

    q2_label = Label(fen_princ, text = question2)
    q2_label.pack()
    eq_button = Button(fen_princ, text = "YES", command = lambda:startScenario("eq",q2_label, eq_button, un_button))
    eq_button.pack()
    un_button = Button(fen_princ, text = "NO", command = lambda:startScenario("un",q2_label, eq_button, un_button))
    un_button.pack()

def questionXE(w1, w2):
    """ Activated by button.
    Goal: Ask first question about elite population to lead either to egalitarian scenario or second question. """

    cleanTk(w1, w2, None)

    question1 = question1Fen1()

    q1_label = Label(fen_princ, text = question1)
    q1_label.pack()
    XE_button = Button(fen_princ, text = "YES", command = lambda:questionK(q1_label, XE_button, eg_button))
    XE_button.pack()
    eg_button = Button(fen_princ, text = "NO", command = lambda:startScenario("eg", q1_label, XE_button, eg_button))
    eg_button.pack()

def introduction():
    """ First welcoming window.
    Goals: Explain main goals of the model
           Explain variables and parameters
           Start the interactive interface """

    welcomeTxt = welcomeTxtFen1()

    welcome_label = Label(fen_princ, text = welcomeTxt)
    welcome_label.pack()
    go_button = Button(fen_princ, text = "GO!", command = lambda:questionXE(welcome_label, go_button))
    go_button.pack()


if __name__=='__main__':
    """ Called by RUN_HANDY.
    This file is the first Tkinter interactive interface.
    Goals: Contain explanations of project
           Ask questions to user to lead to one of three scenarios: egalitarian, equitable or unequal.
           Send file containing initial datas for chosen scenario to HANDY_calculs.c to modelize datas in next window.
           Three sets of datas lead to optimal equilibrium.
           Possibility to definitely quit program. 
           End by destroying window and C file continues. """

    # Creation of Tkinter window
    fen_princ = Tk()
    fen_princ.attributes('-fullscreen', True)

    # Button to quit
    moveButton(fen_princ, 1, "")

    # Only one function called because buttons call functions themselves
    introduction()

    # Displays the first window
    fen_princ.mainloop()