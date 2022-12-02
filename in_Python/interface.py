import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,FFMpegFileWriter
from PIL import Image
import os


def readFile(fname):

    array = np.genfromtxt(fname, delimiter=', ', dtype='float64')
    XC = array[:,0]
    XE = array[:,1]
    N = array[:,2]
    W = array[:,3]

    return [XC, XE, N ,W]

def finalText():
    ax[1].clear()
    ax[1].axis("off")
    ax[1].text(0.3, 0.5, 'We have reached a collapse', style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

# Création de la fonction qui sera appelée à "chaque nouvelle image"
def animate(k):

    s = k*skip

    ax[0].plot(t[:s], XC[:s], color = 'b')
    ax[0].plot(t[:s], XE[:s], color = 'r')
    ax[0].plot(t[:s], N[:s], color = 'g')
    ax[0].plot(t[:s], W[:s], color = 'k')

    ax[0].legend(["Commoner population", "Elite population", "Nature", "Wealth"])
    #rendre legende plus petite

    ax[1].clear() #Permet d'éviter la superposition d'images de tailles diff

    r_xc = XC[s]*0.5 + 0.05 # le "coeff proportionnalité" (=valeur de la col à indice k) * 2 + la valeur min
    # r_xe = XE[s]*0.5 + 0.05
    # r_n = N[s]*0.5 + 0.05
    # r_w = W[s]*0.5 + 0.05

    ax[1].set_xlim([-1,1]) # Définit un cadre pour l'image 
    ax[1].set_ylim([-1,1])
    ax[1].axis("off")
    
    ax[1].imshow(im_xc, extent=[-r_xc-0.5, r_xc-0.5, -r_xc-0.5, r_xc-0.5]) #image en carré ; 0,5 = éloignement par rapport au centre 
    # ax[1].imshow(im_xe, extent=[-r_xe-0.5, r_xe-0.5, -r_xe+0.5, r_xe+0.5])
    # ax[1].imshow(im_n, extent=[-r_n+0.5, r_n+0.5, -r_n+0.5, r_n+0.5])
    # ax[1].imshow(im_w, extent=[-r_w+0.5, r_w+0.5, -r_w-0.5, r_w-0.5])


    if k==time//skip - 1 :
        finalText()

if __name__=='__main__':

    # Importations données graph+im
    print("Entering in interface")
    time = 1000
    skip = 5

    fnameMfile = "/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/in_C/results_python_file.txt"
    fnameMcurs = "/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/in_C/results_python_cursors.txt"
    fnameP = "/Users/peppa/Desktop/Ba3/CMT/PROJECT/HANDY_PROJECT/in_C/results_python_file.txt"
    [XC, XE, N, W] = readFile(fnameMfile)
    t = [i for i in range(time)]

    interface, ax = plt.subplots(1, 2, figsize=(13,6.5))

    ax[0].set_xlim(-20, 1020)
    ax[0].set_ylim(-0.03, 1.03)

    im_xc = Image.open("/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/Images/im1.jpg") 
    # im_xe = Image.open("images/im2.jpg")
    # im_n = Image.open("images/im3.jpg") 
    # im_w = Image.open("images/im4.jpg") 

    ani = FuncAnimation(fig = interface, func = animate, frames = range(time//skip), interval = 1, repeat = False)

    plt.axis("equal")
    plt.show()


# enregistrer la vidéo ?
# courbe inclusive
