#pour peps

from PIL import Image

# creating a object
im = Image.open('sample.jpeg')
  
im.show()


#la photo en pixel arrive, il faudra la resize en fonction du facteur depuis XC
#pixel(0, i+facteur)
#c'est pas direct resize mais 

image.thumbnail((500,500), Image.ANTIALIAS)