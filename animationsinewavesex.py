import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()
x = np.arange(0,2*np.pi,0.01)
line, =ax.plot(x,np.sin(x))
line1, =ax.plot(x,np.cos(x))
def animate(i):
    line.set_ydata(np.sin(x+i/10.0))
    line1.set_ydata(np.cos(x+i/10.0))
    return line,line1,

def init():
    line.set_ydata(np.ma.array(x,mask=True))
    line1.set_ydata(np.ma.array(x, mask=True))
    return line,line1,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
                                interval=25, blit=True)
plt.show()