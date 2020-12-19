
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


global xrot  # Величина оборту за віссю x
global yrot  # Величина оборту за віссю y
global ambient  # Розсіювання світла
global gcolor1  # Колір 1
global gcolor2  # Колір 2
global gcolor3  # Колір 3
global gcolor4  # Колір 4
global gcolor5  # Цвет 5
global lightpos  # Положення джерела світла



def init():
    global xrot  # Величина оборту за віссю  x
    global yrot  # Величина оборту за віссю  y
    global ambient  # Розсіювання світла
    global gcolor1  # Колір 1
    global gcolor2  # Колір 2
    global gcolor3  # Колір 3
    global gcolor4  # Колір 4
    global gcolor5  # Колір 5
    global lightpos  # Положення джерела світла
    # ----------------- характеристики фігури------------------------------
    xrot = 0.0  # Величина оборту за віссю x = 0
    yrot = 0.0  # Величина оборту за віссю = 0
    ambient = (1.0, 1.0, 1.0, 1)  # СВІТЛО: Трійка чисел - колір у форматі RGB, а остання - яскравість
    gcolor1 = (0.7, 0.2, 0.1, 0.8)  # Коллір фігур
    gcolor2 = (0.3, 0.7, 0.0, 0.8)  # Коллір фігури
    gcolor3 = (0.9, 0.8, 0.0, 0.8)  # Коллір фігури
    gcolor4 = (0.7, 0.4, 0.5, 0.8)  # Коллір фігури
    gcolor5 = (0.2, 0.4, 0.9, 0.8)  # Коллір фігури
    # ----------------- характеристики світла ------------------------------
    lightpos = (1.0, 1.0, 1.0)  # Положення джерела світла по віссям xyz
    glClearColor(0.5, 0.5, 0.5, 1.0)  # Сірий колір первинного окрасу
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)  # Межи малювання: горизонталь, вертикаль
    glRotatef(-90, 1.0, 0.0, 0.0)  # Зміщення по віссі Х на 90 грд.
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)  # Встановлення моделі освітлення
    glEnable(GL_LIGHTING)  # Включення освітлення
    glEnable(GL_LIGHT0)  # Включення одного джерела світла
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)  # Визначення положення джерела світла



def specialkeys(key, x, y):
    global xrot
    global yrot
    if key == GLUT_KEY_UP:  # До верху
        xrot -= 2.0
    if key == GLUT_KEY_DOWN:  # До низу
        xrot += 2.0
    if key == GLUT_KEY_LEFT:  # Ліворуч
        yrot -= 2.0
    if key == GLUT_KEY_RIGHT:  # Праворуч
        yrot += 2.0
    glutPostRedisplay()  # Виклик функції побудови графічної сцени


def draw():
    global xrot
    global yrot
    global lightpos
    global greencolor
    global treecolor
    global treecolor1

    glClear(GL_COLOR_BUFFER_BIT)  # Очищення графічного вікна та заливка сірим
    glPushMatrix()  # Збереження поточного положення світла
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)  # Обертання джерела світла та фігур сцени

    # ---------------------- конус, шар та піраміди----------------------------------------------
    glTranslatef(-1.5, 0.0, -1.5)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0.7, 0.4, 0.7, 0.8))
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glEnd()

    glPopMatrix()  # Повертає поточне положення джерела світла
    glutSwapBuffers()  # Відображення графічної сцени


glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # директива використання подвійної буферизації та моделі RGB
glutInitWindowSize(600, 600)  # розміри графічного вікна
glutInitWindowPosition(50, 50)  # положення графічного вікна відносно екрану монітора
glutInit(sys.argv)  # ініціалізація OpenGl
glutCreateWindow(b"Synthesis of realistic image")  # заголовок графічного вікна
init()  # Ініціалізація параметрів
glutDisplayFunc(draw)  # Малювання сцени
glutSpecialFunc(specialkeys)  # Керування сценою
glutMainLoop()  # Ініціалізація запуску
