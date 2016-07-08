#! /usr/bin/env python
from .AbstractScript import AbstractScript
import ts3
import random
import re


class MateBot(AbstractScript):
    name = "MateBot"
    helpstring = """
    [b]MateBot[/b]
    \tReplies to "mate".
    [b]Examples:[/b]
    \tmate
    """

    def __init__(self):
        self.matepat = re.compile("m+a+te")

    
    def react(self, event, conn):
        """ Return the answer to "mate". """
        if "msg" in event:
            m = event["msg"].strip()

            if event["invokername"] != "Gote" and self.matepat.match(m):
                add_m = random.randrange(5)
                add_a = random.randrange(1, 5)
                ind_a = m.find("a")
                ind_t = m.find("t")
                
                result = m[:ind_a] + "m" * add_m + m[ind_a:ind_t] + "a" * add_a + "te"
                conn.sendtextmessage(targetmode=2, target=1,
                                     msg=result)
                return True
        return False
