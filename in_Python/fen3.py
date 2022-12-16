from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import os
import argparse

from helpers.fen_services import readFile, moveButton
from helpers.fen_plot import graphTemplate, animation
from helpers.result_scenario import resultScenario
from helpers.fen_txt import remindersFen3

parser = argparse.ArgumentParser(description="File sent from C")
parser.add_argument("--fileCursors", type=str, help="fichier C", default="in_C/results_python_cursors.txt")
parser.add_argument("--fileBasic", type=str, help="type of scenario chosen", default="in_C/results_python_file.txt")
parser.add_argument("--scenario", type=str, help="type of scenario chosen", default="eg")


def animate_c(k, XC, XE, N, W):

    s = k*skip

    # Animation for second graph with chosen CC
    animation(k, ax[1], t[:s], XC[:s], XE[:s], N[:s], W[:s], CC_c)

    # At the end, displaying results and analysis of results
    if k==(time//skip)-1:
        title, explanation = resultScenario(XC, N)
        title_label = Label(fen_princ, text=title, bg="honeydew", font=('Yu Gothic',50, "bold"), borderwidth=4, relief="sunken")
        title_label.place(x=420, y=90)
        explanation_label= Label(fen_princ, text = explanation, fg= 'green', bg="honeydew", font=('Yu Gothic',28, "bold"), justify=RIGHT)
        explanation_label.place(x=750, y=170)



if __name__=='__main__':
    """ Called by HANDY_calculs.c with arguments using argparse.
    Third Tkinter interactive interface.
    Main works the same as Fen2.py PLEASE REFER TO IT.
    Goals: Display animation of chosen scenario + new animation with CC chosen in previous window
           Analyze results of personnal modelisation and comparaison with first graph
           Possibility to try again 
    Args: args.file (str): path of file (two: from first and cursor window)
          args.scenario (str): type of scenario. 
          """

    args = parser.parse_args()

    fen_princ = Tk()
    fen_princ.attributes('-fullscreen', True)
    fen_princ.configure(bg="honeydew")
    moveButton(fen_princ, 3, args.scenario)

    # Stocking four variables and carying capacity from both first and cursors file
    [XC_b, XE_b, N_b, W_b, variables, parameters_b] = readFile(args.fileBasic)
    [XC_c, XE_c, N_c, W_c, variables, parameters_c] = readFile(args.fileCursors)
    # Chosen CC
    CC_c = float(parameters_c[-1])

    # Displayed text according to scenario chosen in previous window
    # Recall of starting values and CC optimal and CC chosen
    title, reminder_f, reminderCC_f, newCC_c = 0, 0, 0, 0
    if args.scenario == "eg":
        title, reminder_f, reminderCC_f, newCC_c = remindersFen3("eg", CC_c)
    if args.scenario == "eq":
        title, reminder_f, reminderCC_f, newCC_c = remindersFen3("eq", CC_c)
    if args.scenario == "un":
        title, reminder_f, reminderCC_f, newCC_c = remindersFen3("un", CC_c)
    titlelabel = Label(fen_princ, text=title, fg= 'green', bg="honeydew", font=('Yu Gothic',45, "bold")).pack()
    reminder_f_label = Label(fen_princ, text=reminder_f, fg= 'mediumseagreen', bg="honeydew", borderwidth=3, relief="solid", font=('Yu Gothic',15, "bold"), justify=LEFT).place(x=25, y=125)
    CCtxtlabel = Label(fen_princ, text=reminderCC_f, fg= 'mediumseagreen', bg="honeydew", borderwidth=3, relief="solid", font=('Yu Gothic',15, "bold")).place(x=110, y=220)
    newCClabel = Label(fen_princ, text=newCC_c, fg= 'mediumseagreen', bg="honeydew", borderwidth=3, relief="solid", font=('Yu Gothic',15, "bold")).place(x=500, y=220)
    arrow= "→"
    arrowlabel = Label(fen_princ, text=arrow, fg= 'mediumseagreen', bg="honeydew", font=('Yu Gothic',40, "bold")).place(x=330, y=200)
    arrowlabel = Label(fen_princ, text=arrow, fg= 'mediumseagreen', bg="honeydew", font=('Yu Gothic',40, "bold")).place(x=380, y=200)
    arrowlabel = Label(fen_princ, text=arrow, fg= 'mediumseagreen', bg="honeydew", font=('Yu Gothic',40, "bold")).place(x=430, y=200)

    time = 1000
    t = [i for i in range(time-1)]
    skip = 50

    # Used to normalise axes
    x_factor = int(parameters_c[-3])
    w_factor = int(parameters_c[-2])

    # Given CC from file
    CC_b = float(parameters_b[-1])

    # Two axes
    fig, ax = plt.subplots(1, 2, figsize=(6.39,2.74), gridspec_kw={'width_ratios': [1, 1.5]})
    fig.patch.set_facecolor('honeydew')

    graphTemplate(ax[0], int(parameters_b[-3]), int(parameters_b[-2]))
    graphTemplate(ax[1], x_factor, w_factor)

    # Displaying immobil first graph
    animation(0, ax[0], t, XC_b, XE_b, N_b, W_b, CC_b)

    canvas = FigureCanvasTkAgg(fig, master=fen_princ)
    canvas.get_tk_widget().place(x=0, y=256)

    ani = FuncAnimation(fig = fig, func = animate_c, fargs = (XC_c,XE_c,N_c,W_c), frames = range(time//skip), interval = 1, repeat = False)
              
    fen_princ.mainloop()
