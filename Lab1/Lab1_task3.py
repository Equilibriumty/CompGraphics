from matplotlib import pyplot as plt
import numpy as np
import math
plt.axes()

def draw_lines():
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.xlim(0, 1)
    plt.ylim(-0.2, 0.2)
    plt.grid()
    x = np.linspace(-1, 1, num=1000)
    y1 = np.vectorize(lambda x: 0.11 * math.acos(x))
    y2 = np.vectorize(lambda x: 0.11 * math.atan(x))
    y3 = np.vectorize(lambda x: 0.11 * math.asin(x))
    plt.plot(x, y1(x))
    plt.plot(x, y2(x))
    plt.plot(x, y3(x))
    plt.show()

draw_lines()
