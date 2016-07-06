# TS3_PyBot
A simple bot for TeamSpeak 3 written in Python.

## Use
Just run [`TS3_PyBot.py`]().

```sh
python TS3_PyBot.py
```

The bot should now be running. Error messages will be displayed in the same console window.

## Dependencies
The following libraries need to be installed:

* [Cleverbot](https://github.com/folz/cleverbot.py)
* [PyTS3](https://github.com/benediktschmitt/py-ts3/tree/master/ts3)

The bot requires Python 3.3+.

## Settings
The [`settings.json`](https://github.com/PapoutsoglouE/TS3_PyBot/blob/master/settings.json) file contains the bot configuration. In addition to the server address, the bot also requires Server Query credentials. The default server query port is `10011`. The server ID will have to be edited if there are multiple virtual servers. It can be found by logging in on the server through telnet, then running the `serverlist` command, and finally looking up the desired `virtualserver_id`.

The `scripts` list defines not only which scripts will run, but also their relative priority. Scripts higher on the list take precedence over the ones following them.

## Scripts
All bot functionality is defined through scripts. They are located in the [`lib`](https://github.com/PapoutsoglouE/TS3_PyBot/tree/master/lib) folder and all inherit from the [`AbstractScript`](https://github.com/PapoutsoglouE/TS3_PyBot/blob/master/lib/AbstractScript.py) class. Currently, the following scripts exist:

When the [`HelpBot`](https://github.com/PapoutsoglouE/TS3_PyBot/blob/master/lib/HelpBot.py) script is active, more information about the running scripts can be displayed in the chat:

[`.help`](https://github.com/PapoutsoglouE/TS3_PyBot/blob/master/lib/HelpBot.py#L13): Displays a list of the all active scripts.

[`.help <i>script_name</i>`](https://github.com/PapoutsoglouE/TS3_PyBot/blob/master/lib/HelpBot.py#L13): Displays more information about one script. (e.g. `.help helpbot`)

The trigger word for each script is defined in its respective file, through the [`trigger`](https://github.com/PapoutsoglouE/TS3_PyBot/blob/master/lib/HelpBot.py#L9) variable.


| Script | Trigger | Description |
|--------|----------|-------------|
| [`ButtBot`](https://github.com/PapoutsoglouE/TS3_PyBot/blob/master/lib/ButtBot.py) | - | Replaces a random word in a posted text message with <i>butt</i>. |
| [`CleverBot`](https://github.com/PapoutsoglouE/TS3_PyBot/blob/master/lib/CleverBot.py) | `gote` | Chat with [Cleverbot](). |
| [`EightBall`](https://github.com/PapoutsoglouE/TS3_PyBot/blob/master/lib/EightBall.py) | `.8ball` | The 8ball will answer one question. | 
| [`HelpBot`](https://github.com/PapoutsoglouE/TS3_PyBot/blob/master/lib/HelpBot.py) | `.help` | Get help about running scripts. |
| [`QuoteBot`](https://github.com/PapoutsoglouE/TS3_PyBot/blob/master/lib/QuoteBot.py) | `.quote` | Add, remove, access your quotes. | 

