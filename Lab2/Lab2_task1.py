import time
from math import cos, sin
import graphics as gr
import numpy as np


class Romb(gr.Polygon):
    def __init__(self, mid, x, y, colour="red"):
        self.mid = mid
        self.x = x
        self.y = y
        self.colour = colour
        self.array_of_points = np.array([[mid[0], mid[1] - y/2, 1],
                                         [mid[0] - x/2, mid[1], 1],
                                         [mid[0], mid[1] + y/2, 1],
                                         [mid[0] + x/2, mid[1], 1]
                                         ])
        self.points = [gr.Point(point[0], point[1]) for point in self.array_of_points]
        gr.Polygon.__init__(self, self.points)
        self.setOutline(colour)
        self.setWidth(2)

    def movement(self, x_move, y_move):
        array_of_movement = np.array([[1,      0,     0],
                                      [0,      1,     1],
                                      [x_move, y_move,1]
                                      ])
        self.undraw()
        self.array_of_points = self.array_of_points.dot(array_of_movement)
        self.output(self.graphwin)

    def rotate(self, x_cos, y_sin):
        array_of_rotation = np.array([[x_cos,  y_sin, 0],
                                      [-y_sin, x_cos, 0],
                                      [0,      0,     1]
                                      ])
        self.undraw()
        self.array_of_points = self.array_of_points.dot(array_of_rotation)
        self.output(self.graphwin)

    def scale(self, x_scale, y_scale,):
        array_of_scailing = np.array([[x_scale, 0,      0],
                                      [0,      y_scale, 0],
                                      [0,      0,       1]
                                      ])
        self.undraw()
        self.array_of_points = self.array_of_points.dot(array_of_scailing)
        self.output(self.graphwin)

    def output(self, graphwin):
        self.graphwin = graphwin
        self.points = [gr.Point(point[0], point[1]) for point in self.array_of_points]
        gr.Polygon.__init__(self, self.points)
        self.setOutline(self.colour)
        self.setWidth(2)
        self.draw(graphwin)


def main():
    win = gr.GraphWin("Лабораторна робота №2", 1000, 1000)
    romb = Romb((150, 150), 100, 100)
    romb.output(win)
    romb.movement(100, 100)
    time.sleep(1)
    romb.rotate(cos(0.7), sin(0.3))
    time.sleep(1)
    romb.scale(2.5, 2.5)
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
