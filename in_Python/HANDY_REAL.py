from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
from matplotlib.animation import FuncAnimation
import os
# import functools

# def calltracker(func):
#     @functools.wraps(func)
#     def wrapper(*args):
#         wrapper.has_been_called = True
#         return func(*args)
#     wrapper.has_been_called = False
#     return wrapper

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

# def finalText():
    # ax[1].clear()
    # ax[1].axis("off")
    # if W[999] and N[999] == 0 :
    #     conclusion_text = "We have reached a collapse.\n\nThis is both a type-N and a type-L collapse."
    # if N[999] == 0 :
    #     conclusion_text = "We have reached a collapse.\n\nThis is a type-N collapse."
    # if W[999] == 0 :
    #     conclusion_text = "We have reached a collapse.\n\nThis is a type-L collapse."
    # ax[2].text(0.3, 0.5, s= conclusion_text, style='italic',
    #     bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

def animate(k,XC,XE,N,W):
    s = k*skip
    
    if k==0:
        ax[0].legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=4)

    ax[0].plot(t[:s], XC[:s], color = 'b', label = "Commoner population")
    ax[0].plot(t[:s], XE[:s], color = 'r', label = "Elite population")
    ax[0].plot(t[:s], N[:s], color = 'g', label = "Nature")
    ax[0].plot(t[:s], W[:s], color = 'k', label = "Wealth")


def graphic(fname):
    text_welcomeI = welcomeScenario("Egalitarian")
    print(text_welcomeI)
    welcomeI_label = Label(fen_princ, text = text_welcomeI, width=70).grid(row= 0,column=0)
    home_button = Button(fen_princ, text = "Back to Home", command = introduction).grid(row=1, column=0)

    time = 1000
    skip = 20
    t = [i for i in range(time)]

    interface, ax = plt.subplots(1, 2, figsize=(6.5,3))
    ax[0].set_xlim(-20, 1020)
    ax[0].set_ylim(-0.03, 1.03)
    ax[1].set_xlim(-20, 1020)
    ax[1].set_ylim(-0.03, 1.03)

    [XC, XE, N, W, variables, parameters] = readFile(fname)

    canvas = FigureCanvasTkAgg(interface, master=fen_princ)
    canvas.get_tk_widget().place(x=0, y=180)

    ani = FuncAnimation(fig = interface, func = animate, fargs = (XC,XE,N,W), frames = range(time//skip), interval = 1, repeat = False)
    

def welcomeScenario(title):
    text = "WELCOME TO YOUR " + title.upper() + "SCENARIO"


def send_egalitarianScenario():
    path = ['egalitarian', "Text/HANDY_egalitarian_basic.txt"]

    window = [question1_label, enter_egalitarian_label, enter_egalitarian_button]
    for i in window : i.destroy()

    os.chdir("in_C")
    os.system("gcc HANDY_calculs.c -o handy_calculs_exe")
    os.system("./handy_calculs_exe " + path[0] + " " + path[1])
    time.sleep(2)
    graphic("in_C/results_python_file.txt")

def send_equitableScenario():
    send_equitableScenario.has_been_called = True
    path = ['equitable', "Text/HANDY_equitable_basic.txt"]

    window = [question1_label, question2_label, enter_equitable_label, enter_equitable_button]
    for i in window : i.destroy()

    # os.chdir("/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/in_Python")
    # print(os.getcwd())
    os.chdir("in_C")
    # print(os.getcwd())
    os.system("gcc HANDY_calculs.c -o handy_calculs_exe")
    os.system("./handy_calculs_exe " + path[0] + " " + path[1])

def send_unequalScenario():
    send_unequalScenario.has_been_called = True
    path = ['unequal', "Text/HANDY_unequal_basic.txt"]

    window = [question1_label, question2_label, enter_unequal_label, enter_unequal_button]
    for i in window : i.destroy()

    os.chdir("in_C")
    os.system("gcc HANDY_calculs.c -o handy_calculs_exe")
    os.system("./handy_calculs_exe " + path[0] + " " + path[1])

def go_egalitarianScenario():
    global enter_egalitarian_label
    global enter_egalitarian_button

    window = [elite_button, egalitarian_button]
    for i in window : i.destroy()

    egalitarian_summary = """You have chosen a scenario with no Elite Population.
                            This means you will enter the Egalitarian Scenario.\n
                            Ready?"""

    enter_egalitarian_label = Label(fen_princ, text = egalitarian_summary, width=70)
    enter_egalitarian_label.grid(row=0,column=0)

    enter_egalitarian_button = Button(fen_princ, text = "Start the Egalitarian Modelisation!", command = send_egalitarianScenario)
    enter_egalitarian_button.grid(row=1,column=0)

def go_equitableScenario():
    global enter_equitable_label
    global enter_equitable_button

    window = [elite_button, egalitarian_button, equitable_button, unequal_button]
    for i in window : i.destroy()

    equitable_summary = """You have chosen a scenario with an Elite Population which is payed
                            as much as the Commoner Population.
                            This means you will enter the Equitable Scenario.\n
                            Ready?"""

    enter_equitable_label = Label(fen_princ, text = equitable_summary, width=70)
    enter_equitable_label.grid(row=0,column=0)

    enter_equitable_button = Button(fen_princ, text = "Start the Equitable Modelisation!", command = send_egalitarianScenario)
    enter_equitable_button.grid(row=1,column=0)

def go_unequalScenario():
    global enter_unequal_label
    global enter_unequal_button

    window = [elite_button, egalitarian_button, equitable_button, unequal_button]
    for i in window : i.destroy()

    unequal_summary = """You have chosen a scenario with an Elite Population which is payed
                            more than the Commoner Population.
                            This means you will enter the Unequal Scenario.\n
                            Ready?"""

    enter_unequal_label = Label(fen_princ, text = unequal_summary, width=70)
    enter_unequal_label.grid(row=0,column=0)

    enter_unequal_button = Button(fen_princ, text = "Start the Unequal Modelisation!", command = send_unequalScenario)
    enter_unequal_button.grid(row=1,column=0)

def questionK():
    global question2_label
    global equitable_button
    global unequal_button

    window = [elite_button, egalitarian_button]
    for i in window : i.destroy()

    question2 = """You have chosen a scenario with an Elite Population.\n
                    Second choice: Do you want the Elite and the Commoner Populations to be paid equally,\n
                    with no difference in their salaries?"""

    question2_label = Label(fen_princ, text = question2, width=70)
    question2_label.grid(row=0,column=0)

    equitable_button = Button(fen_princ, text = "I want the two to be paid equally", command = go_equitableScenario)
    equitable_button.grid(row=1,column=0)

    unequal_button = Button(fen_princ, text = "I do not want the two to be paid equally", command = go_unequalScenario)
    unequal_button.grid(row=2,column=0)

def questionXE():
    global question1_label
    global egalitarian_button
    global elite_button

    window = [welcome_label, go_button]
    for i in window : i.destroy()

    question1 = """First choice: Do you want an Elite Population in the scenario?"""
    #Si possible, travailler sur le côté graphique/esthétique du texte 

    # First choices
    question1_label = Label(fen_princ, text = question1, width=70)
    question1_label.grid(row=0,column=0)

    elite_button = Button(fen_princ, text = "I want an Elite Population", command = questionK)
    elite_button.grid(row=1,column=0)

    egalitarian_button = Button(fen_princ, text = "I do not want an Elite population", command = go_egalitarianScenario)
    egalitarian_button.grid(row=2,column=0)

def introduction():
    global welcome_label
    global go_button


    #finir texte intro avec présentation prjet, explications variables + paramètres ET les 3 choix possibles pour user 
    text_welcome = """WELCOME TO THE HANDY PROJECT\n\n
                You are about to simulate the collapse of the society 
                using only four variables and ten parameters. 
                We will ask you to make choices about the variables and parameters so 
                you can try different types of scenario.\n\n
                First choice: do you want an Elite Population in the scenario?"""
    #Si possible, travailler sur le côté graphique/esthétique du texte 

    # First choices
    welcome_label = Label(fen_princ, text = text_welcome, width=70)
    welcome_label.grid(row=0,column=0)

    go_button = Button(fen_princ, text = "Let's get started!", command = questionXE)
    go_button.grid(row=1,column=0)


if __name__=='__main__':
    send_egalitarianScenario.has_been_called = False
    send_equitableScenario.has_been_called = False
    send_unequalScenario.has_been_called = False

    fen_princ = Tk()

    fen_princ.attributes('-fullscreen', True)
    introduction()

    # while not send_egalitarianScenario.has_been_called :
    #     print("wait") #or send_equitableScenario.has_been_called or send_unequalScenario.has_been_called:
    
    # text_welcomeI = welcomeScenario("Egalitarian")
    # print(text_welcomeI)
    # welcomeI_label = Label(fen_princ, text = text_welcomeI, width=70).grid(row= 0,column=0)
    # home_button = Button(fen_princ, text = "Back to Home", command = introduction).grid(row=1, column=0)

    # time = 1000
    # skip = 20
    # t = [i for i in range(time)]

    # interface, ax = plt.subplots(1, 2, figsize=(6.5,3))
    # ax[0].set_xlim(-20, 1020)
    # ax[0].set_ylim(-0.03, 1.03)
    # ax[1].set_xlim(-20, 1020)
    # ax[1].set_ylim(-0.03, 1.03)

    # graphic("in_C/results_python_file.txt")
        
    # elif send_equitableScenario.has_been_called :
    #     text_welcomeI = welcomeScenario("Equitable")
    #     welcomeI_label = Label(fen_princ, text = text_welcomeI, width=70).grid(row= 0,column=0)
    #     home_button = Button(fen_princ, text = "Back to Home", command = introduction).grid(row=1)

    #     time = 1000
    #     skip = 20
    #     t = [i for i in range(time)]

    #     interface, ax = plt.subplots(1, 2, figsize=(6.5,3))
    #     ax[0].set_xlim(-20, 1020)
    #     ax[0].set_ylim(-0.03, 1.03)
    #     ax[1].set_xlim(-20, 1020)
    #     ax[1].set_ylim(-0.03, 1.03)

    #     graphic("in_C/results_python_file.txt")
    # elif send_unequalScenario.has_been_called :
    #     text_welcomeI = welcomeScenario("Unequal")
    #     pass





    fen_princ.mainloop()






# expliquer les variables 
# et la normalisation 