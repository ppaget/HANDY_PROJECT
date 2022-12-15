import os

def Py2C(stock, fen_princ):
    os.system("gcc in_C/HANDY_calculs.c -o in_C/handy_calculs_exe")
    os.system("./in_C/handy_calculs_exe " + stock[0] + " " + stock[1])
    fen_princ.destroy()
