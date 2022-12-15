import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt
import numpy as np

#on devra normaliser par ça
norm_caca = 2
norm_nat = 20
#abscisses
time = 1000
t = [i for i in range(time)]

interface, ax = plt.subplots(figsize=(3.8,2.5))
    # Setting limits and resizing scale-axis
ax.set_xlim(-20, 1020)
ax.set_ylim(-0.05, 1.05) #axe nature

par1 = ax.twinx() # axe commoners
par2 = ax.twinx() # axe wealth

par1.set_ylim(-0.05, 1.05) #axe nature #axe nature
par2.set_ylim(-0.05, 1.05) #axe nature

# par1.set_ylim(0.06, 1.06) #il faut les décaler par rapport à nature qui est au centre
# par2.set_ylim(-0.09, 0.94)

# [t.set_color('orange') for t in ax.yaxis.get_ticklabels()]

# [t.set_color('green') for t in par1.yaxis.get_ticklabels()] #couleur marche pas 
# [t.set_color('grey') for t in par2.yaxis.get_ticklabels()] # couleur marche pas 

par1.yaxis.set_ticks_position('left') #les mettre à gauche
par2.yaxis.set_ticks_position('left')

y_N_ticks = [0, 0.5, 1] #seulement les trois valeurs affihées sur l'axe
y_N_ticks_label = [0, 0.5, 1]

y_XC_ticks = [-0.05, 0.45, 0.95]
y_XC_ticks_label = [0, norm_caca//2, norm_caca]

y_W_ticks = [0.09, 0.82, 1.55]
y_W_ticks_label = [0, norm_nat//2, norm_nat]
ax.set_yticks(y_N_ticks, labels=y_N_ticks_label)
par1.set_yticks(y_XC_ticks,  labels=y_XC_ticks_label)
par2.set_yticks(y_W_ticks, labels=y_W_ticks_label)

ax.tick_params(axis='y', labelcolor='g', length=0) #réduire taille ds valeurs
par1.tick_params(axis='y', labelcolor='orange', length=0)
par2.tick_params(axis='y', labelcolor='grey', length=0)


# caca_m = 75000 // 75000 #afficher la ligne horizontale
# ax.axhline(y=caca_m, color='orange', linestyle='--', label = "Carrying Capacity")
# ax.legend(loc='upper left', bbox_to_anchor=(-0.15, -0.06),
#         fancybox=True, shadow=True, ncol=4, fontsize='xx-small')

plt.show()



