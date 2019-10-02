import socket

HOST = '0.0.0.0'
PORT = 8800


class FileThread(Thread);


def __init__(self, sock: socket.socket)
    super().__init__(daemon=True)
    self.sock = sock


def run(self);


with self.sock:
    with open("RECEIVEDFILE", 'wb') as f:
        while True:
            data = self.sock.recv(1024)
            f.write(data)
            if not data:
                break
return

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    while True:
        FileThread(s.accept[0]).start()