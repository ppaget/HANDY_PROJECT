from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import os
from time import sleep
import argparse

parser = argparse.ArgumentParser(description="File sent from C")
parser.add_argument("--fileCursors", type=str, help="fichier C", default="../in_C/results_python_cursors.txt")
parser.add_argument("--fileBasic", type=str, help="type of scenario chosen", default="../in_C/results_python_file.txt")
parser.add_argument("--scenario", type=str, help="type of scenario chosen", default="egalitarian")

def backFen1():
    os.system("python ../in_Python/fen1.py")
    fen_princ.destroy()
def backFen2():
    if args.scenario == "egalitarian" :
        os.system("python ../in_Python/fen2.py --fileName ../in_C/results_python_file.txt --scenario egalitarian")
    if args.scenario == "equitable" :
        os.system("python ../in_Python/fen2.py --fileName ../in_C/results_python_file.txt --scenario equitable")
    if args.scenario == "unequal" :
        os.system("python ../in_Python/fen2.py --fileName ../in_C/results_python_file.txt --scenario unequal")
              
    fen_princ.destroy()
def quit():
    fen_princ.destroy()

def analysis_results(nbr):

    end = []
    if nbr == 1:
        end.append("a TYPE-N COLLAPSE")
    if nbr == 2:
        end.append("a TYPE-L COLLAPSE")
    if nbr == 3:
        end.append("REVERSIBLE TYPE-N COLLAPSES")
    if nbr == 4:
        end.append("an EQUILIBRIUM")

    result_text = """Your modelisation leads to :\n""" + end[0]
    result_label= Label(fen_princ, text = result_text, width=70).grid(row= 0,column=1)


    again_button = Button(fen_princ, text = "Chose new values", command = backFen2).grid(row=7, column=1)
    end_button = Button(fen_princ, text = "Quit Model", command = quit).grid(row=8, column=1)


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

def animate_c(k, XC, XE, N, W):

    s = k*skip

    ax[1].plot(t[:s], XC[:s], color = 'b', label = "Commoner population")
    ax[1].plot(t[:s], XE[:s], color = 'r', label = "Elite population")
    ax[1].plot(t[:s], N[:s], color = 'g', label = "Nature")
    ax[1].plot(t[:s], W[:s], color = 'k', label = "Wealth")

    if k==(time//skip)-1:
        scenario = 0
        zero = float(0)
        if zero in N :
            result = np.where(N==zero)
            i0 = result[0][0] #4 de différence car on a rajouté 2 lignes

            M = max(N[i0+1:])
            iM = np.where(N==M)[0][0]

            if zero in XC[i0+1:iM+10] :
                scenario = 3
            elif N[998]==0 :
                scenario = 1
            else :
                scenario = 4
        else :
            if XC[998]<=0.1 : #Valeur de seuil car on ne voit pas totalement la collapse dans le uneq_1
                scenario = 2
            else : 
                scenario = 4

        analysis_results(scenario) #en argument scenario

def cursorsEg():
    text_welcome = """EGALITARIAN MODELISATION WITH CHOICES\n
                    No elite. Choices for d."""
    return text_welcome
def cursorsEq():
    text_welcome = """WELCOME TO YOUR EGALITARIAN MODELISATION\n
                    Elites. Choices for d."""
    return text_welcome
def cursorsUn():
    text_welcome = """WELCOME TO YOUR EGALITARIAN MODELISATION\n
                    Elites. Choices for k and d."""
    return text_welcome



if __name__=='__main__':

    args = parser.parse_args()
    fen_princ = Tk()
    fen_princ.attributes('-fullscreen', True)

    text_welcome = []
    if args.scenario == "egalitarian" :
        text_welcome.append(cursorsEg())
    if args.scenario == "equitable" :
        text_welcome.append(cursorsEq())
    if args.scenario == "unequal" :
        text_welcome.append(cursorsUn())

    welcome_label = Label(fen_princ, text = text_welcome[0], width=70).grid(row= 0,column=0)
    home_button = Button(fen_princ, text = "Back to Home", command = backFen1).grid(row=1)

    time = 1000
    skip = 20

    [XC_b, XE_b, N_b, W_b, variables, parameters] = readFile(args.fileBasic)
    [XC_c, XE_c, N_c, W_c, variables, parameters] = readFile(args.fileCursors)
    t = [i for i in range(time-1)]

    interface, ax = plt.subplots(1, 2, figsize=(6,2.6), gridspec_kw={'width_ratios': [1, 1.5]})

    ax[0].set_xlim(-20, 1020)
    ax[0].set_ylim(-0.03, 1.03)
    ax[0].tick_params(axis='x', labelsize=5)
    ax[0].tick_params(axis='y', labelsize=5)

    ax[0].plot(t, XC_b, color = 'b', label = "Commoner population")
    ax[0].plot(t, XE_b, color = 'r', label = "Elite population")
    ax[0].plot(t, N_b, color = 'g', label = "Nature")
    ax[0].plot(t, W_b, color = 'k', label = "Wealth")
    
    ax[0].legend(loc='upper left', bbox_to_anchor=(0.25, -0.06),
        fancybox=True, shadow=True, ncol=4, fontsize='xx-small')

    ax[1].set_xlim(-20, 1020)
    ax[1].set_ylim(-0.03, 1.03)
    ax[1].tick_params(axis='x', labelsize=5)
    ax[1].tick_params(axis='y', labelsize=5)

    canvas = FigureCanvasTkAgg(interface, master=fen_princ)
    canvas.get_tk_widget().place(x=-0.9, y=250)

    ani = FuncAnimation(fig = interface, func = animate_c, fargs = (XC_c,XE_c,N_c,W_c), frames = range(time//skip), interval = 1, repeat = False)
       
    fen_princ.mainloop()
