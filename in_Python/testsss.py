from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time
from tkinter import *


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


if __name__=='__main__':

    time = 1000
    skip = 20
    fname = "/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/in_C/results_python_file.txt"
    [XC, XE, N, W, variables, parameters] = readFile(fname)
    t = [i for i in range(time-1)]

    interface, ax = plt.subplots(1, 2, figsize=(6.5,3))

    ax[0].set_xlim(-20, 1020)
    ax[0].set_ylim(-0.03, 1.03)

    ax[0].plot(t, XC, color = 'b', label = "Commoner population")
    ax[0].plot(t, XE, color = 'r', label = "Elite population")
    ax[0].plot(t, N, color = 'g', label = "Nature")
    ax[0].plot(t, W, color = 'k', label = "Wealth")
    
    ax[0].legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
        fancybox=True, shadow=True, ncol=4)

    plt.show()

