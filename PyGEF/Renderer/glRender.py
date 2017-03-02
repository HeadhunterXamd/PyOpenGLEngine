__author__ = 'nielsvanschooten@gmail.com'
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


animationAngle = 1.0
frameRate = 25


def doAnimationStep():
	"""Update animated parameters.

	This Function is made active by glutSetIdleFunc"""
	global animationAngle
	global frameRate
	animationAngle += 1
	while animationAngle > 360:
		animationAngle -= 360
	yield ( 1 / float(frameRate) )
	glutPostRedisplay()


def initgl(Width, Height):
	# A general OpenGL initialization function.  Sets all of the initial parameters.
	glClearColor(0.0, 0.0, 0.0, 0.0)  # This Will Clear The Background Color To Black
	glClearDepth(1.0)  # Enables Clearing Of The Depth Buffer
	glDepthFunc(GL_LESS)  # The Type Of Depth Test To Do
	glEnable(GL_DEPTH_TEST)  # Enables Depth Testing
	glShadeModel(GL_SMOOTH)  # Enables Smooth Color Shading

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()  # Reset The Projection Matrix
	gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)  # Calculate The Aspect Ratio Of The Window

	glMatrixMode(GL_MODELVIEW)


def render():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # // Clear Screen And Depth Buffer
	glLoadIdentity()  # // Reset The Current Modelview Matrix
	gluLookAt(0.0, 0.0, -5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
	# glScalef (1.0, 2.0, 1.0)

	# GLdouble radius
	# GLint slices
	# GLint stacks
	glutWireSphere(GLdouble(1), GLint(6), GLint(6))

	glutSwapBuffers()

