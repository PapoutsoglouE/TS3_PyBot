#! /usr/bin/env python
from .AbstractScript import AbstractScript
import ts3
import random


class DieBot(AbstractScript):
    name = "DieBot"
    trigger = ".roll"
    helpstring = """
    [b]DieBot[/b]
    \tRoll a die.
    \tYou can also roll more N-sided dice.
    [b]Examples:[/b]
    \t.roll
    \t.roll [i]<sides>[/i]
    \t.roll [i]12[/i]
    \t.roll [i]<sides> <dice>[/i]
    \t.roll [i]12 5[/i]
    """


    def react(self, event, conn, settings):
        """ Roll dice. """
        if "msg" in event:
            if event["invokername"] == settings["name"]: 
                return False

            m = event["msg"].strip()
            parts = m.split()
            dice = 1
            sides = 6
            rolls = list()
            
            if not (parts[0] == self.trigger and len(parts) < 4):
                return False
            else:
                if len(parts) > 1:
                    try:
                        sides = int(parts[1])
                        if sides < 1:
                            sides = 6
                    except ValueError:
                        pass
                if len(parts) == 3:
                    try:
                        dice = int(parts[2])
                        if dice < 1:
                            dice = 1
                    except ValueError:
                        pass

                for die in range(dice):
                    rolls.append(str(random.randint(1, sides)))
                    
                result = "[b]Rolled:[/b] " + ", ".join(rolls)
                conn.sendtextmessage(targetmode=2, target=1,
                                     msg=result)
                return True
        return False
