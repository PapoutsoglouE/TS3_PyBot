#! /usr/bin/env python
#! python
#https://github.com/benediktschmitt/py-ts3

import ts3
import json
import importlib
from lib.AbstractScript import AbstractScript


class Bot:
	
	def __init__(self):
		""" Initialise connection to TS server. """
		with open("settings.json") as f:
			self.settings = json.load(f)
		self._import_scripts()
		self.tsconn = ts3.query.TS3Connection(self.settings["host"], self.settings["port"])
		self.tsconn.login(
			client_login_name = self.settings["username"],
			client_login_password = self.settings["password"]
		)
		self.tsconn.use(sid=self.settings["serverID"])
		self.tsconn.clientupdate(client_nickname=self.settings["name"])
		
		
	def _import_scripts(self):
		""" Import and instantiate each script. """
		self.scripts = list()
		for s in self.settings["scripts"]:
			try:
				r_module = importlib.import_module("lib." + s)  
				r_class = getattr(r_module, s)
				self.scripts.append(r_class())
			except (ImportError, ValueError, AttributeError):
				print("Failed to get help string for " + s)
		print(self.scripts)
		
		
	def _react_to_message(self, event):
		""" Go through the scripts and check if any have a reaction for the given
			message event. Priority can be defined in the settings file: scripts
			higher on the list have higher priority. """
		if AbstractScript.isMessage(event):
			for s in self.scripts:
				reaction = s.react(event)
				if reaction:
					self.tsconn.sendtextmessage(targetmode=2, target=1, msg=reaction)
					return
		
		
	def runBot(self):
		""" Main bot loop. Check an event and respond to it. """
		# Register for events
		self.tsconn.servernotifyregister(event="server")
		self.tsconn.servernotifyregister(id_=1, event="textchannel")
		
		while True:
			event = self.tsconn.wait_for_event()
			print(event[0])
			self._react_to_message(event[0])
		
		
	
	
		
B = Bot()
B.runBot()












