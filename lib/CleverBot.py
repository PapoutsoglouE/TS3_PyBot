#!/usr/bin/env python
from .AbstractScript import AbstractScript
from cleverbot import Cleverbot
import re


class CleverBot(AbstractScript):
    name = "CleverBot"
    trigger = "gote"
    helpstring = """
    [b]CleverBot[/b]
    \tChat with Cleverbot.
    [b]Examples:[/b]
    \tgote [i]<message>[/i]
    \tgote [i]good morning[/i]
    \t[i]good morning[/i] gote
    """


    def __init__(self, param=None):
        """ Initialise Cleverbot connection. """
        self.cb = Cleverbot()


    def react(self, event):
        """ Act. False if there is no message to send,
        string message otherwise. """
        if "msg" in event:
            m = event["msg"]
            # don't forget to check for trigger http://pastebin.com/zD2mAHH6
            if self.trigger.lower() in m.lower():
                rem_trigger = re.compile(r"\b(" + self.trigger + r")\b",
                                         flags=re.IGNORECASE)
                answer = self.cb.ask(rem_trigger.sub("", m))
                return answer
        return False
