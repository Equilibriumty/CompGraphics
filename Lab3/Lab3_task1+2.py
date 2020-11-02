import graphics  as gp
import time
import numpy as np
import math as mt
import random
color1 = ""
colors_outline=["red","blue","yellow"]
xwstar=1000
ywstar=1000
st=300
Prlpd = np.array([[25, 25, 25, 1],
                 [25+st, 25, 25, 1],
                 [25, 25+st, 25+st/2, 1],
                 [25+0, 25+st/2, 25+st, 1]])


def PrlpdWiz(Prxy, root, color1, color2, color3, color4):
    Prxy=list(Prxy)
    Ax = Prxy[0][0]
    Ay = Prxy[0][1]
    Bx = Prxy[1][0]
    By = Prxy[1][1]
    Ix = Prxy[2][0]
    Iy = Prxy[2][1]
    Mx = Prxy[3][0]
    My = Prxy[3][1]
    obj = gp.Polygon(gp.Point(Ax, Ay), gp.Point(Bx, By), gp.Point(Ix, Iy))
    obj.setFill(color1)
    obj.setOutline(color2)
    obj.draw(root)
    obj = gp.Polygon(gp.Point(Ax, Ay), gp.Point(Mx, My), gp.Point(Ix, Iy))

    obj.setFill(color1)
    obj.setOutline(color3)
    obj.draw(root)
    obj = gp.Polygon(gp.Point(Bx, By), gp.Point(Mx, My), gp.Point(Ix, Iy))

    obj.setOutline(color4)
    obj.draw(root)

    return PrlpdWiz


def ProjectXY (Figure):
   mass=[]
   f = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])    # по строках
   for i in range(4):
       mass.append(np.array(Figure[i]).dot(f))
   return mass

# -------------------------------------------- зміщення ----------------------------------------------

def ShiftXYZ (Figure, l, m, n):
   f = np.array([[1, 0, 0, l], [0, 1, 0, m], [0, 0, 1, n], [1, 0, 0, 1]])    # по строках
   ft=f.T
   Prxy = Figure.dot(ft)
   return Prxy

# -------------------------------------------- обертання коло х----------------------------------------


def insertX (Figure, TetaG):
    TetaR=(3/14*TetaG)/180
    f = np.array([ [1, 0, 0, 0], [0, mt.cos(TetaR), mt.sin(TetaR), 0], [0, -mt.sin(TetaR),  mt.cos(TetaR), 0], [0, 0, 0, 1] ])
    ft=f.T
    Prxy = Figure.dot(ft)
    return Prxy


def dimetri (Figure, TetaG1, TetaG2):
    TetaR1=(3/14*TetaG1)/180
    TetaR2=(3/14*TetaG2)/180
    f1 = np.array([[mt.cos(TetaR1), 0 , -mt.sin(TetaR1), 0], [0, 1, 0, 0],  [mt.sin(TetaR1), 0, mt.cos(TetaR1), 1], [0, 0, 0, 0],])
    ft1 = f1.T
    Prxy1 = Figure.dot(ft1)
    f2 = np.array([ [1, 0, 0, 0], [0, mt.cos(TetaR2), mt.sin(TetaR2), 0], [0, -mt.sin(TetaR2),  mt.cos(TetaR2), 0], [0, 0, 0, 1] ])
    ft2=f2.T
    Prxy2 = Prxy1.dot(ft2)
    return Prxy2

win3 = gp.GraphWin("Перше завдання", xwstar, ywstar)
win3.setBackground('white')
while True:
    xw = 200
    yw = 200
    st = 50
    TetaG1 = 0
    TetaG2 = -90
    l = (xw) - st
    m = (yw) - st
    n = m
    Prxy3 = Prlpd

    PrlpdWiz(Prxy3, win3, color1, colors_outline[0], colors_outline[1], colors_outline[2])
    time.sleep(1)
    PrlpdWiz(Prxy3, win3, "white", "white", "white", "white")
    time.sleep(1)
    xw = 200;yw =200;st = 50;TetaG1 = 0;TetaG2 = -90
    l = (xw) - st;m = (yw) - st;n = m;
    Prlpd1 = ShiftXYZ(Prlpd, l, m, n)
    Prlpd2 = insertX(Prlpd1, TetaG1)
    Prxy3 = ProjectXY(Prlpd2)
    PrlpdWiz(Prxy3, win3, color1, colors_outline[0], colors_outline[1], colors_outline[2])
    time.sleep(1)
    PrlpdWiz(Prxy3, win3, "white", "white", "white", "white")
    time.sleep(1)
    xw = 200
    yw = 200
    st = 50
    TetaG1 = 180
    TetaG2 = -90
    l = (xw) - st
    m = (yw) - st
    n = m
    Prlpd1 = ShiftXYZ(Prlpd, l, m, n)
    Prlpd2 = insertX(Prlpd1, 45)
    Prxy3 = ProjectXY(Prlpd2)
    PrlpdWiz(Prxy3, win3, color1, colors_outline[0], colors_outline[1], colors_outline[2])
    time.sleep(1)
    PrlpdWiz(Prxy3, win3, "white", "white", "white", "white")
    time.sleep(1)

    xw=320
    yw=120
    st=50
    TetaG1=360
    TetaG2=180
    l=(xw)-st
    m=(yw)-st
    n=m
    Prlpd1=ShiftXYZ(Prlpd, l, m, n)
    Prlpd2=dimetri(Prlpd1, TetaG1, TetaG2)
    Prxy3=ProjectXY(Prlpd2)
    PrlpdWiz(Prxy3, win3, color1,  colors_outline[0],  colors_outline[1],  colors_outline[2])
    time.sleep(1)
    PrlpdWiz(Prxy3, win3, "white", "white", "white", "white")
    time.sleep(1)


