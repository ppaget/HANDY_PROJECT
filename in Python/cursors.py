from tkinter import *

def afficherValeur_xc() :
    valeur = curseurxc.get()
    text1 = ("XC : ", valeur)
    monAffichagexc.configure(text = text1)

def afficherValeur_xe() :
    valeur = curseurxe.get()
    text1 = ("XE : ", valeur)
    monAffichagexe.configure(text = text1)

def afficherValeur_n() :
    valeur = curseurn.get()
    text1 = ("N : ", valeur)
    monAffichagen.configure(text = text1)

def afficherValeur_w() :
    valeur = curseurw.get()
    text1 = ("W : ", valeur)
    monAffichagew.configure(text = text1)


if __name__=='__main__':

    fen_princ = Tk()

    # XC
    curseurxc = Scale(fen_princ, orient='horizontal', from_ = 0, to = 10)
    curseurxc.pack()

    monAffichagexc = Label(fen_princ, text = "Value wanted for XC", width=70)
    monAffichagexc.pack()

    monBoutonxc = Button(fen_princ, text = "Get value for XC", command = afficherValeur_xc())
    monBoutonxc.pack()
    
    # XE
    curseurxe = Scale(fen_princ, orient='horizontal', from_ = 0, to = 20)
    curseurxe.pack()

    monAffichagexe = Label(fen_princ, text = "Value wanted for XE", width=70)
    monAffichagexe.pack()

    monBoutonxe = Button(fen_princ, text = "Get value for XE", command = afficherValeur_xe())
    monBoutonxe.pack()

    #N
    curseurn = Scale(fen_princ, orient='horizontal', from_ = 0, to = 5)
    curseurn.pack()

    monAffichagen = Label(fen_princ, text = "Value wanted for N", width=70)
    monAffichagen.pack()

    monBoutonn = Button(fen_princ, text = "Get value for N", command = afficherValeur_n())
    monBoutonn.pack()

    # W
    curseurw = Scale(fen_princ, orient='horizontal', from_ = 0, to = 15)
    curseurw.pack()

    monAffichagew = Label(fen_princ, text = "Value wanted for W", width=70)
    monAffichagew.pack()

    monBoutonw = Button(fen_princ, text = "Get value for W", command = afficherValeur_w())
    monBoutonw.pack()

    # END
    fen_princ.mainloop()


