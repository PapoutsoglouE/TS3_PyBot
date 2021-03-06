#! /usr/bin/env python
from .AbstractScript import AbstractScript
import ts3
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


    def react(self, event, conn, settings):
        """ Return the answer of the 8ball. """
        if "msg" in event:
            if event["invokername"] == settings["name"]: 
                return False

            m = event["msg"]
            if m[:7].lstrip().lower() == self.trigger + " ":
                result = random.choice(self.replies)
                conn.sendtextmessage(targetmode=2, target=1,
                                     msg=result)
                return True
        return False
