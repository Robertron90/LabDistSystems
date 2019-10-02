import socket, os, sys

FILE = sys.argv[1]
HOST = sys.argv[2]
PORT = sys.argv[3]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(FILE.decode())

    with open(FILE, 'rb') as f:
      data = f.read(1024)
      sended = 0
      while data:
        s.send(data)
        sended += 1024
        print(sended/os.path.getsize(FILE))
        data = f.read(1024)