import socket


def client():
    sock = socket.socket()
    sock.connect(('localhost', 6379))
    sock.send("PING\r\n")
    # TODO: read the response
    sock.close()


client()
