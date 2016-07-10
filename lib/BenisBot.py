#! /usr/bin/env python
from .AbstractScript import AbstractScript
import ts3
from .benisify import benisify


class BenisBot(AbstractScript):
    name = "BenisBot"
    trigger = ".benis"
    helpstring = """
    [b]BenisBot[/b]
    \tBenisify a sentence.
    [b]Examples:[/b]
    \t.benis [i]<sentence>[/i]
    \t.benis [i]Has anyone really been far even as decided to use even go want to do look more like?[/i]
    """


    def react(self, event, conn, settings):
        """ Return the benisified sentence. """
        
        if "msg" in event:
            if event["invokername"] == settings["name"]: 
                return False

            m = event["msg"].strip()
            parts = m.split()
            if parts[0].lower() == self.trigger:
                result = benisify(m[7:])
                conn.sendtextmessage(targetmode=2, target=1,
                                     msg=result)
                return True
        return False
