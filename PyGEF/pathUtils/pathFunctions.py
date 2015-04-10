__author__ = 'nielsvanschooten'
import os




def getCurrentDirectory(file=__file__):
	return  os.path.dirname(os.path.abspath(file))
