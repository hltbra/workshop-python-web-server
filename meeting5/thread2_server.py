import socket
from threading import Thread

from concurrent.futures import ThreadPoolExecutor


BACKOFF = 100
MAX_THREADS = 100


def reply(client_sock):
    data = client_sock.recv(100 * 1024)
    if data:
        request_line, headers, body = parse_request(data)
        body = "it works\n"
        response = "HTTP/1.0 200 OK\r\nContent-Length: {content_length}\r\n\r\n{body}".format(
            content_length=len(body), body=body)
        client_sock.sendall(response)
    client_sock.close()


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    address = ('0.0.0.0', 8888)
    sock.bind(address)
    sock.listen(BACKOFF)
    print("Web server running on {}".format(address))
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as pool:
        while True:
            client_sock, client_address = sock.accept()
            pool.submit(reply, client_sock)


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