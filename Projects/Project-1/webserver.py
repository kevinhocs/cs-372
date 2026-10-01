import socket
import sys

port = 28333

if len(sys.argv) > 1:
    port = int(sys.argv[1])

s = socket.socket()

s.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1
)

s.bind(("", port))
s.listen()

try:
    while True:
        client_socket, client_addr = s.accept()

        request = b""

        while b"\r\n\r\n" not in request:
            data = client_socket.recv(4096)

            if not data:
                break

            request += data

        body = "Hello!"

        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/plain\r\n"
        response += "Content-Length: 6\r\n"
        response += "Connection: close\r\n"
        response += "\r\n"
        response += body

        client_socket.sendall(
            response.encode("ISO-8859-1")
        )

        client_socket.close()

finally:
    s.close()