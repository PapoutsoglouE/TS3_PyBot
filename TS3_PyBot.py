#!/usr/bin/env python
#!python

import ts3
import json
import importlib


class Bot:

    def __init__(self):
        """ Initialise connection to TS server. """
        with open("settings.json") as f:
            self.settings = json.load(f)
        self._import_scripts()
        self._connect_to_server()
        self.tsconn.clientupdate(client_nickname=self.settings["name"])


    def _connect_to_server(self):
        """ Establish connection to TS3 server. """
        self.tsconn = ts3.query.TS3Connection(self.settings["host"],
                                              self.settings["port"])
        self.tsconn.login(
            client_login_name=self.settings["username"],
            client_login_password=self.settings["password"]
        )
        self.tsconn.use(sid=self.settings["serverID"])

        # Register for events
        self.tsconn.servernotifyregister(event="server")
        self.tsconn.servernotifyregister(id_=1, event="textchannel")
        print("Connected to server at " +
              self.settings["host"] + ":" + self.settings["port"])


    def _import_scripts(self):
        """ Import and instantiate each script. """
        self.scripts = list()
        print("Loading scripts...")
        for s in self.settings["scripts"]:
            try:
                r_module = importlib.import_module("lib." + s)
                r_class = getattr(r_module, s)
                self.scripts.append(r_class())
                print("\t" + getattr(r_class, "name"))
            except (ImportError, ValueError, AttributeError):
                print("Failed to get help string for " + s)


    def _react_to_event(self, event):
        """ Go through the scripts and check if any have a reaction for the
            given message event. Priority can be defined in the settings file:
            scripts higher on the list have higher priority. """
        for s in self.scripts:
            reaction = s.react(event)
            if reaction:
                self.tsconn.sendtextmessage(targetmode=2,
                                            target=1, msg=reaction)
                return


    def runBot(self):
        """ Main bot loop. Check an event and respond to it. """
        while True:
            # connection to server closes automatically after 10 minutes,
            # need to keep it alive
            try:
                self.tsconn.send_keepalive()
                event = self.tsconn.wait_for_event(timeout=540)
                # print(event[0])
                self._react_to_event(event[0])

            except ts3.query.TS3TimeoutError:
                pass


if __name__ == "__main__":
    B = Bot()
    B.runBot()
