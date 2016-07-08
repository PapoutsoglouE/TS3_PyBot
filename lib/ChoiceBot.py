#! /usr/bin/env python
from .AbstractScript import AbstractScript
import ts3
import random


class ChoiceBot(AbstractScript):
    name = "ChoiceBot"
    trigger = ".choose"
    helpstring = """
    [b]ChoiceBot[/b]
    \tBot makes a choice.
    [b]Examples:[/b]
    \t.choose [i]<option 1>, <option 2>, ..., <option N>[/i]
    \t.choose [i]Saber, Sayaka, Mikoto, Pen Pen[/i]
    """


    def react(self, event, conn):
        """ Make a choice. """
        if "msg" in event:
            m = event["msg"].strip()
            
            if m[:8].lstrip().lower() == self.trigger + " ":
                optstring = m[8:].split(",")
                result = "[b]ChoiceBot:[/b]" + random.choice(optstring)
                conn.sendtextmessage(targetmode=2, target=1,
                                     msg=result.strip())
                return True
        return False
