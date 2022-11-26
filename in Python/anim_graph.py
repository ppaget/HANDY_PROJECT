import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,FFMpegFileWriter
from HANDY import Model as HANDY
from PIL import Image

def animate(k):

    ax.plot(t[:k*5], XC[:k*5], color = 'b')
    ax.plot(t[:k*5], XE[:k*5], color = 'r')
    ax.plot(t[:k*5], N[:k*5], color = 'g')
    ax.plot(t[:k*5], W[:k*5], color = 'k')

    ax.legend(["Commoner population", "Elite population", "Nature", "Wealth"])
    #rendre legende plus petite


def readFile(fname):

    array = np.genfromtxt(fname, delimiter=', ', dtype='float64')
    XC = array[:,0]
    XE = array[:,1]
    N = array[:,2]
    W = array[:,3]

    return [XC, XE, N ,W]

if __name__=='__main__':

    fname = "/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/in Python/results_python.txt"
    [XC, XE, N, W] = readFile(fname)
    t = [i for i in range(1000)]

    
# Création de la figure et de l'axe
    fig, ax = plt.subplots()

#Gestion des limites de la fenêtre
    ax.set_xlim(-20, 1020)
    ax.set_ylim(-0.03, 1.03)

    ani = FuncAnimation(fig=fig, func=animate, frames=range(len(t)), interval=1, repeat = False)
    
    
    plt.show()

