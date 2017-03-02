from PyGEF.BaseObject.Vertex import Vertex
from PyGEF.BaseObject.Face import Face
from PyGEF.BaseObject.Mesh import Mesh
# from PyGEF.pathUtils import pathFunctions
__author__ = 'nielsvanschooten'


class OBJParser:
	"""
		homemade .obj parser for my own purpose, needed my own format to wrap my head around
	"""

	def __init__(self, file):
		self.name = None
		self.MaterialLib = None
		self.vertex = {}
		self.faces = []
		self.parsefiledata(file)

	@property
	def getfaces(self):
		return self.faces

	@property
	def getvertex(self):
		return self.vertex

	def parsefiledata(self, file):
		""" parse the vertex data and add them to a dictionary to later on combine it to an object """
		data_file = open(file, "r")
		length = self.filelength(data_file)
		data_file.seek(0, 0)

		for line in range(length):
			if self.parseline(data_file.readline()) is False:
				print("data in line {a} is faulty: \n------\n{b}\n------".format(
					a=line, b=data_file.readline))

		data_file.close()

	def parsevertexdata(self, line: str):
		""" parse the data with the v as prefix """
		coordinates = line.split(" ")
		coordinates.pop(0)
		data = []
		for co in coordinates:
			data.append(eval(co))

		self.vertex[len(self.vertex) + 1] = Vertex(data[0], data[1], data[2])
		return True

	def parsefacedata(self, line: str):
		""" parse the face data for which vertexes  """
		face_data = line.split(" ")
		face_data.pop(0)
		new_face = Face()

		for facemember in face_data:
			new_face.addVertex(self.vertex[eval(facemember)])

		self.faces.append(new_face)
		return True

	def getmeshobject(self):
		""" parse the faces and insert them to a mesh object """
		new_mesh = Mesh()
		for face in self.getfaces:
			new_mesh.setFaces(face)

		return new_mesh

	def parseline(self, line: str) -> bool:
		"""
			Parse the line of the file,
			zero index is always the indicator for what it is.
		"""
		splitline = line.split(" ", 1)
		if "v" in splitline[0]:
			return self.parsevertexdata(line)
		# f indicates in the .obj that the line is data for a face
		elif "f" in splitline[0]:
			return self.parsefacedata(line)
		# o indicates the object name.
		elif "0" in splitline[0]:
			self.name = splitline[1]
			if self.name is not None:
				return True
			else:
				return False
		elif "usemtl" in splitline[0]:
			if splitline[1] is "None":
				return True
			else:
				self.parsemtl(splitline[1])
		else:
			return False

	# noinspection PyMethodMayBeStatic,PyMethodMayBeStatic,PyUnusedLocal
	def parsemtl(self, materialname: str) -> bool:
		return True

	# noinspection PyMethodMayBeStatic,PyMethodMayBeStatic
	def filelength(self, file) -> int:
		"""
		get the length of the file.
		"""
		length = sum(1 for _ in file)
		return length
