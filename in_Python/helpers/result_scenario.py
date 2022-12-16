import numpy as np


def resultAnalysis(nbr:int):

    if nbr == 1:
        title = """ TYPE-N COLLAPSE """
        N_coll = """
        CC too far away from optimal.
        Nature over-exploited...
        """
        return title, N_coll
    if nbr == 2:
        title = """ TYPE-L COLLAPSE """
        L_coll = """
        CC too far away from optimal.
        Not enough workers...
        """
        return title, L_coll
    if nbr == 3:
        title = """ TYPE-N REVERSIBLE COLLAPSES """
        N_rev = """
        Turning point...
        """
        return title, N_rev
    if nbr == 4:
        title = """ EQUILIBRIUM """
        equi = """
        Acceptable CC...
        """
        return title, equi


def resultScenario(XC:list,N:list):

    scenario = 0
    zero = float(0)
    if zero in N :
        zero_1 = np.where(N==zero)
        i0 = zero_1[0][0]
        max1 = max(N[i0+1:])
        iM = np.where(N==max1)[0][0]
        zero_2 = np.where(N[iM+1:]==zero)
        i1 = zero_2[0][0] 
        max2 = max(N[i1+1:])
        if abs(max1-max2)<0.5: #valeur seuil
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
    return resultAnalysis(scenario)