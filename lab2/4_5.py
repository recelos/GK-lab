#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

import random

# generating random color
c1 = random.randint(0, 255)
c2 = random.randint(0, 255)
c3 = random.randint(0, 255)


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    print_rectangle(-50.0, -50.0, 100.0, 100.0)

    glFlush()


def print_rectangle(x, y, a, b, d=0):
    random.seed()

    glColor3b(c1, c2, c3)
    glBegin(GL_TRIANGLES)
    glVertex2f(x + a, y + b)
    glVertex2f(x, y)
    glVertex2f(x + a, y)
    glEnd()

    glColor3b(c1, c2, c3)
    glBegin(GL_TRIANGLES)
    glVertex2f(x + a, y + b)
    glVertex2f(x, y + b)
    glVertex2f(x, y)
    glEnd()


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
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
