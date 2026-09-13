import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8080))
s.listen(1)
conn, addr = s.accept()
print(conn.recv(1024))
while True:
    msg = input('Enter your message: ')
    conn.sendall(msg.encode())
    data = conn.recv(1024)
    print(repr(data))
    if data.decode() == "exit":
        conn.sendall(b"bye goodbye")
        break
conn.close()
s.close()