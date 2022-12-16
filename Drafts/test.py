#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk

#Create an instance of tkinter frame
fen_princ = Tk()

#Set the geometry of tkinter frame
fen_princ.attributes(
    '-fullscreen', True)
fen_princ.configure(bg='red')

#Create a canvas
canvas= Canvas(fen_princ, width= 500 , height= 650, bg='red')
canvas.pack()

#Load an image in the script
img= (Image.open("Images/fire.png"))

#Resize the Image using resize method
resized_image= img.resize((464,472), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(20, 100,anchor=NW,image=new_image)

fen_princ.mainloop()

# 580 590