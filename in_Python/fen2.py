from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import os
import argparse

from helpers.fen_services import readFile, moveButton, cursor_CC
from helpers.fen_plot import graphTemplate, animation
from helpers.fen_txt import welcomeTxtFen2

parser = argparse.ArgumentParser(description="File for optimal equilibrium of chosen scenario sent from C")
parser.add_argument("--fileName", type=str, help="fichier C", default="in_C/results_python_file.txt")
parser.add_argument("--scenario", type=str, help="type of scenario chosen", default="eg")



# def sendCursors():

#     cursor = 0
#     if args.scenario == "eg":
#         cursor = ["eg_c", str(cursorCC.get())]

#     if args.scenario == "eq":
#         cursor = ["eq_c", str(cursorCC.get())]

#     if args.scenario == "un":
#         cursor = ["un_c", str(cursorCC.get())]
#     Py2C(cursor, fen_princ)






def print_d() :
    text_d = "d: " + str(curseurd.get())
    d_label.configure(text= text_d)
def print_k() :
    text_k = "K: " + str(curseurk.get())
    k_label.configure(text= text_k)
def print_xe() :
    text_xe = "XE(0): " + str(curseurxe.get())
    xe_label.configure(text= text_xe)

# def cursor_CC():
#     global curseurk
#     global k_label
#     global curseurd
#     global d_label
#     global curseurxe
#     global xe_label



#     if args.scenario == "eg" or args.scenario == "eq" :
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
#         monBoutond = Button(fen_princ, text = "Validate d", command = print_d).place(x=940, y=320)
#         monBoutongo = Button(fen_princ, text = "Launch scenario", command = sendCursors).place(x=950, y=360)

#         if args.scenario == "eg":
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

        
#     else:
#         text_d = """
#     You can now chose to vary two starting parameters
#     and an initial variable:
#         the Depletion per Capita, D
#         the Inequality Factor, K
#         the initial Elite Population, XE(0)

#     D represents how much Commoners will take ressources from Nature.
#     High D means high exploitation.
#     Chose d: d*D_reference = D.

#     K represents the factor between Commoners and Elites salaries.
#     High K means high difference in salaries.

#     XE(0) represents the number of non-workers at beginning.
#     High XE(0) means high exploitation of ressources to carry 
#     high population.
#     """
#         next_graph_label= Label(fen_princ, text = text_d).place(x=800, y=100)

#         curseurd = Scale(fen_princ, orient='horizontal', from_=0.50, to=20.00, digits = 4, resolution = 0.05)
#         curseurd.place(x=900, y=400)
#         d_label = Label(fen_princ, text = "d: 0.5")
#         d_label.place(x=930, y=440)
#         monBoutond = Button(fen_princ, text = "Validate d", command = lambda : dispValue("d", curseurd, d_label)).place(x=800, y=480)

#         curseurk = Scale(fen_princ, orient='horizontal', from_=5, to=100, resolution = 5)
#         curseurk.place(x=1000, y=400)
#         k_label = Label(fen_princ, text = "K: 5")
#         k_label.place(x=1030, y=440)
#         monBoutonk = Button(fen_princ, text = "Validate K", command = print_k).place(x=950, y=480)
        
#         curseurxe = Scale(fen_princ, orient='horizontal', from_=0.001, to=3000, resolution = 0.001)
#         curseurxe.place(x=1100, y=400)
#         xe_label = Label(fen_princ, text = "XE(0): 0.001")
#         xe_label.place(x=1130, y=440)
#         monBoutonxe = Button(fen_princ, text = "Validate XE(0)", command = print_xe).place(x=1100, y=480)
        
#         monBoutongo = Button(fen_princ, text = "Launch scenario", command = sendCursors).place(x=950, y=520)

#         hints_un = """
# Hints:
# You could try with:
# d = 1 ; k = 100 ; xe = 0.001
# d = 15 ; k = 100 ; xe = 0.20
# d = 2 ; k = 10 ; xe = 25
#             """
#         next_graph_label= Label(fen_princ, text = hints_un, bg="lightgreen").place(x=960, y=600)




def animate_f(k):
    """Called by main.
    Goal: Animated lines created step by step for the four variables.
    Args: k (int): frames """

    # Skipping frames
    s = k*skip
    
    # Displaying legend once
    # if k==0:
    #     ax.legend(loc='upper left', bbox_to_anchor=(-0.11, -0.065), fancybox=True, shadow=True, ncol=5, fontsize=4.5)
    #     ax.axhline(y=CC/mx_CC, color='orange', linestyle='--', label = "Carrying Capacity")

    # Plotting lines from beginning
    animation(k, ax, t[:s], XC[:s], XE[:s], N[:s], W[:s], CC, mx_CC)

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
    moveButton(fen_princ, 2, args.scenario)

    # Text according to chosen scenario in previous window
    text_welcome = 0
    if args.scenario == "eg":
        text_welcome = welcomeTxtFen2("eg")
    if args.scenario == "eq":
        text_welcome = welcomeTxtFen2("eq")
    if args.scenario == "un":
        text_welcome = welcomeTxtFen2("un")
    welcome_label = Label(fen_princ, text = text_welcome).grid(row= 0,column=0)

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

    # Add template to graph
    graphTemplate(ax, 1, 4)

    # Importing plt on Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=fen_princ)
    canvas.get_tk_widget().place(x=0, y=275)

    # Starting animation using frames
    ani = FuncAnimation(fig = fig, func = animate_f, frames = range(time//skip), interval = 1, repeat = False)

    # Display window
    fen_princ.mainloop()

