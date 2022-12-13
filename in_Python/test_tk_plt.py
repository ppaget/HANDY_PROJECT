from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import os
from time import sleep


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

def animate(k, XC, XE, N, W):

    s = k*skip

    ax[0].plot(t[:s], XC[:s], color = 'b')
    # ax[0].plot(t[:s], XE[:s], color = 'r')
    # ax[0].plot(t[:s], N[:s], color = 'g')
    # ax[0].plot(t[:s], W[:s], color = 'k')

    # ax[0].legend(["Commoner population", "Elite population", "Nature", "Wealth"])
    # #rendre legende plus petite

    if k==(time//skip)-1:
        next_graph()

def animate_c(k):

    s = k*skip

    ax[1].plot(t[:s], XC_c[:s], color = 'b')
    # ax[0].plot(t[:s], XE[:s], color = 'r')
    # ax[0].plot(t[:s], N[:s], color = 'g')
    # ax[0].plot(t[:s], W[:s], color = 'k')

    # ax[0].legend(["Commoner population", "Elite population", "Nature", "Wealth"])
    # #rendre legende plus petite

    if k==(time//skip)-1:
        next_graph()

def stock_k() :
    text_k = "k" + curseurk
    chosen_params.append(text_k)

def stock_d() :
    text_d = "d " + curseurd.get()
    chosen_params.append(text_d)

def sendCursors():
    global XC_c
    k = str(curseurk.get())
    d = str(curseurd.get())

    variables = [title, k, d]
    os.chdir("in_C")
    os.system("gcc HANDY_calculs.c -o handy_calculs_exe")
    os.system("./handy_calculs_exe " + variables[0] + " " + variables[1] + " " + variables[2])
    sleep(3)

    file_cursors = "../in_C/results_python_cursors.txt"
    [XC_c, XE_c, N_c, W_c, variables, parameters] = readFile(file_cursors)
    t = [i for i in range(time)]

    canvas = FigureCanvasTkAgg(interface, master=fen_princ)
    canvas.get_tk_widget().place(x=0, y=180)
    print("before anim")
    ani = FuncAnimation(fig = interface, func = animate_c, frames = range(time//skip), interval = 1, repeat = False)
    



def stateText():

    text1 = "Initial variables:"
    text2 = "Parameters :"
    initial_state_label = Label(fen_princ, text = text1+text2, width=70)
    initial_state_label.pack()

def finalText():
    ax[2].clear()
    ax[2].axis("off")
    if W[999] and N[999] == 0 :
        conclusion_text = "We have reached a collapse.\n\nThis is both a type-N and a type-L collapse."
    if N[999] == 0 :
        conclusion_text = "We have reached a collapse.\n\nThis is a type-N collapse."
    if W[999] == 0 :
        conclusion_text = "We have reached a collapse.\n\nThis is a type-L collapse."
    ax[2].text(0.3, 0.5, s= conclusion_text, style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

def next_graph():
    global curseurk
    global monAffichagek
    global curseurd
    global monAffichaged

    print("emilouche")

    # window = [welcomeI_label, home_button]
    # for i in window : i.delete()

    # welcomeI_label = Label(fen_princ, text = text_welcomeI, width=70).grid(row= 0,column=0)
    # home_button = Button(fen_princ, text = "Back to Home", command = stateText).grid(row=1, column=0)

    next_graph_label= Label(fen_princ, text = "You can now chose different starting parameters", width=70).grid(row= 0,column=1)

    curseurk = Scale(fen_princ, orient='horizontal', from_ = 0, to = 100)
    curseurk.grid(row=1, column=1)

    monBoutonk = Button(fen_princ, text = "Validate value for K", command = stock_k).grid(row=3, column=1)

    curseurd = Scale(fen_princ, orient='horizontal', from_ = 1.25, to = 10)
    curseurd.grid(row=4, column=1)

    monBoutond = Button(fen_princ, text = "Validate value for D", command = stock_d).grid(row=6, column=1)
    
    monBoutongo = Button(fen_princ, text = "Launch scenario", command = sendCursors).grid(row=7, column=1)

    print(chosen_params)





if __name__=='__main__':

    # global fen_princ
    # global skip
    # global time
    # global t
    # global XC
    # global XE
    # global N
    # global W
    # global ax
    # global welcomeI_label
    # global home_button
    # global text_welcomeI
    # global title
    # global chosen_params

    chosen_params = []
    title = "egalitarian_cursors"
    fen_princ = Tk()
    fen_princ.attributes('-fullscreen', True)

    text_welcomeI = "WELCOME TO YOUR " + title.upper() + " MODELISATION"

    welcomeI_label = Label(fen_princ, text = text_welcomeI, width=70).grid(row= 0,column=0)
    # welcomeI_label.pack()
    home_button = Button(fen_princ, text = "Back to Home", command = stateText).grid(row=1)
    # home_button.pack()
    time = 1000
    skip = 20
    
    fname = "in_C/results_python_file.txt"
    [XC, XE, N, W, variables, parameters] = readFile(fname)
    t = [i for i in range(time)]

    interface, ax = plt.subplots(1, 2, figsize=(6.5,3))

    # stateText()

    ax[0].set_xlim(-20, 1020)
    ax[0].set_ylim(-0.03, 1.03)
    ax[1].set_xlim(-20, 1020)
    ax[1].set_ylim(-0.03, 1.03)

    canvas = FigureCanvasTkAgg(interface, master=fen_princ)
    canvas.get_tk_widget().place(x=0, y=180)

    ani = FuncAnimation(fig = interface, func = animate, fargs = (XC,XE,N,W), frames = range(time//skip), interval = 1, repeat = False)
    

    
    fen_princ.mainloop()

# if __name__=='__main__':
#     fen_princ = Tk()
# interface()
#     f
#     fen_princ.mainloop()

# x = input("Enter x : ")
# print(x)