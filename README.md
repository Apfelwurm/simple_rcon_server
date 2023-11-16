# simple_rcon_server
This is the most basic example for the usage of https://github.com/991jo/rcon-server .
it essentially opens an rcon server with the password `changeme` on `0.0.0.0:27015` and answers every command with the exact content of the command.

# usage

* clone the repository
* make sure `python3`, `python3-pip` and `python3-venv` is installed
* cd into the repository
* run `python3 -m venv .venv`
* run `source .venv/bin/activate`
* run `pip install -r requirements.txt`
* run `python simple_rcon_server.py`