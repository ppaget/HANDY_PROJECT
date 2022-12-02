import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from PIL import Image


def test(): 
    fig, ax = plt.subplots()
    ax.axis("off")
    ax.text(0.3,0.5, 'We have reached a collapse', style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
    plt.show()
test()