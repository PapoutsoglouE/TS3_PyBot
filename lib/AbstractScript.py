#! /usr/bin/env python
from abc import ABCMeta, abstractmethod, abstractproperty

class AbstractScript(object):
	__metaclass__ = ABCMeta
	name = "AbstractScript"
	trigger = 0
	key = "API key"
	helpstring = """
	AbstractScript is the base of all bot actions. It can be extended to customize bot behaviour. 
	"""
	
	
	def __init__(self, param=None):
		""" Initialise parameters for this script. """
		self.param = param
		
		
	@abstractmethod
	def react(self, event):
		""" Act. False if there is no message to send, 
		string message otherwise. """
		return False
		
		