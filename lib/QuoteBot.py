#!/usr/bin/env python
from .AbstractScript import AbstractScript
import json
import os
import random
import re


class QuoteBot(AbstractScript):
    name = "QuoteBot"
    trigger = ".quote"
    helpstring = "hi"

    """
    [b]QuoteBot[/b]
    \tQuote management. Quotes can be added, removed, or displayed.
    [b]Examples:[/b]
    \t.quote add [i]<quote>[/i]
    \t.quote add [i]I love goats.[/i]
    \t.quote remove [i]<quote ID>[/i]
    \t.quote remove [i]2[/i]
    \t.quote count
    \t.quote [i]<quote ID>[/i]
    \t.quote [i]3[/i]
    \t.quote
    """

    filename = "quotes.json"

    def __init__(self):
        # Create quote file, if it doesn't exist.
        if not os.path.isfile(self.filename):
            with open(self.filename, 'w') as f:
                json.dump({}, f)


    def react(self, event):
        """ Act. False if there is no message to send,
        string message otherwise. """
        if "msg" in event:
            m = event["msg"]

            if m[:6].lstrip().lower() == self.trigger:
                with open(self.filename, "r+") as f:
                    quotes = json.load(f)
                    f.seek(0)
                    parts = m.split()
                    highest_key = 0
                    quote_IDs = list(quotes.keys())
                    if quote_IDs:
                        intKeys = list(filter(self.isInteger, quote_IDs))
                        highest_key = max([int(x) for x in intKeys])

                    if m.strip().lower() == self.trigger:
                        # example command: .quote
                        # return random quote
                        if not quotes:
                            return "[b]QuoteBot[/b]: No quotes found."
                        else:
                            return random.choice(list(quotes.values()))

                    elif parts[1] == "add" and len(parts) > 2:
                        # example command: .quote add test
                        # add quote to json file
                        add_match = re.compile(self.trigger + r"\s+add\s+(.*)",
                                               flags=re.IGNORECASE)
                        new = add_match.match(m.strip()).groups(1)[0]
                        quotes[highest_key + 1] = new
                        json.dump(quotes, f, indent=4)
                        f.seek(0)
                        return False

                    elif parts[1] == "remove" and len(parts) > 2:
                        # example command: .quote remove 3
                        # remove quote from json file
                        print("found remove")
                        rem_match = re.compile(self.trigger +
                                               r"\s+remove\s+(.*)",
                                               flags=re.IGNORECASE)
                        rem_id = rem_match.match(m.strip()).groups(1)[0]
                        print("rem_id: " + rem_id)
                        if str(rem_id) in quote_IDs:
                            print("rem id in quote ids")
                            q = quotes.pop(rem_id)
                            json.dump(quotes, f, indent=4)
                            f.truncate()
                            f.seek(0)
                            return ("[b]QuoteBot[/b]: Removed quote [" +
                                    rem_id + "]: " + q)

                    elif parts[1] == "count":
                        return ("[b]QuoteBot[/b]: " +
                                str(len(quote_IDs)) + " quotes found.")

                    elif len(parts) == 2:
                        # example command: .quote 5
                        # display quote with ID=5
                        # ID of quote is in parts[1]
                        if parts[1] in quote_IDs:
                            return (quotes[parts[1]])

        return False

    @staticmethod
    def isInteger(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
