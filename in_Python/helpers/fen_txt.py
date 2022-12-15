

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
