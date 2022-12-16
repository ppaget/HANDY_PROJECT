from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import argparse

from helpers.fen_services import readFile, moveButton, cursor_CC
from helpers.fen_plot import graphTemplate, animation
from helpers.fen_txt import welcomeTxtFen2

parser = argparse.ArgumentParser(description="File for optimal equilibrium of chosen scenario sent from C")
parser.add_argument("--fileName", type=str, help="fichier C", default="in_C/results_python_file.txt")
parser.add_argument("--scenario", type=str, help="type of scenario chosen", default="eg")


def animate_f(k):
    """Animate y-axis step by step for four variables.
    Args: k (int): frames """

    # Skipping frames
    s = k*skip

    # Calling function with adequate lists
    animation(k, ax, t[:s], XC[:s], XE[:s], N[:s], W[:s], CC)

    # Displaying new informations about CC at last frame
    if k==(time//skip)-1:
        cursor_CC(fen_princ, args.scenario)
        

if __name__=='__main__':
    """ Called by HANDY_calculs.c with arguments using argparse.
    Second Tkinter interactive interface.
    Goals: Display animation of chosen scenario using datas sent by fen1.py and treated by HANDY_calculs.c.
           Animation to see four variables evoluate over time.
           Ask user to chose CC to produce personal modelisations.
           Send chosen parameters to HANDY_calculs.c to modelize in next window. 
    Args: args.fileName (str): path of file.
          args.scenario (str): type of scenario. """

    # Arguments passed by HANDY_calculs.c
    args = parser.parse_args()

    # Creation of window
    fen_princ = Tk()
    fen_princ.attributes('-fullscreen', True)
    fen_princ.configure(bg="azure")
    moveButton(fen_princ, 2, args.scenario)

    # Displayed text according to scenario chosen in previous window
    # Recall of starting values and CC optimal
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

    # Stocking four variables and carying capacity
    [XC, XE, N, W, variables, parameters] = readFile(args.fileName)
    CC = float(parameters[-1])

    # Skipping variables values for the animation to be faster
    skip = 50
    
    # Creating graphic on plt
    fig, ax = plt.subplots(figsize=(3.95,2.5))
    fig.patch.set_facecolor('azure')

    # Add template to graph
    graphTemplate(ax, int(parameters[-3]), int(parameters[-2]))

    # Importing plt on Tkinter window with Canvas
    canvas = FigureCanvasTkAgg(fig, master=fen_princ)
    canvas.get_tk_widget().place(x=0, y=275)

    # Starting animation using frames
    ani = FuncAnimation(fig = fig, func = animate_f, frames = range(time//skip), interval = 1, repeat = False)

    # Display window
    fen_princ.mainloop()

