#! /usr/bin/env python
from .AbstractScript import AbstractScript
import json
import importlib


class HelpBot(AbstractScript):
	name = "HelpBot"
	trigger = ".help"
	helpstring = """
	[b]HelpBot[/b]
	\tShows information about running scripts.
	[b]Examples:[/b]
	\t.help [i]<script>[/i]
	\t.help helpbot
	\t.help
	"""
	
	
	def __init__(self):
		self.hstrings = dict()
		self.scripts = list()
		with open("settings.json") as f:
			data = json.load(f)
			self.scripts = data["scripts"]
			for s in self.scripts:
				try:
					r_module = importlib.import_module("lib." + s)  
					r_class = getattr(r_module, s)
					self.hstrings[r_class.name.lower()] = r_class.helpstring
				except (ImportError, ValueError, AttributeError):
					print("Failed to get help string for " + s)
	
	
	def react(self, event):
		""" Act. True if there is a message to send, 
		False otherwise, followed by the actual string. """
		if "msg" in event:
			m = event["msg"].strip().lower()
			m = ' '.join(m.split())
			if m[0:6] == self.trigger + " ":
				botname = m[6:]
				if botname in self.hstrings:
					return self.hstrings[botname]
			elif m == self.trigger:
				running_scripts = self.scripts
				return """
				[b]Running scripts:[/b] """ + ", ".join(self.scripts)

		return False
			
			
