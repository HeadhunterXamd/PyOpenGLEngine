__author__ = 'nielsvanschooten'
from Base import Base





class Mesh(Base):
	"""
		base mesh class, combined with material usable as object.
		this has a separate position and the vertexPosition is based on this.
	"""

	def __init__(self):
		super().__init__(0,0,0)
		self.facemembers = []
		self.material = None

	def getMembers(self):
		return self.facemembers

	def setFaces(self, face):
		""" set the faces of the mesh object """
		self.facemembers.append(face)