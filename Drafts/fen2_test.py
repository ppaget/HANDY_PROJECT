from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import os
import argparse

parser = argparse.ArgumentParser(description="File sent from C")
parser.add_argument("--fileName", type=str, help="fichier C", default="in_C/results_python_file.txt")
parser.add_argument("--scenario", type=str, help="type of scenario chosen", default="egalitarian")


def backFen1():
    os.system("python ../in_Python/fen1.py")
    fen_princ.destroy()
def quit():
    fen_princ.destroy()

def sendCursors():

    if args.scenario == "egalitarian" or args.scenario == "equitable" :
        if args.scenario == "egalitarian":
            variables = ["eg_c", str(curseurd.get())]
            os.system("gcc HANDY_calculs.c -o handy_calculs_exe")
            os.system("./handy_calculs_exe " + variables[0] + " " + variables[1])
            
        else:
            variables = ["eq_c", str(curseurd.get())]
            os.system("gcc HANDY_calculs.c -o handy_calculs_exe")
            os.system("./handy_calculs_exe " + variables[0] + " " + variables[1])
    else:
        variables = ["un_c", str(curseurd.get()), str(curseurk.get()), str(curseurxe.get())]
        os.system("gcc HANDY_calculs.c -o handy_calculs_exe")
        os.system("./handy_calculs_exe " + variables[0] + " " + variables[1] + " " + variables[2] + " " + variables[3])

    # os.chdir("in_C")
    

    fen_princ.destroy()

def print_d() :
    text_d = "d: " + str(curseurd.get())
    d_label.configure(text= text_d)
def print_k() :
    text_k = "K: " + str(curseurk.get())
    k_label.configure(text= text_k)
def print_xe() :
    text_xe = "XE(0): " + str(curseurxe.get())
    d_label.configure(text= text_xe)

def cursors():
    global curseurk
    global k_label
    global curseurd
    global d_label
    global curseurxe
    global xe_label

#     if args.scenario == "egalitarian" or args.scenario == "equitable" :
#         end_button = Button(fen_princ, text = "Quit Model", command = quit).place(x=1155, y=25)
#         home_button = Button(fen_princ, text = "Back to Home", command = backFen1).place(x=1150, y=60)
        
#         text_d = """
#         You can now chose to vary a starting parameter:
#             the Depletion per Capita, D.

#         It represents how much Commoners will take ressources from Nature.
#         High D means high exploitation.
#         Chose d: d*D_reference = D.
#         """
#         next_graph_label= Label(fen_princ, text = text_d).place(x=750, y=90)

#         curseurd = Scale(fen_princ, orient='horizontal', from_=0.50, to=20.00, digits = 4, resolution = 0.05)
#         curseurd.place(x=970, y=240)
#         d_label = Label(fen_princ, text = "d: 0.5")
#         d_label.place(x=1000, y=280)
#         monBoutond = Button(fen_princ, text = "Validate value for d", command = print_d).place(x=940, y=320)
#         monBoutongo = Button(fen_princ, text = "Launch scenario", command = sendCursors).place(x=950, y=360)

#         if args.scenario == "egalitarian":
#             hints_eg = """
# Hints:
# You could try with:
#     d = 2.5
#     d = 4
#     d = 5.5
#             """
#             next_graph_label= Label(fen_princ, text = hints_eg, bg="lightgreen").place(x=960, y=500)

#         else:
#             hints_eq = """
# Hints:
# You could try with:
#     d = 2.6
#     d = 3.5
#     d = 5
#             """
#             next_graph_label= Label(fen_princ, text = hints_eq, bg="lightgreen").place(x=960, y=500)         

        
    if True==1:
        end_button = Button(fen_princ, text = "Quit Model", command = quit).place(x=1155, y=25)
        home_button = Button(fen_princ, text = "Back to Home", command = backFen1).place(x=1150, y=60)
        text_d = """
    You can now chose to vary two starting parameters
    and an initial variable:
        the Depletion per Capita, D
        the Inequality Factor, K
        the initial Elite Population, XE(0)

    D represents how much Commoners will take ressources from Nature.
    High D means high exploitation.
    Chose d: d*D_reference = D.

    K represents the factor between Commoners and Elites salaries.
    High K means high difference in salaries.

    XE(0) represents the number of non-workers at beginning.
    High XE(0) means high exploitation of ressources to carry 
    high population.
    """
        next_graph_label= Label(fen_princ, text = text_d).place(x=800, y=100)

        curseurd = Scale(fen_princ, orient='horizontal', from_=0.50, to=20.00, digits = 4, resolution = 0.05)
        curseurd.place(x=900, y=400)
        d_label = Label(fen_princ, text = "d: 0.5")
        d_label.place(x=930, y=440)
        monBoutond = Button(fen_princ, text = "Validate value for d", command = print_d).place(x=800, y=480)

        curseurk = Scale(fen_princ, orient='horizontal', from_=5, to=100, resolution = 5)
        curseurk.place(x=1000, y=400)
        k_label = Label(fen_princ, text = "K: 5")
        k_label.place(x=1030, y=440)
        monBoutonk = Button(fen_princ, text = "Validate value for K", command = print_k).place(x=950, y=480)
        
        curseurxe = Scale(fen_princ, orient='horizontal', from_=0.001, to=3000, resolution = 0.001)
        curseurxe.place(x=1100, y=400)
        xe_label = Label(fen_princ, text = "XE(0): 0.001")
        xe_label.place(x=1130, y=440)
        monBoutonxe = Button(fen_princ, text = "Validate value for XE(0)", command = print_xe).place(x=1100, y=480)
        
        monBoutongo = Button(fen_princ, text = "Launch scenario", command = sendCursors).place(x=950, y=520)

        hints_un = """
Hints:
You could try with:
d = 1 ; k = 100 ; xe = 0.001
d = 15 ; k = 100 ; xe = 0.20
d = 2 ; k = 10 ; xe = 25
            """
        next_graph_label= Label(fen_princ, text = hints_un, bg="lightgreen").place(x=960, y=600)



def animate(k):
    """Called by main.
    Goal: Animated lines created step by step for the four variables.
    Args: k (int): frames """

    # Skipping frames
    s = k*skip
    
    # Displaying legend once
    if k==0:
        ax.legend(loc='upper left', bbox_to_anchor=(-0.11, -0.065), fancybox=True, shadow=True, ncol=5, fontsize=4.5)
        ax.axhline(y=caca/caca_m, color='orange', linestyle='--', label = "Carrying Capacity")


    # Plotting lines from beginning
    ax.plot(t[:s], XC[:s], color = 'b', label = "Commoner population")
    ax.plot(t[:s], XE[:s], color = 'r', label = "Elite population")
    ax.plot(t[:s], N[:s], color = 'g', label = "Nature")
    ax.plot(t[:s], W[:s], color = 'grey', label = "Wealth")

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
    
    return [XC, XE, N ,W, parameters]

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

    # Stocking four variables and caryying capacity incremented by HANDY_calculs.c
    [XC, XE, N, W, parameters] = readFile(args.fileName)
    caca = int(parameters[-1])
    # Calculated maximum carrying capacity with the adequate formula
    caca_m = 75000

    # Skipping variables values for the animation to be faster
    skip = 50
    
    # Creating graphic on plt
    interface, ax = plt.subplots(figsize=(3.95,2.5))
    # Setting limits and resizing scale-axis
    ax.set_xlim(-20, 1020)
    ax.set_ylim(-0.05, 1.05)
    ax.set_xlabel("Time (y)", fontsize = 5)
    ax.xaxis.set_label_coords(1.08, -0.023)

    par1 = ax.twinx() # axe commoners
    par2 = ax.twinx() # axe wealth
    par1.set_ylim(-0.05, 1.05) #axe nature #axe nature
    par2.set_ylim(-0.05, 1.05) #axe nature
    par1.yaxis.set_ticks_position('left') #les mettre à gauche
    par2.yaxis.set_ticks_position('left')

    # SELON SCENARIOOOOO
    norm_caca = 6
    norm_nat = 4

    y_N_ticks = [0, 0.5, 1] #seulement les trois valeurs affihées sur l'axe
    y_N_ticks_label = ["0 λ", "0.5 λ","1 λ"]

    y_W_ticks = [-0.05, 0.45, 0.95]
    y_XC_ticks_label = ["0 χ", str(norm_caca//2)+" χ", str(norm_caca)+" χ"]

    y_XC_ticks = [0.09, 0.82, 1.55]
    y_W_ticks_label = ["0 χ", str(norm_nat//2)+" λ", str(norm_nat)+" λ"]
    ax.set_yticks(y_N_ticks, labels=y_N_ticks_label)
    par1.set_yticks(y_XC_ticks,  labels=y_XC_ticks_label)
    par2.set_yticks(y_W_ticks, labels=y_W_ticks_label)

    ax.tick_params(axis='y', labelcolor='g', length=0) #réduire taille ds valeurs
    par1.tick_params(axis='y', labelcolor='orange', length=0)
    par2.tick_params(axis='y', labelcolor='grey', length=0)

    ax.tick_params(axis='x', labelsize=5)
    ax.tick_params(axis='y', labelsize=5)
    par1.tick_params(axis='y', labelsize=5)
    par2.tick_params(axis='y', labelsize=5)

    ax.grid(which='minor', alpha=0.1)
    ax.grid(which='major', alpha=0.1)

    # Importing plt on Tkinter window
    canvas = FigureCanvasTkAgg(interface, master=fen_princ)
    canvas.get_tk_widget().place(x=0, y=275)

    # Starting animation using frames
    ani = FuncAnimation(fig = interface, func = animate, frames = range(time//skip), interval = 1, repeat = False)

    # Display window
    fen_princ.mainloop()

