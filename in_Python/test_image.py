import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from PIL import Image


def test(fname): 
    f = open(fname, "r")
    variables = [f.readline()]
    variables = variables[0].split(", ")
    variables

    print(variables)
test("/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/in_C/results_python_file.txt")


# skip_header=2