__author__ = 'nielsvanschooten'


class Face:
	"""
		this is an interface for generating an polygon in PyGEF, this is also the first abstract Object.
		This has no position because the position of the object is regulated by its VertexMembers.
	"""

	def __init__(self):
		self.vertexMembers = []

	def __str__(self):
		return "A face to remember"

	def getMembers(self):
		return self.vertexMembers

	def addVertex(self, vertex)->bool:
		""" add a vertex to the members list, easier to manage than a huge list of vertexes """
		if(len(self.vertexMembers) < 3):
			self.vertexMembers.append(vertex)
			return True
		else:
			return False
