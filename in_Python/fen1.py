from tkinter import *
from helpers.fen_os import Py2C
from helpers.fen_services import quit

def sendScenario(scenario: str):
    path = 0
    if scenario == "eg":
        path = ['eg_f', "Text/HANDY_egalitarian_basic.txt"]
    if scenario == "eq":
        path = ['eq_f', "Text/HANDY_equitable_basic.txt"]
    if scenario == "un":
        path = ['un_f', "Text/HANDY_unequal_basic.txt"]
    Py2C(path, fen_princ)

def egalitarianScenario():
    """ Activated by button.
    Goals: Announce to user which scenario is chosen.
           Creates a button to start running C file.
    Same for each scenario. """

    # Cleaning old widgets
    window = [question1_label, elite_button, egalitarian_button]
    for i in window : i.destroy()

    egalitarian_summary = """

    You have chosen a scenario with no Elite Population.
    This means you will enter the Egalitarian Scenario.



    Ready?
    
    """

    enter_egalitarian_label = Label(fen_princ, text = egalitarian_summary)
    enter_egalitarian_label.pack()
    enter_egalitarian_button = Button(fen_princ, text = "Start the Egalitarian Modelisation!", command = lambda : sendScenario("eg"))
    enter_egalitarian_button.pack()

def equitableScenario():

    window = [elite_button, egalitarian_button, equitable_button, unequal_button]
    for i in window : i.destroy()

    equitable_summary = """

    You have chosen a scenario with an Elite Population which is
    payed as much as the Commoner Population.
    This means you will enter the Equitable Scenario.



    Ready?
    
    """

    enter_equitable_label = Label(fen_princ, text = equitable_summary)
    enter_equitable_label.pack()
    enter_equitable_button = Button(fen_princ, text = "Start the Equitable Modelisation!", command = lambda : sendScenario("eq"))
    enter_equitable_button.pack()

def unequalScenario():

    window = [elite_button, egalitarian_button, equitable_button, unequal_button]
    for i in window : i.destroy()

    unequal_summary = """

    You have chosen a scenario with an Elite Population which is
    payed more than the Commoner Population.
    This means you will enter the Unequal Scenario.



    Ready?
    
    """
    enter_unequal_label = Label(fen_princ, text = unequal_summary)
    enter_unequal_label.pack()
    enter_unequal_button = Button(fen_princ, text = "Start the Unequal Modelisation!", command = lambda : sendScenario("un"))
    enter_unequal_button.pack()

def questionK():
    """ Activated by button.
    Goal: Ask second question about inequality factor to lead either to equitable or unequal scenario. """

    # Globalisation of widgets so they can be destroyed later
    global question2_label
    global equitable_button
    global unequal_button

    window = [question1_label, elite_button, egalitarian_button]
    for i in window : i.destroy()

    question2 = """

    You have chosen a scenario with an Elite Population.\n
    Second choice: Do you want the Elite and the Commoner Populations to be paid equally,
    with no difference in their salaries?
    
    """

    question2_label = Label(fen_princ, text = question2)
    question2_label.pack()
    equitable_button = Button(fen_princ, text = "YES", command = equitableScenario)
    equitable_button.pack()
    unequal_button = Button(fen_princ, text = "NO", command = unequalScenario)
    unequal_button.pack()

def questionXE():
    """ Activated by button.
    Goal: Ask first question about elite population to lead either to egalitarian scenario or second question. """

    global question1_label
    global egalitarian_button
    global elite_button

    window = [welcome_label, go_button, end_button]
    for i in window : i.destroy()

    question1 = """


    First choice: Do you want an Elite Population in the scenario?
    
    """
    question1_label = Label(fen_princ, text = question1)
    question1_label.pack()
    elite_button = Button(fen_princ, text = "YES", command = questionK)
    elite_button.pack()
    egalitarian_button = Button(fen_princ, text = "NO", command = egalitarianScenario)
    egalitarian_button.pack()

def introduction():
    """ First welcoming window.
    Goals: Explain main goals of the model
           Explain variables and parameters
           Start the interactive interface """

    global welcome_label
    global go_button
    global end_button

    text_welcome = """   


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

    welcome_label = Label(fen_princ, text = text_welcome)
    welcome_label.pack()
    go_button = Button(fen_princ, text = "GO!", command = questionXE)
    go_button.pack()
    end_button = Button(fen_princ, text = "Quit", command = lambda : quit(fen_princ))
    end_button.pack()


if __name__=='__main__':
    """ Called by RUN_HANDY.
    This file is the first Tkinter interactive interface.
    Goals: Contain explanations of project
           Ask questions to user to lead to one of three scenarios: egalitarian, equitable or unequal.
           Send file containing initial datas for chosen scenario to HANDY_calculs.c to modelize datas in next window.
           Three sets of datas lead to optimal equilibrium.
           Possibility to definitely quit program. 
           End by destroying window and C file continues. """

    # Creation of Tkinter window
    fen_princ = Tk()
    fen_princ.attributes('-fullscreen', True)

    # Only one function called because buttons call functions themselves
    introduction()

    # Displays the first window
    fen_princ.mainloop()