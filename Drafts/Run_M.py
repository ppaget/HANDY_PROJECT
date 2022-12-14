#run adapted by us to read from c file 

import os
import numpy as np
import matplotlib.pyplot as plt


def main():
    """ Main loop for plotting """

    fname = "/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/in_C/results_python_file.txt" #modifier le nom

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


    plt.plot(range(len(XC)), XC, label="Commoner Population", color='b')
    plt.plot(range(len(XE)), XE, label="Elite Population", color='r')
    plt.plot(range(len(N)), N, label="Nature", color='g')
    plt.plot(range(len(W)), W, label="Wealth", color='k')
    plt.legend()
    plt.savefig('.'.join(fname.split('.')[:-1])+'.pdf') #graph.pdf
    plt.close()
    os.system("open " + '.'.join(fname.split('.')[:-1])+'.pdf') #open graph.pdf --> essentiel pour afficher graphe


if __name__ == '__main__':
     main()