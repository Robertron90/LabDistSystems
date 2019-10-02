import socket, os, sys

FILE = sys.argv[1]
HOST = sys.argv[2]
PORT = int(sys.argv[3])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(FILE.encode())

    with open(FILE, 'rb') as f:
      data = f.read(1024)
      sended = 0
      while data:
        s.send(data)
        sended += 1024
        print(100*sended/os.path.getsize(FILE) if sended/os.path.getsize(FILE) < 1 else 100)
        data = f.read(1024)