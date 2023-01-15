#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


viewer = [0.0, 0.0, 10.0]

theta = 0.0
pix2angle = 1.0

left_mouse_button_pressed = 0
mouse_x_pos_old = 0
delta_x = 0

mat_ambient = [1.0, 1.0, 1.0, 1.0]
mat_diffuse = [1.0, 1.0, 1.0, 1.0]
mat_specular = [1.0, 1.0, 1.0, 1.0]
mat_shininess = 20.0

light_ambient = [0.1, 0.1, 0.1, 0.1]
light_diffuse = [0.1, 0.1, 0.1, 0.1]
light_specular = [0.1, 0.1, 0.1, 0.1]
light_position = [0.0, 10.0, 0.0, 1.0]

att_constant = 1.0
att_linear = 0.05
att_quadratic = 0.001

changed_component = 'a'

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, att_quadratic)

    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)


def shutdown():
    pass


def render(time):
    global theta

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(viewer[0], viewer[1], viewer[2],
              0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if left_mouse_button_pressed:
        theta += delta_x * pix2angle

    glRotatef(theta, 0.0, 1.0, 0.0)

    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_FILL)
    gluSphere(quadric, 3.0, 10, 10)
    gluDeleteQuadric(quadric)

    glFlush()


def update_viewport(window, width, height):
    global pix2angle
    pix2angle = 360.0 / width

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(70, 1.0, 0.1, 300.0)

    if width <= height:
        glViewport(0, int((height - width) / 2), width, width)
    else:
        glViewport(int((width - height) / 2), 0, height, height)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard_key_callback(window, key, scancode, action, mods):
    global changed_component

    if key == GLFW_KEY_A and action == GLFW_PRESS:
      changed_component = 'a'
      print("changed_component = 'a'")
    if key == GLFW_KEY_D and action == GLFW_PRESS:
      changed_component = 'd'
      print("changed_component = " + changed_component)
      
    if key == GLFW_KEY_S and action == GLFW_PRESS:
      changed_component = 's'
      print("changed_component = " + changed_component)

    if key == GLFW_KEY_UP and action == GLFW_PRESS:
      increase()
    if key == GLFW_KEY_DOWN and action == GLFW_PRESS:
      decrease()
    
    if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
        glfwSetWindowShouldClose(window, GLFW_TRUE)


def increase():
    global light_ambient
    global light_specular
    global light_diffuse

    if changed_component == 'a':
        print("light_ambient: ")
        if all(x + 0.1 < 1.0 for x in light_ambient):
            light_ambient = [x + 0.1 for x in light_ambient]
        glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
        print(light_ambient)

    if changed_component == 'd':
        print("light_diffuse: ")
        if all(x + 0.1 < 1.0 for x in light_diffuse):
            light_diffuse = [x + 0.1 for x in light_diffuse]
        print(light_diffuse)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)

    if changed_component == 's':
        print("d: ")
        if all(x + 0.1 < 1.0 for x in light_specular):
            light_specular = [x + 0.1 for x in light_specular]
        print(light_specular)
        glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)



def decrease():
    global light_ambient
    global light_specular
    global light_diffuse

    if changed_component == 'a':
        print("light_ambient: ")
        if all(x - 0.1 > 0.0 for x in light_ambient):
            light_ambient = [x - 0.1 for x in light_ambient]
        print(light_ambient)
        glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)

    if changed_component == 'd':
        print("light_diffuse: ")
        if all(x - 0.1 > 0.0 for x in light_diffuse):
            light_diffuse = [x - 0.1 for x in light_diffuse]
        print(light_diffuse)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)


    if changed_component == 's':
        print("light_specular: ")
        if all(x - 0.1 > 0.0 for x in light_specular):
            light_specular = [x - 0.1 for x in light_specular]
        print(light_specular)
        glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)


def mouse_motion_callback(window, x_pos, y_pos):
    global delta_x
    global mouse_x_pos_old

    delta_x = x_pos - mouse_x_pos_old
    mouse_x_pos_old = x_pos


def mouse_button_callback(window, button, action, mods):
    global left_mouse_button_pressed

    if button == GLFW_MOUSE_BUTTON_LEFT and action == GLFW_PRESS:
        left_mouse_button_pressed = 1
    else:
        left_mouse_button_pressed = 0


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSetKeyCallback(window, keyboard_key_callback)
    glfwSetCursorPosCallback(window, mouse_motion_callback)
    glfwSetMouseButtonCallback(window, mouse_button_callback)
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
