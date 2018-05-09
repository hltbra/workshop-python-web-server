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
        data = client_sock.recv(100 * 1024)
        request_line, headers, body = parse_request(data)
        print request_line
        print headers
        print body
        client_sock.send("HTTP/1.0 200 OK\r\n")
        body = "it works\n"
        client_sock.send("Content-Length: {}\r\n".format(len(body)))
        client_sock.send("\r\n")
        client_sock.send(body)
        client_sock.close()


def parse_request(data):
    lines = data.split('\r\n')
    request_line = lines.pop(0)
    headers = {}
    while lines:
        line = lines.pop(0)
        if line == '':
            break
        name, value = line.split(": ", 1)
        headers[name] = value
    body = '\r\n'.join(lines)
    return request_line, headers, body


server()