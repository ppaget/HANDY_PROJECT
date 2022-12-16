# Helper to analyze results of personnal modelisation.

import numpy as np


def resultAnalysis(nbr:int):
    """ Texts of description about potential ends of modelisation. """

    if nbr == 1:
        title = """ TYPE-N COLLAPSE """
        N_coll = """
        CC too far away from optimal.
        Nature over-depleted...
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
        Accumulated wealth saves humans.
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
    """Determines how the society ends.

    Args:
        XC (list): commoners
        N (list): nature

    Returns:
        int: call adequate text function
    """

    scenario = 0
    zero = float(0)
    if zero in N :
        # look for first zero of N
        zero_1 = np.where(N==zero)
        i0 = zero_1[0][0]
        # look for next max
        max1 = max(N[i0+1:])
        iM = np.where(N==max1)[0][0]
        # second zero after max
        zero_2 = np.where(N[iM+1:]==zero)
        i1 = zero_2[0][0] 
        # second max
        max2 = max(N[i1+1:])
        if abs(max1-max2)<0.5: #if consecutive maximums are very closed
            scenario = 3 #reversible type-N
        elif N[998]==0 : # nature is zero at the end
            scenario = 1  # type-N
        else :
            scenario = 4 # equilibrium
    else : # if nature never reaches zero
        if XC[998]<=0.1 : # commoners are zero at the end
            scenario = 2 # type-L
        else : 
            scenario = 4 # equilibrium
    return resultAnalysis(scenario)