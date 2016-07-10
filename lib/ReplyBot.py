#! /usr/bin/env python
from .AbstractScript import AbstractScript
import ts3
import random


class ReplyBot(AbstractScript):
    name = "ReplyBot"
    helpstring = """
    [b]ReplyBot[/b]
    \tBot replies when keywords are mentioned. 
    \tSome replies are probability-based.
    [b]Examples:[/b]
    \tpls
    \tffs
    \tD:
    \t:3
    \tcontract
    """

    # p = -1 means random choice from list
    replies = {
        "pls": {"reply": [r"¯\_(ツ)_/¯"], "p": 1},
        "ffs": {"reply": [r"(╯°□°)╯︵ ┻━┻"], "p": 0.9},
        "D:": {"reply": [r"C:"], "p": 1},
        "hi5": {"reply": [r"(。^_・)ノ"], "p": 1},
        "contract": {"reply": [r"／人◕ ‿‿ ◕人＼"], "p": 0.9},
        "<3": {"reply": [r"</3", r"<3"], "p": -0.8},
        ":3": {"reply": [r":|", r">:3"], "p": -0.7}
        #"": {"reply": [r""], "p": },
    }


    def react(self, event, conn, settings):
        """ Return the answer to the keyword. Maybe. """
        if "msg" in event:
            if event["invokername"] == settings["name"]: 
                return False

            m = event["msg"].lower()
            for k in list(self.replies.keys()):
                if k in m:
                    r = self.replies[k]["reply"]
                    p = self.replies[k]["p"]
                    if -1 < p < 0 and len(r) == 2:
                        # biased choice between two
                        if random.random() < p * (-1):
                            conn.sendtextmessage(targetmode=2, target=1,
                                         msg=r[0])
                        else: 
                            conn.sendtextmessage(targetmode=2, target=1,
                                         msg=r[1])
                        return True

                    elif p < 0:
                        # random choice, unbiased
                        conn.sendtextmessage(targetmode=2, target=1,
                                     msg=random.choice(r))
                        return True

                    else:
                        if random.random() < p:
                            conn.sendtextmessage(targetmode=2, target=1,
                                     msg=r[0])
                            return True

        return False
