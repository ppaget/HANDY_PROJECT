import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from PIL import Image
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os


def sendScenario():
    path = ['s']
    for i in lb.curselection():
        j = lb.get(i)
        if j == "Default society" : path.append("../Text/HANDY_params_default.txt")
        if j == "Egalitarian society" : path.append("../Text/HANDY_params_egalitarian_2.txt")
        if j == "Inequal society 1" : path.append("../Text/HANDY_params_inequal.txt")
        if j ==  "Inequal society 2" : path.append("../Text/HANDY_params_inequal_2.txt")
        if j == "Stable society 1" : path.append("../Text/HANDY_params_stable_egalitarian.txt")
        if j == "Stable society 2" : path.append("../Text/HANDY_params_stable_equitable_1.txt")
        if j == "Stable society 3" : path.append("../Text/HANDY_params_stable_equitable_2.txt")

    print(path[0] + " " + path[1])

    fen_princ.destroy()

def choseScenario():
    global monAffichageinput
    global lb
    global monBoutoninput

    monAffichageinput = Label(fen_princ, text = "Chose an existing scenario", width=70)
    monAffichageinput.pack()

    lb = Listbox(fen_princ)
    lb.insert(1, "Default society")
    lb.insert(2, "Egalitarian society")
    lb.insert(3, "Inequal society 1")
    lb.insert(4, "Inequal society 2")
    lb.insert(5, "Stable society 1")
    lb.insert(6, "Stable society 2")
    lb.insert(7, "Stable society 3")
    lb.pack()

    monBoutoninput = Button(fen_princ, text = "Validate scenario", command = sendScenario)
    monBoutoninput.pack()

def test(): 
    fen_princ = Tk()
    lb = Listbox(fen_princ)
    lb.insert(1, "Default society")
    lb.insert(2, "Egalitarian society")
    lb.insert(3, "Inequal society 1")
    lb.insert(4, "Inequal society 2")
    lb.insert(5, "Stable society 1")
    lb.insert(6, "Inequal society 2")
    lb.insert(7, "Inequal society 3")
    lb.pack()
    selected = lb.curselection()
    print(selected)
    fen_princ.mainloop()

if __name__=='__main__':
    fen_princ = Tk()

    fen_princ.attributes('-fullscreen', True)
    choseScenario()
    fen_princ.mainloop()



# skip_header=2