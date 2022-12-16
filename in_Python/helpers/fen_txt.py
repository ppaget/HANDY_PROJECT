

def welcomeTxtFen1():
        
    welcomeTxt=    """   


        WELCOME TO THE HANDY PROJECT!\n\n

    The purpose of this project is to study the dynamics between human
    civilization and nature, following the collapsological theory.
    This simulation, based on a predator-prey model, only uses four
    variables and ten parameters.


    The four variables are:

    - the Commoner Population --> predators - workers take direct ressources from Nature
    - the Elite Population --> predators - non-workers take indirect ressources from Nature
    - the Nature --> prey - ressources for food, energy
    - the accumulated Wealth --> unique to human civilization - resilience from famine
            

        The parameters that control variables are:

    - normal and famine death rates --> control total population
    - commoners and elites birth rates --> control total population
    - subsistence salary per capita --> control wealth
    - threshold wealth per capita --> control wealth
    - regeneration rate of nature --> control nature
    - nature carrying capacity --> control nature

    - inequality factor, K --> difference in wealth between commoners and elites
    - depletion per capita, D --> commoners direct and elites indirect impacts on nature

    - carrying capacity --> number of humans nature can carry
                
    You will be asked to make choices about the variables and parameters
    so you can try different types of scenario.
    They may lead to equilibrium or collapses of society.\n\n   
        """
    return welcomeTxt

def question1Fen1():
    question1 = """


    First choice: Do you want an Elite Population in the scenario?
    
    """
    return question1
    

def question2Fen1():
    question2 = """

    You have chosen a scenario with an Elite Population.\n
    Second choice: Do you want the Elite and the Commoner Populations to be paid equally,
    with no difference in their salaries?
    
    """
    return question2

def summaryTxtFen1(scenario:str):
    summaryTxt = 0
    if scenario=="eg":
        summaryTxt = """

    You have chosen a scenario with no Elite Population.
    This means you will enter the Egalitarian Scenario.



    Ready?
    
    """
    if scenario=="eq":
        summaryTxt = """

    You have chosen a scenario with an Elite Population which is
    payed as much as the Commoner Population.
    This means you will enter the Equitable Scenario.



    Ready?
    
    """
    if scenario=="un":
        summaryTxt = """

    You have chosen a scenario with an Elite Population which is
    payed more than the Commoner Population.
    This means you will enter the Unequal Scenario.



    Ready?
    
    """
    return summaryTxt


def welcomeTxtFen2(scenario:str):


    """ Called by main function.
    Goal: Generate text to explain variables and parameters of chosen scenario.
    Args : scenario (str): name of scenario to select corresponding text.
    Returns: text_welcome: corresponding text. """

    if scenario == "eg":
        text_welcome = """
                    WELCOME TO YOUR EGALITARIAN SCENARIO!

                    Here is the modelisation which results in a soft-landing to OPTIMAL EQUILIBRIUM.

                    Used values:
                        - Initial Commoner population: 100
                        - Initial Elite population: 0

                        - Inequality factor: 0 
                        - Depletion per capita: D_reference

                    All other values are typical.
                D_optimal is the minimum depletion that maximizes the carrying capacity.
                (ideal: only in EGALITARIAN scenario)
                Be careful about normalisation on y-axis!"""
        return text_welcome

    if scenario == "eq":
        text_welcome = """
                WELCOME TO YOUR EQUITABLE SCENARIO!

                Here is the modelisation which results in a soft-landing to OPTIMAL EQUILIBRIUM.

                Used values:
                    - Initial Commoner population: 100
                    - Initial Elite population: 25

                    - Inequality factor: 1 
                    - Depletion per capita: D_reference*1.25
                    
                All other values are typical.
                D_optimal is the minimum depletion that maximizes the carrying capacity.
                (ideal: only in EGALITARIAN scenario)
                Be careful about normalisation on y-axis!

                    """
        return text_welcome

    if scenario == "un":
        text_welcome = """
                WELCOME TO YOUR UNEQUAL SCENARIO!

                Here is the modelisation which results in a soft-landing to OPTIMAL EQUILIBRIUM.

                Used values:
                    - Initial Commoner population: 10 000
                    - Initial Elite population: 3 000
                    - Commoner birth rate: 0.0065 (other scenarios: 0.03)
                    - Elite birth rate: 0.02 (other scenarios: 0.03)

                    - Inequality factor: 10 
                    - Depletion per capita: D_reference*0.95
                    
                All other values are typical.
                D_optimal is the minimum depletion that maximizes the carrying capacity.
                (ideal: only in EGALITARIAN scenario)
                Be careful about normalisation on y-axis!"""
        return text_welcome

def remindersFen3(scenario:str, CC:float):
    reminder1 = 0
    if scenario == "eg" :
        reminder_eg = """
        EGALITARIAN MODELISATION WITH CHOICES
        
        Used values for OPTIMAL EQUILIBRIUM:
            - Initial Commoner population: 100
            - Initial Elite population: 0
            - Inequality factor: 0 
            - Depletion per capita: D_reference """

        reminder1 = reminder_eg

    if scenario == "eq" :
        reminder_eq = """
        EQUITABLE MODELISATION WITH CHOICES
        
        Used values for OPTIMAL EQUILIBRIUM:
            - Initial Commoner population: 100
            - Initial Elite population: 25
            - Inequality factor: 1 
            - Depletion per capita: D_reference*1.25 """

        reminder1 = reminder_eq

    if scenario == "un" :
        reminder_un = """
        EQUITABLE MODELISATION WITH CHOICES
        
        Used values for OPTIMAL EQUILIBRIUM:
            - Initial Commoner population: 10 000
            - Initial Elite population: 3 000
            - Commoner birth rate: 0.0065 (other scenarios: 0.03)
            - Elite birth rate: 0.02 (other scenarios: 0.03)
            - Inequality factor: 10 
            - Depletion per capita: D_reference*0.95
            """
        reminder1 = reminder_un
    
    reminder2 = """New Carrying Capicity: """ + str(CC)

    return reminder1, reminder2

def descrCCFen2():

    txtCC = """
            You can now chose to vary a starting parameter:
                the CARRYING CAPACITY.

            It represents the number oh humans earth can carry.
            If it goes away too far away from its optimal value:
            COLLAPSE!

            Try yourself!
            """
    return txtCC

def hintsFen2(scenario):
    hints = 0
    if scenario=="eg":
        hints = """Hints:
        You could try with:
            d = 2.5
            d = 4
            d = 5.5
            """
    if scenario=="eq":
        hints = """Hints:
        You could try with:
            d = 2.5
            d = 4
            d = 5.5
            """
    if scenario=="un":
        hints = """Hints:
        You could try with:
            d = 2.5
            d = 4
            d = 5.5
            """
    return hints