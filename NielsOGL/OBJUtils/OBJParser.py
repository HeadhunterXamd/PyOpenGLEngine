__author__ = 'nielsvanschooten'
from opengl.BaseObject.Vertex import Vertex
from opengl.BaseObject.Face import Face
from opengl.BaseObject.Mesh import Mesh
from opengl.pathUtils import pathFunctions


class OBJParser():
	"""
		homemade .obj parser for my own purpose, needed my own format to wrap my head around
	"""

	def __init__(self, file):
		self.vertex = {}
		self.faces = []
		self.parseFileData(file)

	def getfaces(self):
		return self.faces

	def getVertex(self):
		return self.vertex

	def parseFileData(self, file):
		""" parse the vertex data and add them to a dictionary to later on combine it to an object """
		dataFile = open(file, "r")
		length = self.fileLength(dataFile)
		dataFile.seek(0, 0)

		for line in range(length):
			self.parseLine(dataFile.readline())

		dataFile.close()

	def parseVertexData(self, line:str):
		""" parse the data with the v as prefix """
		coordinates = line.split(" ")
		coordinates.pop(0)
		data = []
		for co in coordinates:
			data.append(eval(co))

		self.vertex[len(self.vertex)+1] = Vertex(data[0], data[1], data[2])


	def parseFaceData(self, line:str):
		""" parse the face data for which vertexes  """
		fa = line.split(" ")
		fa.pop(0)
		newFace = Face()

		for facemember in fa:
			newFace.addVertex(self.vertex[eval(facemember)])

		self.faces.append(newFace)

	def getMeshObject(self):
		""" parse the faces and insert them to a mesh object """
		newMesh = Mesh()
		for face in self.getfaces():
			newMesh.setFaces(face)

		return newMesh


	def parseLine(self, line:str):
		""" check what kind of line it is """
		if "v" in line[0]:
			return self.parseVertexData(line)
		elif "f" in line[0]:
			return self.parseFaceData(line)
		else:
			return line


	def fileLength(self, file):
		l = sum(1 for line in file)
		return l