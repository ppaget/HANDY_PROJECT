#Fonction pour déterminer et afficher l'issue du scénario

# 1 = Type N Collapse
# 2 = Type L Collapse 
# 3 = Reversible type N Collapse 
# 4 = equilibrium 
from HANDY_REAL import readFile
import numpy as np
zero = float(0)

#List[0]=XC
#List[2]=N

def finalText(File):

    [XC,XE,N,W, lol, mdr]= readFile(File)
    global scenario

    if zero in N :
        result = np.where(N==zero)
        i0 = result[0][0] #4 de différence car on a rajouté 2 lignes

        M = max(N[i0+1:])
        iM = np.where(N==M)[0][0] 

        if zero in XC[i0+1:iM+10] :
            scenario = 3
        elif N[998]==0 :
            scenario = 1
        else :
            scenario = 4
    else :
        if XC[998]<=0.1 : #Valeur de seuil car on ne voit pas totalement la collapse dans le uneq_1
            scenario = 2
        else : 
            scenario = 4

    print(scenario)

if __name__=='__main__':
    #finalText("results_python_file.txt")
    finalText("results_python_file.txt")  
