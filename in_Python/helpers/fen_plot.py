import numpy as np
import matplotlib.pyplot as plt
import os

def graphTemplate(ax, norm_CC, norm_N):

    ax.set_xlim(-20, 1020)
    ax.set_ylim(-0.05, 1.05)
    ax.set_xlabel("Time (y)", fontsize = 5)
    ax.xaxis.set_label_coords(1.08, -0.023)
    par1 = ax.twinx() # axe commoners
    par2 = ax.twinx() # axe wealth
    par1.set_ylim(-0.05, 1.05) #axe nature #axe nature
    par2.set_ylim(-0.05, 1.05) #axe nature
    par1.yaxis.set_ticks_position('left') #les mettre à gauche
    par2.yaxis.set_ticks_position('left')
    y_N_ticks = [0, 0.5, 1] #seulement les trois valeurs affihées sur l'axe
    y_N_ticks_label = ["0 λ", "0.5 λ","1 λ"]
    y_XC_ticks = [0.09, 0.82, 1.55]
    y_XC_ticks_label = ["0 χ", str(norm_CC//2)+" χ", str(norm_CC)+" χ"]
    y_W_ticks = [-0.05, 0.45, 0.95]
    y_W_ticks_label = ["0 χ", str(norm_N//2)+" λ", str(norm_N)+" λ"]
    ax.set_yticks(y_N_ticks, labels=y_N_ticks_label)
    par1.set_yticks(y_XC_ticks,  labels=y_XC_ticks_label)
    par2.set_yticks(y_W_ticks, labels=y_W_ticks_label)
    ax.tick_params(axis='y', labelcolor='g', length=0) #réduire taille ds valeurs
    par1.tick_params(axis='y', labelcolor='orange', length=0)
    par2.tick_params(axis='y', labelcolor='grey', length=0)
    ax.tick_params(axis='x', labelsize=5)
    ax.tick_params(axis='y', labelsize=5)
    par1.tick_params(axis='y', labelsize=5)
    par2.tick_params(axis='y', labelsize=5)
    ax.grid(which='minor', alpha=0.1)
    ax.grid(which='major', alpha=0.1)

def animation(k, ax, t, XC, XE, N, W, CC, mx_CC):

    if k==0:
        ax.legend(loc='upper left', bbox_to_anchor=(0.2, -0.06),
        fancybox=True, shadow=True, ncol=5, fontsize=5)
    if k==1:
        ax.axhline(y=CC/mx_CC, color='orange', linestyle='--', label = "Carrying Capacity")

    ax.plot(t, XC, color = 'b', label = "Commoner population")
    ax.plot(t, XE, color = 'r', label = "Elite population")
    ax.plot(t, N, color = 'g', label = "Nature")
    ax.plot(t, W, color = 'grey', label = "Wealth")
    