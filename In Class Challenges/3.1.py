
def encode_data(message, value):
    message = message.encode("utf-8")
    length = 2 + len(message) + 4
    return bytearray(
        length.to_bytes(2, "big")
        + message
        + value.to_bytes(4, "big", signed=True)
    )

def decode_data(data):
    length = int.from_bytes(data[:2], "big")
    message = data[2:length - 4].decode("utf-8")
    value = int.from_bytes(data[length - 4:length], "big", signed=True)
    return message, value

encoded = encode_data("Hello", -42)
decoded = decode_data(encoded)

print(encoded)
print(decoded)