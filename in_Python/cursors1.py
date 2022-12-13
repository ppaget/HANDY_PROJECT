from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

def afficherValeur_xc() :
    valeur = curseurxc.get()
    text1 = "XC : " + str(valeur)
    monAffichagexc.configure(text = text1)
def afficherValeur_xe() :
    valeur = curseurxe.get()
    text1 = "XE : " + str(valeur)
    monAffichagexe.configure(text = text1)
def afficherValeur_n() :
    valeur = curseurn.get()
    text1 = "N : " + str(valeur)
    monAffichagen.configure(text = text1)
def afficherValeur_w() :
    valeur = curseurw.get()
    text1 = "W : " + str(valeur)
    monAffichagew.configure(text = text1)


def sendScenario():
    path = ['s']
    for i in lb.curselection():
        j = lb.get(i)
        if j == "Default society" : path.append("../Text/HANDY_params_default.txt") # "../" necessary : allows to exit in_C file and go into HANDY_PROJECT global file 
        if j == "Egalitarian society" : path.append("../Text/HANDY_params_egalitarian_2.txt")
        if j == "Inequal society 1" : path.append("../Text/HANDY_params_inequal.txt")
        if j ==  "Inequal society 2" : path.append("../Text/HANDY_params_inequal_2.txt")
        if j == "Stable egalitarian society" : path.append("../Text/HANDY_params_stable_egalitarian.txt")
        if j == "Stable equitable society 1" : path.append("../Text/HANDY_params_stable_equitable_1.txt")
        if j == "Stable equitable society 2" : path.append("../Text/HANDY_params_stable_equitable_2.txt")

    #send the good file 
    os.chdir("in_C")


    os.system("gcc HANDY_calculs.c -o handy_calculs_exe") #spaces don't count as arguments
    os.system("./handy_calculs_exe " + path[0] + " " + path[1]) 
    # argv[1]=path[0] : indicates which type of scenario the user choose 

    fen_princ.destroy()

def sendCursors():
    xc = str(curseurxc.get())
    xe = str(curseurxe.get())
    n = str(curseurn.get())
    w = str(curseurw.get())

    variables = ['c', xc, xe, n, w]
    os.chdir("in_C")
    os.system("gcc HANDY_calculs.c -o handy_calculs_exe")
    os.system("./handy_calculs_exe " + variables[0] + " " + variables[1] + " " + variables[2] + " " + variables[3] + " " + variables[4])

    fen_princ.destroy()

def sendPath():
    path = ['f', name_file.get()]

    window = [monAffichagep, monBoutonfile, monBoutoncurs, monBoutonpath]
    for i in window : i.destroy()

    # os.chdir("/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/in_Python")
    # print(os.getcwd())
    os.chdir("in_C")
    # print(os.getcwd())
    os.system("gcc HANDY_calculs.c -o handy_calculs_exe")
    os.system("./handy_calculs_exe " + path[0] + " " + path[1])

    fen_princ.destroy()

def choseScenario():
    global monAffichageinput
    global lb
    global monBoutoninput

    window = [monAffichagep, monBoutonfile, monBoutoncurs, monBoutonpath]
    for i in window : i.destroy()

    monAffichageinput = Label(fen_princ, text = "Chose an existing scenario", width=70)
    monAffichageinput.pack()

    lb = Listbox(fen_princ)
    lb.insert(1, "Default society")
    lb.insert(2, "Egalitarian society")
    lb.insert(3, "Inequal society 1")
    lb.insert(4, "Inequal society 2")
    lb.insert(5, "Stable egalitarian society")
    lb.insert(6, "Stable equitable society 1")
    lb.insert(7, "Stable equitable society 2")
    lb.pack()

    monBoutoninput = Button(fen_princ, text = "Validate scenario", command = sendScenario)
    monBoutoninput.pack()

def choseCursors():
    global curseurxc
    global monAffichagexc
    global monBoutonxc
    global curseurxe
    global monAffichagexe
    global monBoutonxe
    global curseurn
    global monAffichagen
    global monBoutonn
    global curseurw
    global monAffichagew
    global monBoutonw
    global monBoutonfinal
    global T

    XC = "XC stands for the commoner population ; this variable plays a prey role, with its predator being the Elite population, XE (see bellow)."
    XE = "XE stands for the elite population ; this variable has the XC's predator role. If set the value of XE is set to 0, meaning there is no Elite in the society, a 'Equal society' scenario is created."
    N = "N refers to the natural resources ; this variable coresponds to the amount of nature and has a 'prey' role, predated by Wealth."
    W = "W refers to the accumulated wealth ; this variable can either be set to 0 (meaning that no wealth has been accumulated yet), or to another value to represent a previous resources' accumulation."

    window = [monAffichagep, monBoutonfile, monBoutoncurs, monBoutonpath,T]
    for i in window : i.destroy()
    # Presentation
    monAffichagepresentation = Label(fen_princ, text = "You are about to create a scenario.\nPlease chose values for the four variables.\nParameters by default will be used.\n", width=70)
    monAffichagepresentation.pack()

    # XC
    textXC=Text(fen_princ, height = 2, width = 120)
    textXC.insert("3.0", XC)
    textXC.pack()

    curseurxc = Scale(fen_princ, orient='horizontal', from_ = 0, to = 10)
    curseurxc.pack()

    monAffichagexc = Label(fen_princ, text = "Value wanted for Commoner population", width=70)
    monAffichagexc.pack()

    monBoutonxc = Button(fen_princ, text = "Get value for Commoner population", command = afficherValeur_xc)
    monBoutonxc.pack()
    

    # XE
    textXE=Text(fen_princ, height = 2, width = 120)
    textXE.insert("3.0", XE)
    textXE.pack()

    curseurxe = Scale(fen_princ, orient='horizontal', from_ = 0, to = 20)
    curseurxe.pack()

    monAffichagexe = Label(fen_princ, text = "Value wanted for Elite population", width=70)
    monAffichagexe.pack()

    monBoutonxe = Button(fen_princ, text = "Get value for Elite population", command = afficherValeur_xe)
    monBoutonxe.pack()

    #N
    textN=Text(fen_princ, height = 2, width = 120)
    textN.insert("1.0", N)
    textN.pack()

    curseurn = Scale(fen_princ, orient='horizontal', from_ = 0, to = 5)
    curseurn.pack()

    monAffichagen = Label(fen_princ, text = "Value wanted for Amount of nature", width=70)
    monAffichagen.pack()

    monBoutonn = Button(fen_princ, text = "Get value for Amount of nature", command = afficherValeur_n)
    monBoutonn.pack()

    # W
    textW=Text(fen_princ, height = 2, width = 120)
    textW.insert("1.0", W)
    textW.pack()

    curseurw = Scale(fen_princ, orient='horizontal', from_ = 0, to = 15)
    curseurw.pack()

    monAffichagew = Label(fen_princ, text = "Value wanted for Amount of wealth", width=70)
    monAffichagew.pack()

    monBoutonw = Button(fen_princ, text = "Get value for Amount of wealth", command = afficherValeur_w)
    monBoutonw.pack()

    #Validate values
    monBoutonfinal = Button(fen_princ, text = "GOOOO", command = sendCursors)
    monBoutonfinal.pack()

def chosePath():
    global monAffichagepath
    global monBoutonpath
    global name_file

    window = [monAffichagep, monBoutonfile, monBoutoncurs, monBoutonpath]
    for i in window : i.destroy()

    monAffichagepath = Label(fen_princ, text = "Enter path of file", width=70)
    monAffichagepath.pack()
    
    name_file = Entry(fen_princ)
    name_file.pack()

    monBoutonpath = Button(fen_princ, text = "Validate path", command=sendPath)
    monBoutonpath.pack()

def questions():
    global monAffichagep
    global monBoutonfile
    global monBoutoncurs
    global monBoutonpath
    global T

    #finir texte intro avec présentation projet, explications variables + paramètres ET les 3 choix possibles pour user 
    welcome = "THE HANDY PROJECT"
    #Si possible, travailler sur le côté graphique/esthétique du texte 

    # First choices
    monAffichagep = Label(fen_princ, text = welcome, width=70)
    monAffichagep.config(font =("Courier", 40))
    monAffichagep.pack()

    T=Text(fen_princ, height = 8, width = 140)
    
    intro="Welcome to the handy project.The purpose of this project is to study the dynamics between human civilization and nature.\nThis simulation was created to observe, through different scenarios, the impact resources' distirbution can have on society,\nfollowing the collapsological theory.\n\nTo begin with, please select wether you prefer to work with an existing 'pre designed' scenario, or to create your own (you will be steered to chose values for the differents variables). You can also directly upload a files with your own values)\n\n WARNING : please make sure that your file is a comptatible txt file."
    T.insert('1.0', intro) #first argument := line.column
    T.pack()


    monBoutonfile = Button(fen_princ, text = "I want to chose an existing scenario", command = choseScenario)
    monBoutonfile.pack()

    monBoutoncurs = Button(fen_princ, text = "I want to create a scenario now", command = choseCursors)
    monBoutoncurs.pack()

    monBoutonpath = Button(fen_princ, text = "I want to upload my file", command = chosePath)
    monBoutonpath.pack()


if __name__=='__main__':
    fen_princ = Tk()

    fen_princ.attributes('-fullscreen', True)
    questions()
    fen_princ.mainloop()






# expliquer les variables 
# et la normalisation 

