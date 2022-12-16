# Helper to plot.

def graphTemplate(ax, norm_CC:int, norm_N:int):
    """Graphic template for every displayed graph.

    Args:
        ax: ax being modified
        norm_CC (int): normalisation for population
        norm_N (int): normalisation for nature and wealth
    """

    ax.set_xlim(-20, 1020)
    ax.set_ylim(-0.05, 1.05)
    ax.set_xlabel("Time (y)", fontsize = 5)
    ax.xaxis.set_label_coords(1.08, -0.023)
    par1 = ax.twinx() # axe y commoners
    par2 = ax.twinx() # axe y wealth
    par1.set_ylim(-0.05, 1.05)
    par2.set_ylim(-0.05, 1.05)
    par1.yaxis.set_ticks_position('left') #les mettre à gauche
    par2.yaxis.set_ticks_position('left')
    y_N_ticks = [0, 0.5, 1] # location of displayed values
    y_N_ticks_label = ["0 λ", "0.5 λ","1 λ"] # displayed values
    y_XC_ticks = [0.09, 0.82, 1.55] # commoners
    y_XC_ticks_label = ["0 χ", str(norm_CC/2)+" χ", str(norm_CC)+" χ"]
    y_W_ticks = [-0.05, 0.45, 0.95] #wealth
    y_W_ticks_label = ["0 χ", str(norm_N/2)+" λ", str(norm_N)+" λ"]
    ax.set_yticks(y_N_ticks, labels=y_N_ticks_label) #combinate
    par1.set_yticks(y_XC_ticks,  labels=y_XC_ticks_label)
    par2.set_yticks(y_W_ticks, labels=y_W_ticks_label)
    ax.tick_params(axis='y', labelcolor='g', length=0) #color
    par1.tick_params(axis='y', labelcolor='hotpink', length=0) 
    par2.tick_params(axis='y', labelcolor='grey', length=0)
    ax.tick_params(axis='x', labelsize=5) #size
    ax.tick_params(axis='y', labelsize=5)
    par1.tick_params(axis='y', labelsize=5)
    par2.tick_params(axis='y', labelsize=5)
    ax.grid(which='minor', alpha=0.1) #grid
    ax.grid(which='major', alpha=0.1)

def animation(k:int, ax, t:list, XC:list, XE:list, N:list, W:list, CC_printed:float):
    """Animates our graph over time using frames and FuncAnimation.

    Args:
        k (int): used to display things once
        ax: axe being modified
        t (list): x-axis
        XC (list): y-axis commoners
        XE (list): y-axis elites
        N (list): y-axis nature
        W (list): y-axis wealth
        CC_printed (float): y-axis straight line carrying capacity
    """

    if k==0:
        ax.axhline(y=CC_printed, color='orange', linestyle='--', label = "Carrying Capacity")

    if k==1:
        ax.legend(loc='upper left', bbox_to_anchor=(-0.165, -0.069),
        fancybox=True, shadow=True, ncol=5, fontsize=4.2)

    ax.plot(t, XC, color = 'b', label = "Commoner population")
    ax.plot(t, XE, color = 'r', label = "Elite population")
    ax.plot(t, N, color = 'g', label = "Nature")
    ax.plot(t, W, color = 'grey', label = "Wealth")
    