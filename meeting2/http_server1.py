import socket


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    address = ('localhost', 8888)
    sock.bind(address)
    sock.listen(2)
    print("Web server running on {}".format(address))
    while True:
        client_sock, client_address = sock.accept()
        client_sock.send("HTTP/1.0 200 OK\r\n")
        body = "it works\n"
        client_sock.send("Content-Length: {}\r\n".format(len(body)))
        client_sock.send("\r\n")
        client_sock.send(body)
        client_sock.close()


server()