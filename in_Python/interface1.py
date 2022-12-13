import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,FFMpegFileWriter
from PIL import Image
import argparse


parser = argparse.ArgumentParser(description="File sent from C")
parser.add_argument("--fileName", type=str, help="fichier C", default="in_C/results_python_file.txt")

def readFile(fname):

    array = np.genfromtxt(fname, delimiter=', ', skip_header=3, dtype=float)
    XC = array[:,0]
    XE = array[:,1]
    N = array[:,2]
    W = array[:,3]
    f = open(fname, "r")
    variables = [f.readline()]
    variables = variables[0].split(", ")
    parameters = [f.readline()]
    parameters = parameters[0].split(", ")
    
    return [XC, XE, N ,W, variables, parameters]

def stateText():
    ax[0].axis("off")
    text1 = "Initial variables: \n\nCommoner population: "+xc+"\nElite population: "+xe+"\nAmount of nature: "+n+"\nAmount of wealth: "+w+"\n\n"
    text2 = "Parameters : \n\nMinimum death rate: "+am+"\nMaximal death rate= "+aM+"\nCommoner birth rate: "+bc+"\nElite birth rate: "+be+"\nNature regeneration factor: "+g+"\nNature's capacity: "+l+"\nSubsistence salary: "+s+"\nNature depletion factor: "+d+"\nDifference in consuption factor: "+k+"\nMinimum required consumption: "+r+"\n"
    ax[0].text(0.3,0.5, s=text1+text2)

def finalText():
    ax[2].clear()
    ax[2].axis("off")
    if W[999] and N[999] == 0 :
        conclusion_text = "We have reached a collapse.\n\nThis is both a type-N and a type-L collapse."
    if N[999] == 0 :
        conclusion_text = "We have reached a collapse.\n\nThis is a type-N collapse."
    if W[999] == 0 :
        conclusion_text = "We have reached a collapse.\n\nThis is a type-L collapse."
    ax[2].text(0.3, 0.5, s= conclusion_text, style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

# Création de la fonction qui sera appelée à "chaque nouvelle image"
def animate(k):
    if k==0:
        ax[0].legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=4)

    s = k*skip

    ax[0].plot(t[:s], XC[:s], color = 'b', label = "Commoner population")
    ax[0].plot(t[:s], XE[:s], color = 'r', label = "Elite population")
    ax[0].plot(t[:s], N[:s], color = 'g', label = "Nature")
    ax[0].plot(t[:s], W[:s], color = 'k', label = "Wealth")

    # line.set_xdata = t[:s]
    # line.set_ydata = XC[:s]
    # return line,

    # ax[0].legend(["Commoner population", "Elite population", "Nature", "Wealth"])
    #rendre legende plus petite

    # ax[2].clear() #Permet d'éviter la superposition d'images de tailles diff

    # r_xc = XC[s]*0.5 + 0.05 # le "coeff proportionnalité" (=valeur de la col à indice k) * 2 + la valeur min
    # # r_xe = XE[s]*0.5 + 0.05
    # # r_n = N[s]*0.5 + 0.05
    # # r_w = W[s]*0.5 + 0.05

    # ax[2].set_xlim([-1,1]) # Définit un cadre pour l'image 
    # ax[2].set_ylim([-1,1])
    # ax[2].axis("off")
    
    # ax[2].imshow(im_xc, extent=[-r_xc-0.5, r_xc-0.5, -r_xc-0.5, r_xc-0.5]) #image en carré ; 0,5 = éloignement par rapport au centre 
    # # ax[2].imshow(im_xe, extent=[-r_xe-0.5, r_xe-0.5, -r_xe+0.5, r_xe+0.5])
    # # ax[2].imshow(im_n, extent=[-r_n+0.5, r_n+0.5, -r_n+0.5, r_n+0.5])
    # # ax[2].imshow(im_w, extent=[-r_w+0.5, r_w+0.5, -r_w-0.5, r_w-0.5])


    # if k==time//skip - 1 :
    #     finalText()

if __name__=='__main__':
    
    print("emilouche")
    args = parser.parse_args()

    # Importations données graph+im
    time = 1000
    skip = 5
    
    [XC, XE, N, W, variables, parameters] = readFile(args.fileName)
    t = [i for i in range(time)]

    # xc = variables[1]
    # xe = variables[2]
    # n = variables[3]
    # w = str(float(variables[4]))
    # am = parameters[1]
    # aM = parameters[2]
    # bc = parameters[3]
    # be = parameters[4]
    # g = parameters[5]
    # l = parameters[6]
    # s = parameters[7]
    # d = parameters[8]
    # k = parameters[9]
    # r = str(float(parameters[10]))

    interface, ax = plt.subplots(1, 2, figsize=(13,6.5))

    # stateText()

<<<<<<< HEAD:in_Python/interface.py
    ax[1].set_xlim(-20, 1020)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    ax[1].set_ylim(-0.03, 1.03)
=======
    ax[0].set_xlim(-20, 1020)
    ax[0].set_ylim(-0.03, 1.03)
    ax[1].axis("off")

    # line, = ax[0].plot(0,0)
>>>>>>> 6c9557dbf66a1ff7252723efc79603398e9c9e7b:in_Python/interface1.py

    #im_xc = Image.open("/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/Images/im1.jpg") 
    # im_xc = Image.open("../Images/im1.jpg") 
    
    # im_xe = Image.open("images/im2.jpg")
    # im_n = Image.open("images/im3.jpg") 
    # im_w = Image.open("images/im4.jpg") 

    ani = FuncAnimation(fig = interface, func = animate, frames = range(time//skip), interval = 1, repeat = False)

    # plt.axis("equal")
    
    plt.show()


# enregistrer la vidéo ?
# courbe inclusive

   
    # fnamePfile = "/Users/peppa/Desktop/Ba3/CMT/PROJECT/HANDY_PROJECT/in_C/results_python_file.txt"
    # fnamePcurs = "/Users/peppa/Desktop/Ba3/CMT/PROJECT/HANDY_PROJECT/in_C/results_python_curs.txt"
    # fnameMcurs = "/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/in_C/results_python_cursors.txt"