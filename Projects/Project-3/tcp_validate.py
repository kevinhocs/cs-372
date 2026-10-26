def ip_to_bytes(ip):
    return bytes(int(part) for part in ip.split("."))


def build_pseudo_header(source_bytes, dest_bytes, tcp_length):
    return (source_bytes
        + dest_bytes
        + b'\x00\x06'
        + tcp_length.to_bytes(2, "big"))


def compute_checksum(pseudo_header, tcp_data):
    data = pseudo_header + tcp_data

    if len(data) % 2 == 1:
        data += b'\x00'

    total = 0

    for i in range(0, len(data), 2):
        total += int.from_bytes(data[i:i+2], "big")
        total = (total & 0xffff) + (total >> 16)

    return (~total) & 0xffff


def validate_packet(i):
    with open(f"tcp_addrs_{i}.txt", "r") as f:
        source_ip, dest_ip = f.read().split()

    with open(f"tcp_data_{i}.dat", "rb") as f:
        tcp_data = f.read()

    source_bytes = ip_to_bytes(source_ip)
    dest_bytes = ip_to_bytes(dest_ip)

    pseudo_header = build_pseudo_header(source_bytes, dest_bytes, len(tcp_data))

    original_checksum = int.from_bytes(tcp_data[16:18], "big")
    tcp_zero_cksum = tcp_data[:16] + b'\x00\x00' + tcp_data[18:]

    calculated_checksum = compute_checksum(pseudo_header, tcp_zero_cksum)

    return original_checksum == calculated_checksum


def main():
    for i in range(10):
        print("PASS" if validate_packet(i) else "FAIL")


if __name__ == "__main__":
    main()