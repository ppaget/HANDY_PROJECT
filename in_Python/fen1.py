from tkinter import *
import os

def quit():
    fen_princ.destroy()
def send_egalitarianScenario():
    path = ['eg_f', "../Text/HANDY_egalitarian_basic.txt"]

    os.chdir("in_C")
    os.system("gcc HANDY_calculs.c -o handy_calculs_exe")
    os.system("./handy_calculs_exe " + path[0] + " " + path[1])

    fen_princ.destroy()

def send_equitableScenario():
    path = ['eq_f', "../Text/HANDY_equitable_basic.txt"]

    os.chdir("in_C")
    os.system("gcc HANDY_calculs.c -o handy_calculs_exe")
    os.system("./handy_calculs_exe " + path[0] + " " + path[1])

    fen_princ.destroy()

def send_unequalScenario():
    path = ['un_f', "../Text/HANDY_unequal_basic.txt"]

    os.chdir("in_C")
    os.system("gcc HANDY_calculs.c -o handy_calculs_exe")
    os.system("./handy_calculs_exe " + path[0] + " " + path[1])

    fen_princ.destroy()

def go_egalitarianScenario():
    global enter_egalitarian_label
    global enter_egalitarian_button

    window = [elite_button, egalitarian_button]
    for i in window : i.destroy()

    egalitarian_summary = """You have chosen a scenario with no Elite Population.
                            This means you will enter the Egalitarian Scenario.\n
                            Ready?"""

    enter_egalitarian_label = Label(fen_princ, text = egalitarian_summary, width=70)
    enter_egalitarian_label.grid(row=0,column=0)

    enter_egalitarian_button = Button(fen_princ, text = "Start the Egalitarian Modelisation!", command = send_egalitarianScenario)
    enter_egalitarian_button.grid(row=1,column=0)

def go_equitableScenario():
    global enter_equitable_label
    global enter_equitable_button

    window = [elite_button, egalitarian_button, equitable_button, unequal_button]
    for i in window : i.destroy()

    equitable_summary = """You have chosen a scenario with an Elite Population which is payed
                            as much as the Commoner Population.
                            This means you will enter the Equitable Scenario.\n
                            Ready?"""

    enter_equitable_label = Label(fen_princ, text = equitable_summary, width=70)
    enter_equitable_label.grid(row=0,column=0)

    enter_equitable_button = Button(fen_princ, text = "Start the Equitable Modelisation!", command = send_equitableScenario)
    enter_equitable_button.grid(row=1,column=0)

def go_unequalScenario():
    global enter_unequal_label
    global enter_unequal_button

    window = [elite_button, egalitarian_button, equitable_button, unequal_button]
    for i in window : i.destroy()

    unequal_summary = """You have chosen a scenario with an Elite Population which is payed
                            more than the Commoner Population.
                            This means you will enter the Unequal Scenario.\n
                            Ready?"""

    enter_unequal_label = Label(fen_princ, text = unequal_summary, width=70)
    enter_unequal_label.grid(row=0,column=0)

    enter_unequal_button = Button(fen_princ, text = "Start the Unequal Modelisation!", command = send_unequalScenario)
    enter_unequal_button.grid(row=1,column=0)

def questionK():
    global question2_label
    global equitable_button
    global unequal_button

    window = [elite_button, egalitarian_button]
    for i in window : i.destroy()

    question2 = """You have chosen a scenario with an Elite Population.\n
                    Second choice: Do you want the Elite and the Commoner Populations to be paid equally,\n
                    with no difference in their salaries?"""

    question2_label = Label(fen_princ, text = question2, width=70)
    question2_label.grid(row=0,column=0)

    equitable_button = Button(fen_princ, text = "I want the two to be paid equally", command = go_equitableScenario)
    equitable_button.grid(row=1,column=0)

    unequal_button = Button(fen_princ, text = "I do not want the two to be paid equally", command = go_unequalScenario)
    unequal_button.grid(row=2,column=0)

def questionXE():
    global question1_label
    global egalitarian_button
    global elite_button

    window = [welcome_label, go_button, end_button]
    for i in window : i.destroy()

    question1 = """First choice: Do you want an Elite Population in the scenario?"""

    # First choices
    question1_label = Label(fen_princ, text = question1, width=70)
    question1_label.grid(row=0,column=0)

    elite_button = Button(fen_princ, text = "I want an Elite Population", command = questionK)
    elite_button.grid(row=1,column=0)

    egalitarian_button = Button(fen_princ, text = "I do not want an Elite population", command = go_egalitarianScenario)
    egalitarian_button.grid(row=2,column=0)

def introduction():
    global welcome_label
    global go_button
    global end_button


    #finir texte intro avec présentation prjet, explications variables + paramètres ET les 3 choix possibles pour user 
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

                    
            You will be asked to make choices about the variables and parameters
            so you can try different types of scenario.\n\n   
            """

    welcome_label = Label(fen_princ, text = text_welcome)
    welcome_label.pack()

    go_button = Button(fen_princ, text = "Let's get started!", command = questionXE)
    go_button.pack()
    end_button = Button(fen_princ, text = "Quit Model", command = quit)
    end_button.pack()


if __name__=='__main__':

    fen_princ = Tk()
    fen_princ.attributes('-fullscreen', True)
    introduction()

    fen_princ.mainloop()