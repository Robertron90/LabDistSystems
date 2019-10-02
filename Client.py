import socket, os, sys


FILE = None
HOST = '127.0.0.1'
PORT = 8800

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    with open(FILE, 'rb') as f:
      data = f.read(1024)
      while data:
        s.send(data)
        data = f.read(1024)