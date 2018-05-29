import errno
import os
import signal
import socket


BACKOFF = 100


# copied from https://ruslanspivak.com/lsbaws-part3/
def grim_reaper(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(
                -1,          # Wait for any child process
                 os.WNOHANG  # Do not block and return EWOULDBLOCK error
            )
        except OSError:
            return

        if pid == 0:  # no more zombies
            return



def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    address = ('0.0.0.0', 8888)
    sock.bind(address)
    sock.listen(BACKOFF)
    print("Web server running on {}".format(address))

    signal.signal(signal.SIGCHLD, grim_reaper)

    while True:
        try:
            client_sock, client_address = sock.accept()
        except IOError as e:
            if e.args[0] == errno.EINTR:

                continue
            else:
                raise

        if os.fork() == 0:
            sock.close()
            data = client_sock.recv(100 * 1024)
            if data:
                request_line, headers, body = parse_request(data)
                body = "it works\n"
                response = "HTTP/1.0 200 OK\r\nContent-Length: {content_length}\r\n\r\n{body}".format(
                    content_length=len(body), body=body)
                client_sock.sendall(response)
            client_sock.close()
            os._exit(0)  # not sys.exit()
        else:
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