from graphics import *
import numpy as np
import math as mt
from math import *
import copy

screenX = 800
screenY = 800
st = 200
Pyramid = np.array([[0, 0, 0, 1],
                     [st, 0, 0, 1],
                     [st / 2, 0, st, 1],
                     [st / 2, -st, st, 1], ])


def cantor(n):
    return [0.] + cant(0., 1., n) + [1.]


def cant(x, y, n):
    if n == 0:
        return []

    new_pts = [2. * x / 3. + y / 3., x / 3. + 2. * y / 3.]
    return cant(x, new_pts[0], n - 1) + new_pts + cant(new_pts[1], y, n - 1)


def XY(Figure):
    f = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])
    ft = f.T
    Prxy = Figure.dot(ft)
    return Prxy


def XYZ(Figure, l, m, n):
    f = np.array([[1, 0, 0, l], [0, 1, 0, m], [0, 0, 1, n], [1, 0, 0, 1]])
    ft = f.T
    Prxy = Figure.dot(ft)
    return Prxy


def InsX(Figure, TetaG):
    TetaR = (3 / 14 * TetaG) / 180
    f = np.array(
        [[1, 0, 0, 0], [0, mt.cos(TetaR), mt.sin(TetaR), 0], [0, -mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 0, 1]])
    ft = f.T
    Prxy = Figure.dot(ft)
    return Prxy


def dimetrij(Figure, TetaG1, TetaG2):
    TetaR1 = (3 / 14 * TetaG1) / 180
    TetaR2 = (3 / 14 * TetaG2) / 180
    f1 = np.array(
        [[mt.cos(TetaR1), 0, -mt.sin(TetaR1), 0], [0, 1, 0, 0], [mt.sin(TetaR1), 0, mt.cos(TetaR1), 1], [0, 0, 0, 0], ])
    ft1 = f1.T
    Prxy1 = Figure.dot(ft1)
    f2 = np.array(
        [[1, 0, 0, 0], [0, mt.cos(TetaR2), mt.sin(TetaR2), 0], [0, -mt.sin(TetaR2), mt.cos(TetaR2), 0], [0, 0, 0, 1]])
    ft2 = f2.T
    Prxy2 = Prxy1.dot(ft2)
    return Prxy2


def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def draw_helper(win, level, p1, p2, p3):
    if level == 1:

        obj = Polygon(Point(p1[0], p1[1]), Point(p2[0], p2[1]), Point(p3[0], p3[1]))
        obj.setFill("red")
        obj.draw(win)
    else:
        p4 = midpoint(p1, p2)
        p5 = midpoint(p2, p3)
        p6 = midpoint(p1, p3)
        draw_helper(win, level - 1, p1, p4, p6)
        draw_helper(win, level - 1, p4, p2, p5)
        draw_helper(win, level - 1, p6, p5, p3)


def draw(win, size):
    level = int(10)
    obj = Rectangle(Point(0, 0), Point(size + 5, size + 5))
    obj.setFill("")
    obj.draw(win)
    triangle_height = int(round(size * sqrt(3.0) / 2.0))
    p1 = (2, triangle_height + 3)
    p2 = (2 + size / 2, 3)
    p3 = (2 + size, triangle_height + 3)
    draw_helper(win, level, p1, p2, p3)


def colorize_lines(x1, y1, x2, y2):
    color1 = 435676
    DX = x2 - x1
    DY = y2 - y1
    sG_x = 1 if DX > 0 else -1 if DX < 0 else 0
    sG_y = 1 if DY > 0 else -1 if DY < 0 else 0
    if DX < 0: DX = -DX
    if DY < 0: DY = -DY
    if DX > DY:
        pDX, pDY = sG_x, 0
        es, el = DY, DX
    else:
        pDX, pDY = 0, sG_y
        es, el = DX, DY
    x, y = x1, y1
    error, t = el / 2, 0

    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sG_x
            y += sG_y
        else:
            x += pDX
            y += pDY
        t += 1
        obj = Point(x, y)
        color1_S = str(color1)
        color1_S = "#" + color1_S
        obj.setFill(color1_S)
        obj.draw(win)
        color1 = color1 - 40
    return colorize_lines


def lines(Prxy):
    Ax = Prxy[0, 0]
    Ay = Prxy[0, 1]
    Bx = Prxy[1, 0]
    By = Prxy[1, 1]
    Ix = Prxy[2, 0]
    Iy = Prxy[2, 1]
    Mx = Prxy[3, 0]
    My = Prxy[3, 1]
    colorize_lines(Bx, By, Mx, My)
    colorize_lines(Ix, Iy, Mx, My)
    colorize_lines(Mx, My, Bx, By)

    colorize_lines(Ax, Ay, Mx, My)
    colorize_lines(Ix, Iy, Mx, My)
    colorize_lines(Ax, Ay, Ix, Iy)
    colorize_lines(Bx, By, Ix, Iy)
    colorize_lines(Ax, Ay, Bx, By)
    colorize_lines(Ix, Iy, Ax, Ay)


while True:
    size = 1000
    win = GraphWin("Зображення фракталу Серпінського та піраміди", size, size)
    win.setBackground('grey')
    draw(win, size)
    xw = 700
    yw = 1000
    st = 200
    TetaG1 = 90
    TetaG2 = -90
    l = (xw) - st
    m = (yw) - st
    n = m
    Pyramid1 = XYZ(Pyramid, l, m, n)
    Pyramid2 = dimetrij(Pyramid1, TetaG1, TetaG2)
    Prxy3 = XY(Pyramid2)
    lines(Prxy3)
    win.getMouse()
    win.close()

    y = 0
    size = 1000
    win = GraphWin("Зображення фракталу Кантора та піраміди", size, size - 200)
    win.setBackground('black')
    for i in range(10):
        p = copy.deepcopy(cantor(i))
        print(p)
        w = 0
        for j in range(int((len(p)) / 2)):
            line = Line(Point(p[w] * 1000, y), Point(p[w + 1] * 1000, y))
            w += 2
            line.setFill("cyan")
            line.setWidth(25)
            line.draw(win)

        y += 80

    xw = 700
    yw = 1000
    st = 200
    TetaG1 = 90
    TetaG2 = -90
    l = (xw) - st
    m = (yw) - st
    n = m
    Pyramid1 = XYZ(Pyramid, l, m, n)
    Pyramid2 = dimetrij(Pyramid1, TetaG1, TetaG2)
    Prxy3 = XY(Pyramid2)
    lines(Prxy3)
    win.getMouse()
    win.close()
