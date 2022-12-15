import numpy as np


def resultAnalysis(nbr:int):
    resultTxt = 0
    if nbr == 1:
        text1 = """
        Your personnal modelisation leads to a:
        TYPE-N COLLAPSE.
        
        Nature is over-exploited by Commoners 
        to sustain themselves and Elites.
        It has reached zero.
        Accumulated Wealth is not sufficient to 
        save humans who all die of famine.
        Carrying capacity is too far-away from
        the maximum one (1) 
        """
        resultTxt = text1
    if nbr == 2:
        text2 = """
        Your personnal modelisation leads to a:
        TYPE-L COLLAPSE.

        Humans do not pick enough Nature ressources
        and accumulated Wealth is not sufficient.
        They all die: first Commoners then Elites.
        Nature can prosperate.
        """
        resultTxt = text2
    if nbr == 3:
        text3 = """
        Your personnal modelisation leads to a:
        TYPE-N REVERSIBLE COLLAPSES.

        Nature first reaches zero.
        Humans start dying of famine.
        Nature can recover.
        Humans recover too.
        Until Nature reaches zero...
        """
        resultTxt = text3
    if nbr == 4:
        text4 = """
        Your personnal modelisation leads to an:
        EQUILIBRIUM.

        Total Population reaches equilibirum under 
        maximum carrying capacity.
        Difference with the optimal:
        Earth will host less Humans and less Nature.
        """
        resultTxt = text4
    return resultTxt


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