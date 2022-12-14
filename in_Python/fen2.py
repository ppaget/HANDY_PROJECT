from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import os
import argparse

parser = argparse.ArgumentParser(description="File sent from C")
parser.add_argument("--fileName", type=str, help="fichier C", default="../in_C/results_python_file.txt")
parser.add_argument("--scenario", type=str, help="type of scenario chosen", default="egalitarian")


def backFen1():
    os.system("python ../in_Python/fen1.py")
    fen_princ.destroy()
def quit():
    fen_princ.destroy()

def sendCursors():
    scenario_cursors = []
    k = []
    if args.scenario == "egalitarian" :
        scenario_cursors.append("eg_c")
        k.append("no change")
    if args.scenario == "equitable" :
        scenario_cursors.append("eq_c")
        k.append("no change")
    if args.scenario == "unequal" :
        scenario_cursors.append("un_c")
        k.append(str(curseurk.get()))

    d = str(curseurd.get())

    variables = [scenario_cursors[0], k[0], d]
    # os.chdir("in_C")
    os.system("gcc HANDY_calculs.c -o handy_calculs_exe")
    os.system("./handy_calculs_exe " + variables[0] + " " + variables[1] + " " + variables[2])

    fen_princ.destroy()

def print_k() :
    text_k = "K: " + str(curseurk.get())
    k_label.configure(text= text_k)
def print_d() :
    text_d = "D: " + str(curseurd.get())
    d_label.configure(text= text_d)

def cursors():
    global curseurk
    global k_label
    global curseurd
    global d_label

    home_button = Button(fen_princ, text = "Back to Home", command = backFen1).grid(row=0, column=1)
    end_button = Button(fen_princ, text = "Quit Model", command = quit).grid(row=1, column=1)

    if args.scenario == "egalitarian" or args.scenario == "equitable" :
        next_graph_label= Label(fen_princ, text = "You can now chose a starting parameter : the Depletion per Capita, D.").grid(row= 2,column=1)

        curseurd = Scale(fen_princ, orient='horizontal', from_=0.5, to=20.0, digits = 4, resolution = 0.10)
        curseurd.grid(row=4, column=1)
        d_label = Label(fen_princ, text = "D: 0.50")
        d_label.grid(row=5, column=1)
        monBoutond = Button(fen_princ, text = "Validate value for D", command = print_d).grid(row=6, column=1)
        
        monBoutongo = Button(fen_princ, text = "Launch scenario", command = sendCursors).grid(row=7, column=1)

        
    if args.scenario == "unequal" :
        next_graph_label= Label(fen_princ, text = "You can now chose two starting parameters: the Depletion per Capita, D and the inequality factor, K.", width=70).grid(row= 3,column=1)

        curseurd = Scale(fen_princ, orient='horizontal', from_=0.5, to=20.0, digits = 4, resolution = 0.10)
        curseurd.grid(row=4, column=1)
        d_label = Label(fen_princ, text = "D: 0.50")
        d_label.grid(row=5, column=1)
        monBoutond = Button(fen_princ, text = "Validate value for D", command = print_d).grid(row=6, column=1)

        curseurk = Scale(fen_princ, orient='horizontal', from_=5, to=100, resolution = 5)
        curseurk.grid(row=7, column=1)
        k_label = Label(fen_princ, text = "K: 5")
        k_label.grid(row=8, column=1)
        monBoutonk = Button(fen_princ, text = "Validate value for K", command = print_k).grid(row=9, column=1)
        
        monBoutongo = Button(fen_princ, text = "Launch scenario", command = sendCursors).grid(row=11, column=1)

        # home_button = Button(fen_princ, text = "Back to Home", command = backFen1).grid(row=9, column=1)
        # end_button = Button(fen_princ, text = "Quit Model", command = quit).grid(row=10, column=1)



def animate(k):
    """Called by main.
    Goal: Animated lines created step by step for the four variables.
    Args: k (int): frames """

    # Skipping frames
    s = k*skip
    
    # Displaying legend once
    if k==0:
        ax.legend(loc='upper left', bbox_to_anchor=(-0.15, -0.06),
        fancybox=True, shadow=True, ncol=4, fontsize='xx-small')

    # Plotting lines from beginning
    ax.plot(t[:s], XC[:s], color = 'b', label = "Commoner population")
    ax.plot(t[:s], XE[:s], color = 'r', label = "Elite population")
    ax.plot(t[:s], N[:s], color = 'g', label = "Nature")
    ax.plot(t[:s], W[:s], color = 'k', label = "Wealth")

    # Displaying new informations at last frame
    if k==(time//skip)-1:
        cursors()

def readFile(fname):
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

def welcomeTxt(scenario):
    """ Called by main function.
    Goal: Generate text to explain variables and parameters of chosen scenario.
    Args : scenario (str): name of scenario to select corresponding text.
    Returns: text_welcome: corresponding text. """

    if scenario == "egalitarian":
        text_welcome = """
                    WELCOME TO YOUR EGALITARIAN SCENARIO!

                    Here is the modelisation which results in a soft-landing to OPTIMAL EQUILIBRIUM.

                    Used values:
                        - Commoner population: 100
                        - Elite population: 0

                        - Inequality factor: 0 
                        - Depletion per capita: D_reference

                    All other values are typical.
                    D_reference is the minimum consumption to go with the egalitarian scenario.
                        """
        return text_welcome

    if scenario == "equitable":
        text_welcome = """
                WELCOME TO YOUR EQUITABLE SCENARIO!

                Here is the modelisation which results in a soft-landing to OPTIMAL EQUILIBRIUM.

                Used values:
                    - Commoner population: 100
                    - Elite population: 25

                    - Inequality factor: 1 
                    - Depletion per capita: D_reference*1.25
                    
                All other values are typical.
                D_reference is the minimum consumption to go with the egalitarian scenario.
                    """
        return text_welcome

    if scenario == "unequal":
        text_welcome = """
                WELCOME TO YOUR UNEQUAL SCENARIO!

                Here is the modelisation which results in a soft-landing to OPTIMAL EQUILIBRIUM.

                Used values:
                    - Commoner population: 10 000
                    - Elite population: 3 000
                    - Commoner birth rate: 0.0065 (other scenarios: 0.03)
                    - Elite birth rate: 0.02 (other scenarios: 0.03)

                    - Inequality factor: 10 
                    - Depletion per capita: D_reference*0.95
                    
                All other values are typical.
                D_reference is the minimum consumption to go with the egalitarian scenario.
                    """
        return text_welcome


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

    # Text according to chosen scenario in previous window
    text_welcome = []
    if args.scenario == "egalitarian" :
        text_welcome.append(welcomeTxt("egalitarian"))
    if args.scenario == "equitable" :
        text_welcome.append(welcomeTxt("equitable"))
    if args.scenario == "unequal" :
        text_welcome.append(welcomeTxt("unequal"))
    welcome_label = Label(fen_princ, text = text_welcome[0]).grid(row= 0,column=0)

    # Modelisation for 1000 years, generating x-axis
    time = 1000
    t = [i for i in range(time)]

    # Skipping values for the animation to be faster
    skip = 20
    
    # Stocking four variables incremented by HANDY_calculs.c
    [XC, XE, N, W] = readFile(args.fileName)
    
    # Creating graphic on plt
    interface, ax = plt.subplots(figsize=(3.8,2.5))
    # Setting limits and resizing scale-axis
    ax.set_xlim(-20, 1020)
    ax.set_ylim(-0.03, 1.03)
    ax.tick_params(axis='x', labelsize=5)
    ax.tick_params(axis='y', labelsize=5)

    # Importing plt on Tkinter window
    canvas = FigureCanvasTkAgg(interface, master=fen_princ)
    canvas.get_tk_widget().place(x=0, y=270)

    # Starting animation using frames
    ani = FuncAnimation(fig = interface, func = animate, frames = range(time//skip), interval = 1, repeat = False)

    # Display window
    fen_princ.mainloop()

