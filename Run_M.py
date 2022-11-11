#run adapted by us 

import os
import matplotlib.pyplot as plt
from HANDY import Model as HANDY


def main():
    """ Main loop for code execution"""

    fname = "params_stable_equitable_2.txt"
    model = HANDY(fname=fname)
    XC, XE, N, W = model.run_auto(norm=True)

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