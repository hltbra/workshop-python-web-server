import socket


MSG_LEN = 1024 * 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 6379))

while True:
    try:
        command = raw_input("> ")
    except (KeyboardInterrupt, EOFError):
        break
    # FIXME: check if all data was sent
    sock.send(command + "\r\n")
    # FIXME: read bytes incrementally
    data = sock.recv(MSG_LEN)
    # TODO: support more response types
    print(data[1:])

