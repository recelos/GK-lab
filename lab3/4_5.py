#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

from math import *
import random

c1 = random.randint(0, 255)
c2 = random.randint(0, 255)
c3 = random.randint(0, 255)

c4 = random.randint(0, 255)
c5 = random.randint(0, 255)
c6 = random.randint(0, 255)

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

def shutdown():
    pass

def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()

def spin(angle):
    glRotatef(angle*100, 1.0, 0.0, 0.0)
    glRotatef(angle*100, 0.0, 1.0, 0.0)
    glRotatef(angle*100, 0.0, 0.0, 1.0)

def egg(N, tab, color):
    for i in range(N):
        for j in range(N):
            glBegin(GL_TRIANGLE_STRIP)
            
            glColor3b(color[i][j][0], color[i][j][1], color[i][j][2])
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
            
            glColor3b(color[i+1][j][0], color[i+1][j][1], color[i+1][j][2])
            glVertex3f(tab[i+1][j][0], tab[i+1][j][1], tab[i+1][j][2])
            
            glColor3b(color[i][j+1][0], color[i][j+1][1], color[i][j+1][2])
            glVertex3f(tab[i][j+1][0], tab[i][j+1][1], tab[i][j+1][2])
            
            glColor3b(color[i+1][j+1][0], color[i+1][j+1][1], color[i+1][j+1][2])
            glVertex3f(tab[i+1][j+1][0], tab[i+1][j+1][1], tab[i+1][j+1][2])
            glEnd()


def render(time, N, tab, color):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    axes()
    spin(time)
    egg(N, tab, color)

    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)

    N = 50

    tab = [[[0] * 3 for i in range(N+1)] for j in range(N+1)]
    color = [[[0] * 3 for i in range(N+1)] for j in range(N+1)]

    fill_matrix(N, tab, color)

    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime(), N, tab, color)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()

def fill_matrix(N, tab, color):
    for i in range(0, N+1):
        for j in range(0, N+1):
            u = i / N
            v = j / N
            tab[i][j][0] = (-90 * pow(u, 5) + 225 * pow(u, 4) - 270 * pow(u, 3) + 180 * pow(u, 2) - 45 * u) * cos(pi * v)
            tab[i][j][1] = 160 * pow(u, 4) - 320 * pow(u, 3) + 160 * pow(u, 2) - 5
            tab[i][j][2] = (-90 * pow(u, 5) + 225 * pow(u, 4) - 270 * pow(u, 3) + 180 * pow(u, 2) - 45 * u) * sin(pi * v)
            color[i][j][0] = random.randint(0, 255)
            color[i][j][1] = random.randint(0, 255)
            color[i][j][2] = random.randint(0, 255)

if __name__ == '__main__':
    main()
