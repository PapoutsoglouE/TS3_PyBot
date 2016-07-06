#! /usr/bin/env python
from .AbstractScript import AbstractScript
import random


class EightBall(AbstractScript):
	name = "EightBall"
	trigger = ".8ball"
	helpstring = """
	[b]EightBall[/b]
	\tGet an answer from an 8ball.
	[b]Examples:[/b]
	\t.8ball [i]<question>[/i]
	\t.8ball [i]Has anyone really been far even as decided to use even go want to do look more like?[/i]
	"""
	
	replies = [
		"It is certain.", 
		"It is decidedly so.", 
		"Without a doubt.", 
		"Yes, definitely.", 
		"You may rely on it.", 
		"As I see it, yes.", 
		"Most likely.", 
		"Outlook good.", 
		"Yes.", 
		"Signs point to yes.", 
		"Reply hazy, try again.", 
		"Ask again later.", 
		"Better not tell you now.", 
		"Cannot predict now.", 
		"Concentrate and ask again.", 
		"Don't count on it.", 
		"My reply is no.", 
		"My sources say no.", 
		"Outlook not so good.", 
		"Very doubtful.", 
		]

	
	def react(self, event):
		""" Act. True if there is a message to send, 
		False otherwise, followed by the actual string. """
		if "msg" in event:
			m = event["msg"]
			if m[:7].lstrip().lower() == ".8ball ":
				return random.choice(self.replies)
				
		
		
