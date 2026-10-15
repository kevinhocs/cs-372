import socket
import time


def system_seconds_since_1900():
    return int(time.time()) + 2208988800


def get_nist_time():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("time.nist.gov", 37))
    data = s.recv(4)
    s.close()

    return int.from_bytes(data, "big")


def main():
    print(f"NIST time  : {get_nist_time()}")
    print(f"System time: {system_seconds_since_1900()}")


if __name__ == "__main__":
    main()
