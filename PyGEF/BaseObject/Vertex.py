__author__ = 'nielsvanschooten'
from opengl.BaseObject.Base import Base


class Vertex(Base):

	def __init__(self, x, y, z):
	""" this is a vertex model to translate the vertex data from 3d files to PyGEF. """
		super().__init__()
		self.x = x
		self.y = y
		self.z = z


	def __str__(self):
		return str(self.x, self.y, self.z)

	def getPosition(self):
		""" returns a list of 3 numbers which represent the position of the vertex """
		return [self.x, self.y, self.z]

	def translate(self, vec):
		self.x += vec[0]
		self.y += vec[1]
		self.z += vec[2]
