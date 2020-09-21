import matplotlib
from matplotlib import pyplot as plt
from matplotlib import pylab
plt.axes()


def draw_rectangles():
    for i in range(5):
        line = plt.Line2D((3-i, 3-i), (12-i, 14+i), lw=2, color="black")
        line2 = plt.Line2D((3-i, 10+i), (12-i, 12-i), lw=2, color="black")
        plt.gca().add_line(line)
        plt.gca().add_line(line2)
    for i in range(5):
        line3 = plt.Line2D((10+i, 10+i), (12-i, 14+i), lw=2, color="black")
        line4 = plt.Line2D((3-i, 10+i), (14+i, 14+i), lw=2, color="black")
        plt.gca().add_line(line3)
        plt.gca().add_line(line4)


def draw_circles(axes):
    for i in range(6):
        circleX = matplotlib.patches.Ellipse((0, 0), width=7.5+i,height=4+i, fill=False, lw=2)
        axes.add_patch(circleX)


pylab.xlim(-20, 20)
pylab.ylim(-20, 20)
pylab.grid()
axes = pylab.gca()
axes.set_aspect("equal")
draw_rectangles()
draw_circles(axes)
plt.axis('scaled')
plt.show()