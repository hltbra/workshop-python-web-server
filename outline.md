# Overview
- Python 3 knowledge
- HTTP 1.0 implementation
- use barebones sockets and standard library, no use of high level abstractions


# Intro to network programming
- communication between computers (a.k.a servers)
  - client/server architecture
  - usually the server waits for commands and return responses forever (while true loop)
- ip
- intro to IPs & ports
- tcp & udp
  - connectionless vs connection-based
  - discuss why HTTP would be built on top of TCP (but not enforced!)
- sockets
- intro to protocols (rules that both parts agree upon)
  - write a simple hello world protocol
  - redis protocol
  - intro to HTTP protocol
- project: create a TCP client, connect to Redis, MySQL, and websites



# Concurrency
- concurrency vs parallelism (james's farner talk!)




# References
- HTTP 1.0 RFC: https://tools.ietf.org/html/rfc1945
- Internet Programming with Python: http://assets.en.oreilly.com/1/event/27/Internet%20Programming%20with%20Python%20Presentation.pdf
- Python Network Programming: http://www.dabeaz.com/python/PythonNetBinder.pdf
- Marc-André Cournoyer + Tube: https://github.com/macournoyer/tube
- Internet Protocol Suite: https://en.wikipedia.org/wiki/Internet_protocol_suite
- Network socket: https://en.wikipedia.org/wiki/Network_socket