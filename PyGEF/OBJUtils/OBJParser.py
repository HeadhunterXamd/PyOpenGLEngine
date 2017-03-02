__author__ = 'nielsvanschooten'
from PyGEF.BaseObject.Vertex import Vertex
from PyGEF.BaseObject.Face import Face
from PyGEF.BaseObject.Mesh import Mesh
from pathUtils import pathFunctions


class OBJParser():
    """
        homemade .obj parser for my own purpose, needed my own format to wrap my head around
    """

    def __init__(self, file):
        self.name = None
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
            if self.parseLine(dataFile.readline()) is False:
                print("data in line {a} is faulty: \n------\n{b}\n------".format(
                    a=line, b=dataFile.readline))

        dataFile.close()

    def parseVertexData(self, line: str):
        """ parse the data with the v as prefix """
        coordinates = line.split(" ")
        coordinates.pop(0)
        data = []
        for co in coordinates:
            data.append(eval(co))

        self.vertex[len(self.vertex) + 1] = Vertex(data[0], data[1], data[2])
        return True

    def parseFaceData(self, line: str):
        """ parse the face data for which vertexes  """
        faceData = line.split(" ")
        faceData.pop(0)
        newFace = Face()

        for facemember in faceData:
            newFace.addVertex(self.vertex[eval(facemember)])

        self.faces.append(newFace)
        return True

    def getMeshObject(self):
        """ parse the faces and insert them to a mesh object """
        newMesh = Mesh()
        for face in self.getfaces():
            newMesh.setFaces(face)

        return newMesh

    def parseLine(self, line: str) -> bool:
        """
            Parse the line of the file,
            zero index is always the indicator for what it is.
        """
        splitLine = line.split(" ", 1)
        if "v" in splitLine[0]:
            return self.parseVertexData(line)
        # f indicates in the .obj that the line is data for a face
        elif "f" in splitLine[0]:
            return self.parseFaceData(line)
        # o indicates the object name.
        elif "0" in splitLine[0]:
            self.name = splitLine[1]
            if self.name is not None:
                return True
            else:
                return False
        elif "usemtl" in splitLine[0]:
            if splitLine[1] is "None":
                return True
            else:
                self.ParseMTL(splitLine[1])
        else:
            return False

    def ParseMTL(self, filename: str) -> bool:
        return True

    def fileLength(self, file):
        length = sum(1 for line in file)
        return length
