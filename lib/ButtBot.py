#! /usr/bin/env python
from .AbstractScript import AbstractScript
import ts3
import random


class ButtBot(AbstractScript):
    name = "ButtBot"
    p = 0.05  # probability of word replacement
    trigger = ".buttbot"
    helpstring = """
    [b]ButtBot[/b]
    \tChance of replacing a random word in a message with [i]butt[/i].
    \tProbability of replacement can be viewed or changed.    
    [b]Examples:[/b]
    \t.buttbot set <[i]p[/i]>
    \t.buttbot set [i]0.01[/i]
    \t.buttbot get
    """


    def react(self, event, conn):
        """ Act. True if there is a message to send,
        False otherwise, followed by the actual string. """
        if "msg" in event:
            m = event["msg"].strip()
            word = m.split()
            x = random.random()
            
            if word[0].lower() == self.trigger:
                if word[1].lower() == "set" and len(word) == 3:
                    try:
                        new_p = float(word[2])
                        if 0.0 <= new_p <= 1.0:
                            self.p = new_p
                            self.helpstring = """
                                [b]ButtBot[/b]
                                \tChance of replacing a random word in a message with [i]butt[/i].
                                \tCurrently [i]p = """ + str(self.p) + """[/i].
                                """
                            print("success")
                            return True
                        else:
                            return False
                    except ValueError:
                        pass
                        print("fail")

                elif word[1].lower() == "get" and len(word) == 2:
                    result = "[b]Buttbot:[/b] p = " + str(self.p)
                    conn.sendtextmessage(targetmode=2, target=1, 
                                         msg=result)
                    return True

                return False

            if x < self.p:
                i = random.randrange(len(word))
                word[i] = "butt"
                result = " ".join(word)
                conn.sendtextmessage(targetmode=2, target=1, 
                                     msg=result)
                return True

        return False
