# Helper for prepared texts. Window is given.
# Type of scenario often needed to display right text.


def titleFen1():
    title = """   
        WELCOME TO HANDY PROJECT!"""

    subtitle ="""
    Modeling inequality and use of resources in the collapse or sustainability of societies.
"""
    return title, subtitle

def welcomeTxtFen1():
      
    welcomeTxt=    """   
    Only four variables to simulate human life on earth!

    - Commoner Population (XC)
    - Elite Population (XE)
    - Nature (N)
    - accumulated Wealth (W)
            


    To detect a collapse, we will use:

    - Carrying Capacity (CC): number of humans nature can carry
                


    Chose your society and play!
    Will you reach an equilibrium or a collapse..?   
        """
    return welcomeTxt

def question1Fen1():
    question1 = """
    Do you want Elites in your society?
    """
    return question1
    
def question2Fen1():
    question2 = """
    Same salaries for Commoners and Elites?
    """
    return question2

def summaryTxtFen1(scenario:str):
    summaryTxt = 0
    if scenario=="eg":
        summaryTxt = """
  Your scenario:  
  EGALITARIAN.
    """
    if scenario=="eq":
        summaryTxt = """
  Your scenario:  
  EQUITABLE.
    """
    if scenario=="un":
        summaryTxt = """
  Your scenario:  
  UNEQUAL.  
    """
    return summaryTxt

def welcomeTxtFen2(scenario:str):


    """ Called by main function.
    Goal: Generate text to explain variables and parameters of chosen scenario.
    Args : scenario (str): name of scenario to select corresponding text.
    Returns: text_welcome: corresponding text. """

    if scenario == "eg":
        title = """ EGALITARIAN EQUILIBRIUM """
        text_welcome = """
    XC(0): 100  
    XE(0): 0    
    N(0): 100   
    K: 0 
"""
        CCtxt = """  CC optimal: 1  """
        return title, text_welcome, CCtxt

    if scenario == "eq":
        title = """ EQUITABLE EQUILIBRIUM """
        text_welcome = """
    XC(0): 100  
    XE(0): 25   
    N(0): 100   
    K: 1 
"""
        CCtxt = """  CC optimal: 0.8  """
        return title, text_welcome, CCtxt

    if scenario == "un":
        title = """ UNEQUAL COLLAPSE """
        text_welcome = """
    XC(0): 100    
    XE(0): 0.2    
    N(0): 100   
    K: 100 
"""
        CCtxt = """  CC optimal: 1  """
        return title, text_welcome, CCtxt

def descrCCFen2():

    txtCC = """
Chose another
Carrying Capacity
and see!
            """
    return txtCC

def hintsFen2(scenario):

    hints = 0
    if scenario=="eg":
        hints = """
    Hints:
    CC = 0.5    
    CC = 0.3    
    """
    if scenario=="eq":
        hints = """
    Hints:
    CC = 0.6    
    CC = 0.3
    """
    if scenario=="un":
        hints = """
    Hints:
    CC = 0.5    
    CC = 0.3
    """
    return hints

def remindersFen3(scenario:str, CC:float):
    
    if scenario == "eg" :
        title = """EGALITARIAN"""
        _, reminder_f, reminderCC_f = welcomeTxtFen2("eg")
        newCC_c = """NEW CC: """ + str(CC)
        return title, reminder_f, reminderCC_f, newCC_c

    if scenario == "eq" :
        title = """EQUITABLE"""
        _, reminder_f, reminderCC_f = welcomeTxtFen2("eq")
        newCC_c = """NEW CC: """ + str(CC)
        return title, reminder_f, reminderCC_f, newCC_c

    if scenario == "un" :
        title = """UNEQUAL"""
        _, reminder_f, reminderCC_f = welcomeTxtFen2("un")
        newCC_c = """NEW CC: """ + str(CC)
        return title, reminder_f, reminderCC_f, newCC_c
    

