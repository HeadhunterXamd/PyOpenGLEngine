__author__ = 'nielsvanschooten'
from opengl.BaseObject.Base import Base





class Mesh(Base):
	"""
		base mesh class, combined with material usable as
	"""

	def __init__(self):
		super().__init__()
		self.facemembers = []
		self.material = None

	def getMembers(self):
		return self.facemembers

	def setFaces(self, face):
		""" set the faces of the mesh object """
		self.facemembers.append(face)