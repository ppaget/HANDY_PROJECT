import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,FFMpegFileWriter
from PIL import Image
import matplotlib.image as mpimg


# Création de la fonction qui sera appelée à "chaque nouvelle image"

img = mpimg.imread('sample.jpeg')
imgplot = plt.imshow(img)
plt.show()
    #im_xc.clear() #Permet d'éviter la superposition d'images de tailles diff

    # r_xc = XC[k]*2 + 1 # le "coeff proportionnalité" (=valeur de la col à indice k) * 2 + la valeur min
    # r_xe = XE[k]*2 + 1
    # r_n = N[k]*2 + 1
    # r_w = W[k]*2 + 1
    
    # im_xc.imshow(im_xc, origin = 'lower', extent=(-0.5, r_xc, -0.5, r_xc)) #image en carré ; 0,5 = éloignement par rapport au centre 
    # """ ax[1].imshow(im_xe, extent=[-r_xe-0.5, r_xe-0.5, -r_xe-0.5, r_xe-0.5])
    # ax[1].imshow(im_n, extent=[-r_n+0.5, r_n+0.5, -r_n-0.5, r_n-0.5])
    # ax[1].imshow(im_w, extent=[-r_w-0.5, r_w-0.5, -r_w+0.5, r_w+0.5])"""

    # ax.axis("off")
    # plt.show()

# if __name__=='__main__':

# # Création de la figure et de l'axe
#     ax = plt.subplots(1, 2, figsize=(10,5))

# #Gestion des limites de la fenêtre
#     ax[0].set_xlim(-20, 1020)
#     ax[0].set_ylim(-0.03, 1.03)

#     ani = FuncAnimation(fig = im_xc, func = animate, frames = range(time), interval = 1, repeat = False)

    
#     plt.show()


# enregistrer la vidéo ?
# courbe inclusive
