import socket

SERVER_HOST = "localhost"
SERVER_PORT = 65432
BUFFER_SIZE = 1024
LISTEN_BACKLOG = 1

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listening_socket:
        listening_socket.bind((SERVER_HOST, SERVER_PORT))
        listening_socket.listen(LISTEN_BACKLOG)
        conn, address = listening_socket.accept()

        with conn:
            print(f"recieved msg: {conn.recv(BUFFER_SIZE).decode()}")

            while True:
                msg = input('Enter your message: ')
                conn.sendall(msg.encode())
                data = conn.recv(BUFFER_SIZE)
                print(repr(data)[2:-1])
                if data.decode() == "exit":
                    conn.sendall(b"bye goodbye")
                    break


if __name__ == "__main__":
    run_server()