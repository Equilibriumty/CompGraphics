from matplotlib import pyplot as plt
import numpy as np
import math


def draw_lines():
    plt.xlabel("X")
    plt.ylabel("Y")
    x = np.linspace(-1, 1, num=1000)
    plt.grid(axis="both")
    y1 = np.vectorize(lambda x: 0.0011 * math.acos(x))
    y2 = np.vectorize(lambda x: 0.0011 * math.atan(x))
    y3 = np.vectorize(lambda x: 0.0011 * math.asin(x))
    plt.plot(x, y1(x))
    plt.plot(x, y2(x))
    plt.plot(x, y3(x))
    plt.show()


draw_lines()
