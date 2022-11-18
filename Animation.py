import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,FFMpegFileWriter
from HANDY import Model as HANDY

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r', animated=True)
f = np.linspace(0, 1000, 200)

def init():
    ax.set_xlim(-3, 3)
    ax.set_ylim(-0.25, 2)
    ln.set_data(xdata,ydata)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.exp(-frame**2))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=f,
                    init_func=init, blit=True, interval = 2.5,repeat=False)
plt.show()

mywriter = FFMpegFileWriter(fps=25,codec="libx264")
ani.save("test.mp4", writer=mywriter)