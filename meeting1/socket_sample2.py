import socket


def server():
    server_sock = socket.socket()
    server_sock.bind(('localhost', 8888))
    print('Listening on 8888')
    server_sock.listen(1)
    while True:
        client_sock, client_address = server_sock.accept()
        client_sock.send("HELLO THXBYE\n")
        client_sock.close()


server()
