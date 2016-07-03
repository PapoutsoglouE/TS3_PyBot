#https://github.com/benediktschmitt/py-ts3

import ts3

with ts3.query.TS3Connection("127.0.0.1", 10011) as ts3conn:
	ts3conn.login(
		client_login_name="ServerQuery",
		client_login_password="eNbJi1an"
	)
	ts3conn.use(sid=1)
	
	# Register for events
	ts3conn.servernotifyregister(event="server")
	
	while True:
		event = ts3conn.wait_for_event()
		print(event)
		# Greet new clients.
		if event[0]["reasonid"] == "0":
			print("client connected")
			ts3conn.clientpoke(clid=event[0]["clid"], msg="Hello :)")
