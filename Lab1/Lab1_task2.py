import pylab
from math import sin, cos
from matplotlib import lines, patches

def drawLine(axes, xrange, yrange, color="orange"):
    line = lines.Line2D(xrange, yrange, color=color)
    axes.add_line(line)

def drawPolyg(axes, xyrange, color="orange"):
    polyg = patches.Polygon(xyrange, fill=False, color=color)
    axes.add_patch(polyg)

if __name__ == "__main__":
    pylab.xlim(-4, 4)
    pylab.ylim(-3.1, 3.1)
    pylab.grid()

    axes = pylab.gca()
    coef = 0.75
    shift = ((-coef, 0), (0, coef), (coef, 0), (0, -coef))
    colors = ("red", "blue", "yellow", "green")
    for r in range(4):
        drawLine(axes, [-2+shift[r][0]+cos(i / 150) for i in range(1000)],
                        [shift[r][1]+sin(i / 150) for i in range(1000)])

        drawPolyg(axes, [(2 + shift[r][0] + cos(i / 15), shift[r][1] + sin(i / 15)) for i in range(100)],
                    color=colors[r])
    pylab.show()