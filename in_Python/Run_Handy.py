# Test for Git

#  See "A Minimal Model for Human and Nature Interaction",
#  Safa Motesharrei, Jorge Rivas, Eugenia Kalnay,
#  November 13, 2012

import sys
import os
import matplotlib.pyplot as plt
from HANDY import Model as HANDY


def main():
    """ Main loop for code execution"""
    fname = "/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/Text/Egalitarian/HANDY_params_default.txt"
    model = HANDY(fname=fname) #fichier trouvé
    XC, XE, N, W = model.run_auto(norm=True)

    plt.plot(range(len(XC)), XC, label="Commoner Population", color='b')
    plt.plot(range(len(XE)), XE, label="Elite Population", color='r')
    plt.plot(range(len(N)), N, label="Nature", color='g')
    plt.plot(range(len(W)), W, label="Wealth", color='k')
    plt.legend()
    plt.savefig('.'.join(fname.split('.')[:-1])+'.pdf') #graph.pdf
    plt.close()
    os.system("open " + '.'.join(fname.split('.')[:-1])+'.pdf') #open graph.pdf


if __name__ == '__main__':

    main()