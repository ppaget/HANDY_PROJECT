import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,FFMpegFileWriter
from PIL import Image


# Création de la fonction qui sera appelée à "chaque nouvelle image"
def animate(k):

    ax[0].plot(t[:k*5], XC[:k*5], color = 'b')
    ax[0].plot(t[:k*5], XE[:k*5], color = 'r')
    ax[0].plot(t[:k*5], N[:k*5], color = 'g')
    ax[0].plot(t[:k*5], W[:k*5], color = 'k')

    ax[0].legend(["Commoner population", "Elite population", "Nature", "Wealth"])
    #rendre legende plus petite

    im_xc = Image.open("in Python/sample.jpeg") 

    """im_xe = Image.open('sample.jpeg') 
    im_n = Image.open('sample.jpeg') 
    im_w = Image.open('sample.jpeg')"""

    ax[1].clear() #Permet d'éviter la superposition d'images de tailles diff

    ax[1].set_xlim([-3,3])
    ax[1].set_ylim([-3,3])

    r_xc = XC[k]*2 + 1 # le "coeff proportionnalité" (=valeur de la col à indice k) * 2 + la valeur min
    r_xe = XE[k]*2 + 1
    r_n = N[k]*2 + 1
    r_w = W[k]*2 + 1
    
    ax[1].imshow(im_xc, extent=[-r_xc, r_xc, -r_xc, r_xc]) #image en carré ; 0,5 = éloignement par rapport au centre 
    """ ax[1].imshow(im_xe, extent=[-r_xe-0.5, r_xe-0.5, -r_xe-0.5, r_xe-0.5])
    ax[1].imshow(im_n, extent=[-r_n+0.5, r_n+0.5, -r_n-0.5, r_n-0.5])
    ax[1].imshow(im_w, extent=[-r_w-0.5, r_w-0.5, -r_w+0.5, r_w+0.5])"""

    ax[1].axis("off")



def readFile(fname):

    array = np.genfromtxt(fname, delimiter=', ', dtype='float64')
    XC = array[:,0]
    XE = array[:,1]
    N = array[:,2]
    W = array[:,3]

    return [XC, XE, N ,W]

if __name__=='__main__':

    time = 1000
    fnameM = "/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/in Python/results_python.txt"
    fnameP = "/Users/peppa/Desktop/Ba3/CMT/PROJECT/HANDY_PROJECT/in C/results_python.txt"
    [XC, XE, N, W] = readFile(fnameP)
    t = [i for i in range(time)]
    
# Création de la figure et de l'axe
    interface, ax = plt.subplots(1, 2, figsize=(10,5))

#Gestion des limites de la fenêtre
    ax[0].set_xlim(-20, 1020)
    ax[0].set_ylim(-0.03, 1.03)
    

    ani = FuncAnimation(fig = interface, func = animate, frames = range(time), interval = 1, repeat = False)

    
    plt.show()


# enregistrer la vidéo ?
# courbe inclusive
