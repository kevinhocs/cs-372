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

        if not request:
            client_socket.close()
            continue

        request_text = request.decode("ISO-8859-1")
        path = request_text.split(" ")[1]
        filename = path.lstrip("/")

        try:
            with open(filename, "r") as file:
                body = file.read()

            if filename.endswith(".html"):
                content_type = "text/html"
            else:
                content_type = "text/plain"

            status = "200 OK"

        except FileNotFoundError:
            body = "404 Not Found"
            content_type = "text/plain"
            status = "404 Not Found"

        response = f"HTTP/1.1 {status}\r\n"
        response += f"Content-Type: {content_type}\r\n"
        response += f"Content-Length: {len(body.encode('ISO-8859-1'))}\r\n"
        response += "Connection: close\r\n"
        response += "\r\n"
        response += body

        client_socket.sendall(
            response.encode("ISO-8859-1")
        )

        client_socket.close()

finally:
    s.close()