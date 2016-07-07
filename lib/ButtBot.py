#! /usr/bin/env python
from .AbstractScript import AbstractScript
import ts3
import random


class ButtBot(AbstractScript):
    name = "ButtBot"
    p = 0.05  # probability of word replacement
    helpstring = """
    [b]ButtBot[/b]
    \tChance of replacing a random word in a message with [i]butt[/i].
    \tCurrently [i]p = """ + str(p) + """[/i].
    """


    def react(self, event, conn):
        """ Act. True if there is a message to send,
        False otherwise, followed by the actual string. """
        if "msg" in event:
            m = event["msg"]
            x = random.random()
            if x < self.p:
                word = m.split()
                i = random.randrange(len(word))
                word[i] = "butt"
                result = " ".join(word)
                conn.sendtextmessage(targetmode=2, target=1,
                                     msg=result)
                return True

        return False
