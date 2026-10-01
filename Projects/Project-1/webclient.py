import socket
import sys

host = sys.argv[1]
port = 80

if len(sys.argv) > 2:
    port = int(sys.argv[2])

s = socket.socket()

server = (host, port)

try:
    s.connect(server)

    request = "GET / HTTP/1.1\r\n"
    request += "Host: " + host + "\r\n"
    request += "Connection: close\r\n"
    request += "\r\n"

    s.sendall(request.encode("ISO-8859-1"))

    while True:
        data = s.recv(4096)

        if not data:
            break

        text = data.decode("ISO-8859-1")
        print(text, end="")

finally:
    s.close()