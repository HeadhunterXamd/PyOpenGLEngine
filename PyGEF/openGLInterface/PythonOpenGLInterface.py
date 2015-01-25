__author__ = 'nielsvanschooten'
import OpenGL
OpenGL.FULL_LOGGING = True
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PyGEF.Renderer.glRender import *
import sys
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'
# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)
def keyPressed(*args):
	# If escape is pressed, kill everything.
	if args[0] == ESCAPE:
		sys.exit()

class OGLInterface():
	"""
		interface for the PyGEF renderer, this is interchangeable for your own renderer.
		The renderer interface here just initializes the PyGEF interface.
		You can overwrite this interface and implement your own interface for your own renderer.
	"""

	def __init__(self):
		self.window = 0
		self.started = False
		self.renderer = None
		self.initengine()




	def initengine(self):
		"""
			initialize the renderer and starts the mainloop
		"""

		if glutInit(sys.argv):
			glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

			# get a 640 x 480 window
			glutInitWindowSize(640, 480)

			# the window starts at the upper left corner of the screen
			glutInitWindowPosition(0, 0)
			self.window = glutCreateWindow("test")
			glutDisplayFunc(render)
			glutIdleFunc(doAnimationStep)
			glutKeyboardFunc(keyPressed)
			initgl(640, 480)
			glutMainLoop()






o = OGLInterface()