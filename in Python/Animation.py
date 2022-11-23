import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,FFMpegFileWriter
from HANDY import Model as HANDY
from PIL import Image


# Création de la function qui sera appelée à "chaque nouvelle image"
def animate(k):

    ax[0].plot(t[:k*5], XC[:k*5], color = 'b')
    ax[0].plot(t[:k*5], XE[:k*5], color = 'r')
    ax[0].plot(t[:k*5], N[:k*5], color = 'g')
    ax[0].plot(t[:k*5], W[:k*5], color = 'k')

    ax[0].legend(["Commoner population", "Elite population", "Nature", "Wealth"])
    #rendre legende plus petite


    im_xc = Image.open('sample.jpeg') 
    im_xe = Image.open('sample.jpeg') 
    im_n = Image.open('sample.jpeg') 
    im_w = Image.open('sample.jpeg') 
    ax[1].clear()

    r_xc = XC[k]*2 + 1 #le coeff proportionnalité * 2 + la valeur min
    r_xe
    r_n
    r_w
    
    ax[1].imshow(im_xc, extent=[-r_xc+0.5, r_xc+0.5, -r_xc+0.5, r_xc+0.5])
    ax[1].imshow(im_xe, extent=[-r_xe-0.5, r_xe-0.5, -r_xe-0.5, r_xe-0.5])
    ax[1].imshow(im_n, extent=[-r_n+0.5, r_n+0.5, -r_n-0.5, r_n-0.5])
    ax[1].imshow(im_w, extent=[-r_w-0.5, r_w-0.5, -r_w+0.5, r_w+0.5])

    ax[1].axis("off")




    return ax

    

if __name__=='__main__':

    fname = "params_stable_equitable_2.txt"
    model = HANDY(fname=fname) #fichier trouvé

    t = [i for i in range(1000)]
    [XC, XE, N, W] = model.run_auto(norm=True)

    
# Création de la figure et de l'axe
    fig, ax = plt.subplots(1, 2, figsize=(10,5))

#Gestion des limites de la fenêtre
    ax[0].set_xlim(-20, 1020)
    ax[0].set_ylim(-0.03, 1.03)

    ani = FuncAnimation(fig=fig, func=animate, frames=range(len(t)), interval=1, repeat = False, blit=True)
    
    
    plt.show()


# enregistrer la vidéo ?
# courbe inclusive

