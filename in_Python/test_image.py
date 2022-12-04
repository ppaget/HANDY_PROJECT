import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from PIL import Image
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os


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

test()


# skip_header=2