import sys
import socket

# How many bytes is the word length?
WORD_LEN_SIZE = 2

def usage():
    print("usage: wordclient.py server port", file=sys.stderr)

packet_buffer = b''

def get_next_word_packet(s):
    global packet_buffer

    while True:
        if len(packet_buffer) >= 2:
            length = int.from_bytes(packet_buffer[:2], "big") + 2

            if len(packet_buffer) >= length:
                packet = packet_buffer[:length]
                packet_buffer = packet_buffer[length:]
                return packet

        data = s.recv(4096)

        if not data:
            return None

        packet_buffer += data

def extract_word(word_packet):
    return word_packet[2:].decode("utf-8")

# Do not modify:

def main(argv):
    try:
        host = argv[1]
        port = int(argv[2])
    except:
        usage()
        return 1

    s = socket.socket()
    s.connect((host, port))

    print("Getting words:")

    while True:
        word_packet = get_next_word_packet(s)

        if word_packet is None:
            break

        word = extract_word(word_packet)

        print(f"    {word}")

    s.close()

if __name__ == "__main__":
    sys.exit(main(sys.argv))