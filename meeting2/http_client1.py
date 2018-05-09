import socket


MSG_LEN = 1024 * 1024


def client():
    sock = socket.socket()
    sock.connect(('httpbin.org', 80))

    # request line
    sock.send("GET /ip HTTP/1.0\r\n")
    # headers
    sock.send("Host: httpbin.org\r\n")
    sock.send("\r\n")

    data = sock.recv(MSG_LEN)
    print(data)
    sock.close()


client()
