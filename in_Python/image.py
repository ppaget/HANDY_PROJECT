import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from PIL import Image

# regarde d'abord le main avant cette fct
def plot_dynamic(i): # pour la i eme timestep
    # on plot à gauche sur la figure les i eme premier points de f (le sinus) 
    ax[0].plot(x[:i], f[:i], 'r')

    # maintenant l'image sur le droite de la figure
    # on calcul la taile de l'image en fonction de la valeur de f. 
    # abs(sinus) compris entre 0 et 1 donc quand f est max r = 0.6 et f min r=0.05
    r = f[i]*0.55 + 0.05
    # on clear la figure pour enlever le cercle d'avant
    ax[1].clear()
    # limites des axes
    ax[1].set_xlim([-1, 1])
    ax[1].set_ylim([-1.25, 1.25])
    # on affiche l'image centrer en (0, 0) avec les bord de -r a r pour x et y (l'image c'est un carré)
    ax[1].imshow(img, extent=[-r+0.5, r+0.5, -r, r])
    ax[1].imshow(img, extent=[-r-0.5, r-0.5, -r, r])
    # enleve les axes de gauche sinon c'est moche
    ax[1].axis("off")


if __name__=='__main__':
    # on va tracer valeur absolue de sinus entre 0 et 500 avec l'image qui grossis en fonction
    # avec une periode de 2pi/500
    x = np.linspace(0, 500, 100)
    f = np.abs(np.sin(x*(2*np.pi)/(500)))

    # creation de la figure avec 2 subplot
    # en gros on a ax = [ax0, ax1] avec ax0 les axes de gauche et ax1 axes de droite
    # si tu veux plot sur l'axe de gauche tu fais ax[0].plot
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 3))
    # fixe les axes de la première figure
    ax[0].set_xlim([0, 500]) # x compris entre 0 et 500
    ax[0].set_ylim([0, 1]) # y entre 0 et 1 -> abs(sin)
    # plt.axis("equal") # pour avoir des subplot carré

    # ouvre l'image qu'on va afficher à coté 
    img = Image.open("in_Python/im1.jpg")

    # fonction d'animation à chaque timestep elle va appeler plot dynamic avec i qui augmente
    # interval 1 c'est pour dire que y a 1 ms entre chaque interval
    # fig c'est pour plot sur la figure qu'on a defini au dessus
    animator = ani.FuncAnimation(fig, plot_dynamic, interval=1)
    plt.show()
