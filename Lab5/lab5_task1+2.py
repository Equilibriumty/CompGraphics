from graphics import *
import numpy as np
import math as mt
import operator
from functools import reduce

choice = 0
screen_X = 800
screen_Y = 800
st = 200
Pyramid = np.array([[0, 0, 0, 1],
                     [st, 0, 0, 1],
                     [st / 2, 0, st, 1],
                     [st / 2, -st, st, 1], ])


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


# Аксонометрія
def dimetrii(Figure, TetaG1, TetaG2):
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


# АЛГОРИТМ БРАЗЕНХЕЙМА ТА ВИКЛИК ПОЛІНОМА ЛАГРАЖА
def colorize_lines(x1, y1, x2, y2):
    mass_x = []
    mass_y = []
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
        mass_x.append(x)
        mass_y.append(y)
        obj.setFill("red")
        obj.draw(win)
    if choice == 1:

        for i in range(len(mass_x)):
            mass_x[i] = mass_x[i] + (i * 0.0000000001)
        for i in range(len(mass_x)):
            obj.setFill("black")
            y = lagrange_interpolation(mass_x[i], mass_x, mass_y)
            obj = Point(mass_x[i], y)
            obj.draw(win)


# Полином Лагранжа
def lagrange_interpolation(x, x_values, y_values):
    def _basis(j):
        p = [(x - x_values[m]) / (x_values[j] - x_values[m]) for m in range(k) if m != j]
        return reduce(operator.mul, p)

    assert len(x_values) != 0 and (
                len(x_values) == len(y_values))
    k = len(x_values)
    return sum(_basis(j) * y_values[j] for j in range(k))


def Rastr(Prxy):
    Ax = Prxy[0, 0]
    Ay = Prxy[0, 1]
    Bx = Prxy[1, 0]
    By = Prxy[1, 1]
    Ix = Prxy[2, 0]
    Iy = Prxy[2, 1]
    Mx = Prxy[3, 0]
    My = Prxy[3, 1]
    colorize_lines(Mx, My, Bx, By)
    colorize_lines(Ax, Ay, Mx, My)
    colorize_lines(Ix, Iy, Mx, My)
    colorize_lines(Bx, By, Ix, Iy)
    colorize_lines(Ax, Ay, Bx, By)
    colorize_lines(Ix, Iy, Ax, Ay)



while True:
    win = GraphWin("Аксонометричне зображення трикутної піраміди", screen_X, screen_Y)
    win.setBackground('white')
    xw = 600
    yw = 600
    st = 200
    TetaG1 = 90
    TetaG2 = -180
    l = (xw) - st
    m = (yw) - st
    n = m
    Pyramid1 = XYZ(Pyramid, l, m, n)
    Pyramid2 = dimetrii(Pyramid1, TetaG1, TetaG2)
    Prxy3 = XY(Pyramid2)
    Rastr(Prxy3)
    win.getMouse()
    win.close()
    choice = 1
    win = GraphWin("Аксонометрія та інтерполяція поліномом Лагранжа", screen_X, screen_Y)
    win.setBackground('white')
    xw = 600
    yw = 600
    st = 200
    TetaG1 = 90
    TetaG2 = -180
    l = (xw) - st
    m = (yw) - st
    n = m
    Pyramid1 = XYZ(Pyramid, l, m, n)
    Pyramid2 = dimetrii(Pyramid1, TetaG1, TetaG2)
    Prxy3 = XY(Pyramid2)
    Rastr(Prxy3)
    win.getMouse()
    win.close()
