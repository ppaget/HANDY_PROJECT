from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time
from tkinter import *

def questionXE():
    return 3

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
    welcome_label.pack()

    go_button = Button(fen_princ, text = "Let's get started!", command = questionXE)
    go_button.pack()

if __name__=='__main__':
    fen_princ = Tk()

    fen_princ.attributes('-fullscreen', True)
    word = introduction()

    print(word)
    fen_princ.mainloop()

