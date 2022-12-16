from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
from PyQt5 import QtCore
import argparse

from helpers.fen_services import readFile, moveButton, cursor_CC
from helpers.fen_plot import graphTemplate, animation
from helpers.fen_txt import welcomeTxtFen2

parser = argparse.ArgumentParser(description="File for optimal equilibrium of chosen scenario sent from C")
parser.add_argument("--fileName", type=str, help="fichier C", default="in_C/results_python_file.txt")
parser.add_argument("--scenario", type=str, help="type of scenario chosen", default="eg")



def animate_f(k):
    """Called by main.
    Goal: Animated lines created step by step for the four variables.
    Args: k (int): frames """

    # Skipping frames
    s = k*skip
    
    animation(k, ax, t[:s], XC[:s], XE[:s], N[:s], W[:s], CC/mx_CC)

    # Displaying new informations at last frame
    if k==(time//skip)-1:
        cursor_CC(fen_princ, args.scenario)





if __name__=='__main__':
    """ Called by HANDY_calculs.c with arguments.
    This file is the second Tkinter interactive interface.
    Goals: Display animation of chosen scenario using datas sent by fen1.py and treated by HANDY_calculs.c.
           Animation to see four variables evoluate step by step.
           Display informations about the animation.
           Possibility to come back to fen1.py or definitely quit program.
           Ask user to chose parameters with cursors: D and K to produce personal modelisations.
           Send chosen parameters to HANDY_calculs.c to modelize in next window. 
           End by destroying window and C file continues.
    Args: args.fileName (str): path of file containing incremented datas with time.
          args.scenario (str): name of scenario to give accurate informations. """

    # Arguments passed by HANDY_calculs.c
    args = parser.parse_args()

    fen_princ = Tk()
    fen_princ.attributes('-fullscreen', True)
    fen_princ.configure(bg="azure")
    moveButton(fen_princ, 2, args.scenario)

    # Text according to chosen scenario in previous window
    title, text_welcome = 0, 0
    if args.scenario == "eg":
        title, text_welcome, CCtxt = welcomeTxtFen2("eg")
    if args.scenario == "eq":
        title, text_welcome, CCtxt = welcomeTxtFen2("eq")
    if args.scenario == "un":
        title, text_welcome, CCtxt = welcomeTxtFen2("un")
    titlelabel = Label(fen_princ, text=title, fg= 'mediumblue', bg="azure", font=('Yu Gothic',45, "bold")).pack()
    welcome_label = Label(fen_princ, text=text_welcome, fg= 'lightseagreen', bg="azure", borderwidth=3, relief="solid", font=('Yu Gothic',15, "bold"), justify=LEFT).place(x=25, y=135)
    CCtxtlabel = Label(fen_princ, text=CCtxt, fg= 'lightseagreen', bg="azure", borderwidth=3, relief="solid", font=('Yu Gothic',15, "bold")).place(x=110, y=230)

    # Modelisation for 1000 years, generating x-axis
    time = 1000
    t = [i for i in range(time)]

    # Stocking four variables and caryying capacity incremented by HANDY_calculs.c
    [XC, XE, N, W, variables, parameters] = readFile(args.fileName)
    CC = int(parameters[-1])

    # Calculated maximum carrying capacity with the adequate formula
    mx_CC = 75000

    # SELON SCENARIOOOOO MODIFIER
    # norm_CC = 1
    # norm_N = 4

    # Skipping variables values for the animation to be faster
    skip = 50
    
    # Creating graphic on plt
    fig, ax = plt.subplots(figsize=(3.95,2.5))
    fig.patch.set_facecolor('azure')

    # Add template to graph
    graphTemplate(ax, 1, 4)

    # Importing plt on Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=fen_princ)
    canvas.get_tk_widget().place(x=0, y=275)

    # Starting animation using frames
    ani = FuncAnimation(fig = fig, func = animate_f, frames = range(time//skip), interval = 1, repeat = False)

    # Display window
    fen_princ.mainloop()

