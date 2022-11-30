from tkinter import *
# - - - - - - - - - - - - - - - - - -
# Déclarations des fonctions utilisées
# - - - - - - - - - - - - - - - - - -

TK_SILENCE_DEPRECATION=1

def afficherValeur(string) :
    if string == "xc":
        valeur = curseurxc.get()
        text1 = ("XC : ", valeur)
        monAffichagexc.configure(text = text1)
    # if string == 'xe' :
    #     valeur = curseurxe.get()
    #     text1 = ("XE : ", valeur)
    #     monAffichagexe.configure(text = text1)

# - - - - - - - - - - - - - - - - - -
# Création de la fenêtre et des objets associés la fenêtre
# - - - - - - - - - - - - - - - - - -

fen_princ = Tk()

# Création d'un Scale nommé curseur1
curseurxc = Scale(fen_princ, orient='horizontal', from_ = 0, to = 10)
curseurxc.pack()

# Création d'un Label nommé monAffichage
monAffichagexc = Label(fen_princ, text = "Value wanted for XC", width=70)
monAffichagexc.pack()

# Création d'un Button lancant la fonction afficherValeur()
monBoutonxc = Button(fen_princ, text = "Get value for XC", command = afficherValeur("xc"))
monBoutonxc.pack()


# curseurxe = Scale(fen_princ, orient='horizontal', from_ = 0, to = 20)
# curseurxe.pack()

# monAffichagexe = Label(fen_princ, text = "XE is : ", width=70)
# monAffichagexe.pack()

# monBoutonxe = Button(fen_princ, text = "Get value for XE", command = afficherValeur('xe'))
# monBoutonxe.pack()


# curseurn = Scale(fen_princ, orient='horizontal', from_ = 0, to = 5)
# curseurn.pack()

# curseurw = Scale(fen_princ, orient='horizontal', from_ = 0, to = 15)
# curseurw.pack()

# - - - - - - - - - - - - - - - - - -
# Bouclage de la fenêtre fen_princ
# - - - - - - - - - - - - - - - - - -

fen_princ.mainloop()

