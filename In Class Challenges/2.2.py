def subnet(ip, mask):
    network = []
    host = []

    for i in range(4):
        network.append(ip[i] & mask[i])
        host.append(ip[i] & (~mask[i] & 0xff))

    return (network, host)

print(subnet([192,168,17,2], [255,255,248,0]))
print(subnet([192,168,17,2], [255,0,0,0]))