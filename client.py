import socket

SERVER_HOST = "127.0.0.1"

SERVER_PORT = 65432

BUFFER_SIZE = 1024


def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        client_socket.sendall(b"Hello World!")

        while True:
            print(f"response msg: {client_socket.recv(BUFFER_SIZE).decode()}")
            msg = input("Enter your message: ")
            client_socket.sendall(msg.encode())
            if msg == "exit":
                break

if __name__ == "__main__":
    run_client()