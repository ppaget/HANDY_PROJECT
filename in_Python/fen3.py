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


# def analysis_results(nbr):
    # end_button = Button(fen_princ, text = "Quit Model", command = lambda:quit(fen_princ)).place(x=1155, y=25)
    # home_button = Button(fen_princ, text = "Back to Home", command = lambda:backFen(fen_princ,1)).place(x=1150, y=60)
    # again_button = Button(fen_princ, text = "Chose new values", command = lambda:backFen2(fen_princ, args.scenario)).place(x=1130, y=95)

#     result_text = []
#     if nbr == 1:
#         text1 = """
#         Your personnal modelisation leads to a:
#         TYPE-N COLLAPSE.
        
#         Nature is over-exploited by Commoners 
#         to sustain themselves and Elites.
#         It has reached zero.
#         Accumulated Wealth is not sufficient to 
#         save humans who all die of famine.
#         Carrying capacity is too far-away from
#         the maximum one (1) 
#         """
#         result_text.append(text1)
#     if nbr == 2:
#         text2 = """
#         Your personnal modelisation leads to a:
#         TYPE-L COLLAPSE.

#         Humans do not pick enough Nature ressources
#         and accumulated Wealth is not sufficient.
#         They all die: first Commoners then Elites.
#         Nature can prosperate.
#         """
#         result_text.append(text2)
#     if nbr == 3:
#         text3 = """
#         Your personnal modelisation leads to a:
#         TYPE-N REVERSIBLE COLLAPSES.

#         Nature first reaches zero.
#         Humans start dying of famine.
#         Nature can recover.
#         Humans recover too.
#         Until Nature reaches zero...
#         """
#         result_text.append(text3)
#     if nbr == 4:
#         text4 = """
#         Your personnal modelisation leads to an:
#         EQUILIBRIUM.

#         Total Population reaches equilibirum under 
#         maximum carrying capacity.
#         Difference with the optimal:
#         Earth will host less Humans and less Nature.
#         """
#         result_text.append(text4)

#     result_label= Label(fen_princ, text = result_text[0]).grid(row= 0,column=2)


def animate_c(k, XC, XE, N, W):

    s = k*skip

    # if k==0:
    #     # ax[1].axhline(y=caca_c/caca_m, color='orange', linestyle='--')
    #     ax[1].legend(loc='upper left', bbox_to_anchor=(0.2, -0.06),
    #     fancybox=True, shadow=True, ncol=5, fontsize=5)

    animation(k, ax[1], t[:s], XC[:s], XE[:s], N[:s], W[:s], CC_c, mx_CC)
    # problème avec légende je pense
    # ax[1].plot(t[:s], XC[:s], color = 'b')
    # ax[1].plot(t[:s], XE[:s], color = 'r')
    # ax[1].plot(t[:s], N[:s], color = 'g')
    # ax[1].plot(t[:s], W[:s], color = 'grey')

    if k==(time//skip)-1:
        # scenario = 0
        # zero = float(0)
        # if zero in N :
        #     zero_1 = np.where(N==zero)
        #     i0 = zero_1[0][0]
        #     max1 = max(N[i0+1:])
        #     iM = np.where(N==max1)[0][0]
        #     zero_2 = np.where(N[iM+1:]==zero)
        #     i1 = zero_2[0][0] 
        #     max2 = max(N[i1+1:])
        #     if abs(max1-max2)<0.5: #valeur seuil
        #         scenario = 3
        #     elif N[998]==0 :
        #         scenario = 1
        #     else :
        #         scenario = 4
        # else :
        #     if XC[998]<=0.1 : #Valeur de seuil car on ne voit pas totalement la collapse dans le uneq_1
        #         scenario = 2
        #     else : 
        #         scenario = 4

        # analysis_results(scenario) #en argument scenario

        resultTxt = resultScenario(XC, N)
        result_label= Label(fen_princ, text = resultTxt).grid(row= 0,column=2)


# def reminders(d, k, xe):
#     if args.scenario == "egalitarian" :
#         reminder1 = """
#         EGALITARIAN MODELISATION WITH CHOICES
        
#         Used values for OPTIMAL EQUILIBRIUM:
#             - Initial Commoner population: 100
#             - Initial Elite population: 0
#             - Inequality factor: 0 
#             - Depletion per capita: D_reference """

#         reminder2 = """
#         Value chosen previously:
#             - Depletion per capita:
#             D_reference*""" + str(d)
#         return reminder1, reminder2


#     if args.scenario == "equitable" :
#         reminder1 = """
#         EQUITABLE MODELISATION WITH CHOICES
        
#         Used values for OPTIMAL EQUILIBRIUM:
#             - Initial Commoner population: 100
#             - Initial Elite population: 25
#             - Inequality factor: 1 
#             - Depletion per capita: D_reference*1.25 """
        
#         reminder2 = """
#         Value chosen previously:
#             - Depletion per capita:
#             D_reference*""" + str(d)

#         return reminder1, reminder2

#     if args.scenario == "unequal" :
#         reminder1 = """
#         EQUITABLE MODELISATION WITH CHOICES
        
#         Used values for OPTIMAL EQUILIBRIUM:
#             - Initial Commoner population: 10 000
#             - Initial Elite population: 3 000
#             - Commoner birth rate: 0.0065 (other scenarios: 0.03)
#             - Elite birth rate: 0.02 (other scenarios: 0.03)
#             - Inequality factor: 10 
#             - Depletion per capita: D_reference*0.95
#             """
#         reminder2 = """
#         Values chosen previously:
#             - Depletion per capita:
#             D_reference*""" + str(d)+ """
#             - Inequality factor:""" + str(k) + """ 
#             - Initial Elite population""" + str(xe) 
#         return reminder1, reminder2
# # ATTENTION MARCHE PAS BIEN


if __name__=='__main__':

    args = parser.parse_args()
    fen_princ = Tk()
    fen_princ.attributes('-fullscreen', True)
    moveButton(fen_princ, 3, args.scenario)

    [XC_b, XE_b, N_b, W_b, variables, parameters_b] = readFile(args.fileBasic)
    [XC_c, XE_c, N_c, W_c, variables, parameters_c] = readFile(args.fileCursors)

    CC_c = float(parameters_c[8])
    # k_c = float(parameters_c[9])
    # xe_c = XE_c[0]

    reminder1 = 0
    reminder2 = 0
    if args.scenario == "eg":
        reminder1, reminder2 = remindersFen3("eg", CC_c)
    if args.scenario == "eq":
        reminder1, reminder2 = remindersFen3("eg", CC_c)
    if args.scenario == "un":
        reminder1, reminder2 = remindersFen3("eg", CC_c)

    # reminder1, reminder2 = remindersFen3(CC_c)
    
    reminder1_label = Label(fen_princ, text = reminder1, bg="seashell").grid(row= 0,column=0)
    reminder2_label = Label(fen_princ, text = reminder2, bg="seashell").grid(row= 0,column=1)

    time = 1000
    mx_CC = 75000
    norm_CC = float(parameters_c[-3])
    norm_N = float(parameters_c[-2])
    skip = 50

    CC_b = int(parameters_b[-1])
    CC_c = int(parameters_c[-1])

    t = [i for i in range(time-1)]

    fig, ax = plt.subplots(1, 2, figsize=(6.39,2.74), gridspec_kw={'width_ratios': [1, 1.5]})
    graphTemplate(ax[0], 1, 4)
    graphTemplate(ax[1], norm_CC, norm_N)

    # ax[0].axhline(y=caca_b/caca_m, color='orange', linestyle='--', label = "Carrying Capacity")
    animation(1, ax[0], t, XC_b, XE_b, N_b, W_b, CC_b, mx_CC)

    # ax[0].plot(t, XC_b, color = 'b', label = "Commoner population")
    # ax[0].plot(t, XE_b, color = 'r', label = "Elite population")
    # ax[0].plot(t, N_b, color = 'g', label = "Nature")
    # ax[0].plot(t, W_b, color = 'grey', label = "Wealth")
    # ax[0].legend(loc='upper left', bbox_to_anchor=(0.2, -0.06),
    #     fancybox=True, shadow=True, ncol=5, fontsize=5)


    canvas = FigureCanvasTkAgg(fig, master=fen_princ)
    canvas.get_tk_widget().place(x=0, y=250)

    ani = FuncAnimation(fig = fig, func = animate_c, fargs = (XC_c,XE_c,N_c,W_c), frames = range(time//skip), interval = 1, repeat = False)
       
    #ani = FuncAnimation(fig = fig, func = animation, fargs = (XC_c,XE_c,N_c,W_c), frames = range(time//skip), interval = 1, repeat = False)
       
    fen_princ.mainloop()
