import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from PIL import Image


def test(fname): 
    array = np.genfromtxt(fname, delimiter=', ', dtype="float64")
    variables = array[:,0]
    parameters = array[:,0]
    print(variables, parameters)
test("/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/in_C/results_python_cursors.txt")