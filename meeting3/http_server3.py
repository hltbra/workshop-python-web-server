import socket
import os


def handle_request(request_line, headers, body, client_sock):
    method, uri, protocol = request_line.split()
    if method != 'GET':
        client_sock.send("HTTP/1.0 405 Method Not Allowed\r\n")
        return
    uri = uri[1:]  # skip "/"
    if uri == '':
        content = "\n".join(os.listdir("."))
    elif os.path.exists(uri) and os.path.isfile(uri):
        with open(uri) as f:
            content = f.read()
    else:
        content = "Page not found"
        client_sock.send("HTTP/1.0 404 Not Found\r\n")
        client_sock.send("Content-Length: {}\r\n".format(len(content)))
        client_sock.send("\r\n")
        client_sock.send(content)
        return
    client_sock.send("HTTP/1.0 200 OK\r\n")
    client_sock.send("Content-Length: {}\r\n".format(len(content)))
    client_sock.send("\r\n")
    client_sock.send(content)


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
        handle_request(request_line, headers, body, client_sock)
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