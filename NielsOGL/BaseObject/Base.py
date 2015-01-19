__author__ = 'nielsvanschooten'
from abc import ABCMeta, abstractmethod

class Base():

	__metaclass__ = ABCMeta

	def __init__(self, x, y, z ):
		self.x = x
		self.y = y
		self.z = z

	@abstractmethod
	def getMembers(self):
		pass

	@abstractmethod
	def getPosition(self):
		pass
