import socket
import sys


SERVER_ADDRESS = ('localhost', 8888)


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(SERVER_ADDRESS)
    sock.listen(2)
    try:
        while True:
            client_sock, client_address = sock.accept()
            data = client_sock.recv(1024)
            if data.strip() == 'PING':
                client_sock.send("PONG\n")
            else:
                client_sock.send("ERR: COMMAND NOT FOUND\n")
            client_sock.close()
    except (KeyboardInterrupt, EOFError):
        sock.close()


def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(SERVER_ADDRESS)
    sock.send("PING")
    data = sock.recv(1024)
    print(data)
    sock.close()


if sys.argv[1] == 'server':
    server()
elif sys.argv[1] == 'client':
    client()