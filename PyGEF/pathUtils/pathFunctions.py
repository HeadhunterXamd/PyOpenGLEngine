__author__ = 'nielsvanschooten'
import os, inspect




def getCurrentDirectory():
	return  os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
