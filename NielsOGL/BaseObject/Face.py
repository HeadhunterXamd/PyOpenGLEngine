__author__ = 'nielsvanschooten'
from opengl.BaseObject.Base import Base

class Face(Base):
	"""
		this is an interface for generating an polygon in NielsOGL
	"""

	def __init__(self):
		super().__init__()
		self.vertexMembers = []

	def __str__(self):
		return "A face to remember"

	def getMembers(self):
		return self.vertexMembers

	def addVertex(self, vertex)->bool:
		""" add a vertex to the members list, easier to manage than a huge list of vertexes """
		if(len(self.vertexMembers) <= 3):
			self.vertexMembers.append(vertex)
			return True
		else:
			return False
