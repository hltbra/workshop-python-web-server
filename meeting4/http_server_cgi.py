import socket
import subprocess

import os


def handle_request(request_line, headers, body, client_sock):
    method, uri, protocol = request_line.split()
    script_name = uri[1:].split('/', 1)[0]
    if not os.path.isfile(script_name):
        client_sock.send("HTTP/1.0 404 Not Found\r\n")
        client_sock.send("\r\n")
        client_sock.send("Script not found!")
        return
    path_info = uri[1:].split(script_name, 1)[1]
    env = {}
    env['REQUEST_METHOD'] = method
    env['SCRIPT_NAME'] = script_name
    env['SERVER_NAME'] = 'demoserver'
    env['SERVER_PORT'] = '8888'
    env['SERVER_PROTOCOL'] = protocol
    env['PATH_INFO'] = path_info
    if body:
        env['CONTENT_LENGTH'] = str(len(body))
    if 'Content-Type' in headers:
        env['CONTENT_TYPE'] = headers['Content-Type']
    for header_name, header_value in headers.items():
        cgi_header_name = 'HTTP_{}'.format(header_name.upper().replace('-', '_'))
        env[cgi_header_name] = header_value

    proc = subprocess.Popen([script_name], bufsize=len(body), stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=env)
    stdout = proc.communicate(input=body)[0]
    handle_cgi_response(client_sock, stdout)


def handle_cgi_response(client_sock, stdout):
    resp_headers, resp_body = stdout.split('\r\n\r\n')
    response_headers = dict(header.split(': ') for header in resp_headers.split('\r\n'))
    client_sock.send('HTTP/1.0 {}\r\n'.format(response_headers.pop('Status')))
    for header_name, header_value in response_headers.items():
        client_sock.send('{}: {}\r\n'.format(header_name, header_value))
    client_sock.send('\r\n')
    client_sock.send(resp_body)


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    address = ('localhost', 8888)
    sock.bind(address)
    sock.listen(2)
    print("Web server running on {}".format(address))
    while True:
        client_sock, client_address = sock.accept()
        data = client_sock.recv(1000 * 1024)
        if not data:
            continue
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
