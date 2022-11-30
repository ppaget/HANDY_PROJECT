from tkinter import *
import os


def afficherValeur() :
    valeur = curseur1.get()
    text1 = ("XC is : ", valeur)
    monAffichage.configure(text = text1)

fen_princ = Tk()

curseur1 = Scale(fen_princ, orient='horizontal', from_ = 0, to = 10)
curseur1.pack()

monAffichage = Label(fen_princ, text = "Value for XC", width=70)
monAffichage.pack()

monBouton = Button(fen_princ, text = "Chose Value", command = afficherValeur)
monBouton.pack()

valeur = curseur1.get()
fen_princ.mainloop()

os.chdir("/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/in_Python")
os.chdir("../in_C") #sortir de celui d'avant
# os.system("python emilien.py")
os.system("gcc HANDY_calculs.c -o handy_calculs_exe")
os.system("./handy_calculs_exe " + str(valeur)) #+ " " + str(value_xe))


