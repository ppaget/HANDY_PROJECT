import os

def Py2C(fen_princ, stock):
    os.system("gcc in_C/HANDY_calculs.c -o in_C/handy_calculs_exe")
    os.system("./in_C/handy_calculs_exe " + stock[0] + " " + stock[1])
    fen_princ.destroy()



def sendScenario(fen_princ, scenario:str):
    path = 0
    if scenario == "eg":
        path = ['eg_f', "Text/HANDY_egalitarian_basic.txt"]
    if scenario == "eq":
        path = ['eq_f', "Text/HANDY_equitable_basic.txt"]
    if scenario == "un":
        path = ['un_f', "Text/HANDY_unequal_basic.txt"]
    Py2C(fen_princ, path)



def sendCursors(fen_princ, scenario, cursorCC):

    cursor = 0
    if scenario == "eg":
        cursor = ["eg_c", str(cursorCC.get())]
    if scenario == "eq":
        cursor = ["eq_c", str(cursorCC.get())]
    if scenario == "un":
        cursor = ["un_c", str(cursorCC.get())]
    Py2C(fen_princ, cursor)
