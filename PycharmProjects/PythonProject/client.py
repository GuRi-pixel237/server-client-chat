import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8080))
s.sendall(b"Hello World!")
while True:
    print(s.recv(1024))
    msg = input()
    s.sendall(msg.encode())
    if msg == "exit":
        break
s.close()