# First displayed window.

from tkinter import *
from PIL import ImageTk, Image
from helpers.fen_os import sendScenario
from helpers.fen_services import moveButton, cleanTk
from helpers.fen_txt import titleFen1, welcomeTxtFen1, question1Fen1, summaryTxtFen1, question2Fen1

def startScenario(scenario:str, w1, w2, w3):
    """ Summary text annouces which scenario is chosen.
    Path to HANDY_calculs.c.
    """
    # Different cleaning according to answer
    if scenario=="eg":
        cleanTk(w1, w2, w3,None)
    if scenario=="eq" or scenario=="un":
        cleanTk(w1,w2,w3,None)

    summaryTxt = summaryTxtFen1(scenario)
    startlabel = Label(fen_princ, text = summaryTxt, bg="indianred", font=('Yu Gothic',30, "bold"))
    startlabel.place(x=800, y=350)

    # Calls function to run HANDY_calculs.c with chosen scenario
    startbutton = Button(fen_princ, text = "START!", fg= 'darkred', bg="navajowhite", font=('Yu Gothic',30, "bold"),command = lambda : sendScenario(fen_princ, scenario))
    startbutton.place(x=850, y=600)

def questionK(w1,w2,w3):
    """ Ask second question about inequalitiesto lead either to equitable or unequal scenario. """

    cleanTk(w1,w2,w3,None)

    question2 = question2Fen1()

    q2_label = Label(fen_princ, text = question2, fg= 'darkred', bg="navajowhite", font=('Yu Gothic',30, "bold"))
    q2_label.place(x=630, y=400)
    eq_button = Button(fen_princ, text = "YES", fg= 'darkred', bg="navajowhite", font=('Yu Gothic',30, "bold"),command = lambda:startScenario("eq",q2_label, eq_button, un_button))
    eq_button.place(x=820, y=600)
    un_button = Button(fen_princ, text = "NO", fg= 'darkred', bg="navajowhite", font=('Yu Gothic',30, "bold"),command = lambda:startScenario("un",q2_label, eq_button, un_button))
    un_button.place(x=920, y=600)

def questionXE(w1, w2, w3, w4):
    """ Ask first question about elite population to lead either to egalitarian scenario or second question. """

    # Cleaning old widgets
    cleanTk(w1, w2, w3, w4)
    # Prepared text
    question1 = question1Fen1()
    # Displaying text
    q1_label = Label(fen_princ, text = question1, fg= 'darkred', bg="navajowhite", font=('Yu Gothic',30, "bold"))
    q1_label.place(x=650, y=400)
    # Buttons to continue
    XE_button = Button(fen_princ, text = "YES",fg= 'darkred', bg="navajowhite", font=('Yu Gothic',30, "bold"),command = lambda:questionK(q1_label, XE_button, eg_button))
    XE_button.place(x=820, y=600)
    eg_button = Button(fen_princ, text = "NO",fg= 'darkred', bg="navajowhite", font=('Yu Gothic',30, "bold"),command = lambda:startScenario("eg", q1_label, XE_button, eg_button))
    eg_button.place(x=920, y=600)

def introduction():
    """ First welcoming window.
    Goals: Explain main goals of the model
           Explain variables
           Start interactive interface """

    # Prepared texts and display them
    title, subtitle = titleFen1()
    welcomeTxt = welcomeTxtFen1()

    titlelabel = Label(fen_princ, text=title, fg= 'darkred', bg="navajowhite", font=('Yu Gothic',50, "bold")).pack()
    subtitlelabel = Label(fen_princ, text=subtitle, fg= 'darkred', bg="navajowhite", font=('Yu Gothic',25, "bold")).pack()
    welcome_label = Label(fen_princ,bg="navajowhite", text = welcomeTxt, font=('Yu Gothic',15, "bold"))
    welcome_label.place(x=650, y=250)

    # Start with questions
    go_button = Button(fen_princ, text = "GO!", fg= 'darkred',font=('Yu Gothic',50, "bold"), command = lambda:questionXE(titlelabel, subtitlelabel, welcome_label, go_button))
    go_button.place(x= 830, y=650)



if __name__=='__main__':
    """ First Tkinter interactive interface.
    Goals: Contain explanations of project.
           Ask questions to user to lead to one of three scenarios: egalitarian, equitable or unequal.
           Send file containing initial datas for chosen scenario to HANDY_calculs.c to modelize datas in next window.
           End by destroying window and C file continues. """

    # Creation of Tkinter window
    fen_princ = Tk()
    fen_princ.attributes('-fullscreen', True)
    fen_princ.configure(bg="navajowhite")

    # Button to quit
    moveButton(fen_princ, 1, "")

    # Display image
    canvas= Canvas(fen_princ, width= 500 , height= 520, bg='navajowhite', highlightthickness=0)
    canvas.place(x=100, y=250)
    img= (Image.open("Images/fire.png"))
    #Resize image
    resized_image= img.resize((464,472), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    #Add image to the Canvas Items
    canvas.create_image(20, 20,anchor=NW,image=new_image)

    # Only one function called because buttons call functions themselves
    introduction()

    # Displays the first window
    fen_princ.mainloop()