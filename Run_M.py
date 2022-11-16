#run adapted by us to read from c file 

import os
import numpy as np
import matplotlib.pyplot as plt
from HANDY import Model as HANDY


def main():
    """ Main loop for plotting """

    fname = "params_stable_equitable_2.txt" #modifier le nom

    array = np.genfromtxt(fname, delimiter=' ', dtype='float64') #ouvrir
    XC = array[:,0]
    XE = array[:,1]
    N = array[:,2]
    W = array[:,3]


    plt.plot(range(len(XC)), XC, label="Commoner Population", color='b')
    plt.plot(range(len(XE)), XE, label="Elite Population", color='r')
    plt.plot(range(len(N)), N, label="Nature", color='g')
    plt.plot(range(len(W)), W, label="Weatlth", color='k')
    plt.legend()
    plt.savefig('.'.join(fname.split('.')[:-1])+'.pdf') #graph.pdf
    plt.close()
    os.system("open " + '.'.join(fname.split('.')[:-1])+'.pdf') #open graph.pdf --> essentiel pour afficher graphe


if __name__ == '__main__':
     main()