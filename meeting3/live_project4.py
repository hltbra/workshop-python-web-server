import socket


SERVER_ADDRESS = ('localhost', 8888)


def server():
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   sock.bind(SERVER_ADDRESS)
   sock.listen(2)
   try:
       while True:
           client_sock, client_address = sock.accept()
           client_sock.send("HTTP/1.0 200 OK\r\n")
           msg = "it works"
           client_sock.send("Content-Length: {}\r\n".format(len(msg)))
           client_sock.send("\r\n")
           client_sock.send(msg)
           # client_sock.close()
   except (KeyboardInterrupt, EOFError):
       sock.close()


server()