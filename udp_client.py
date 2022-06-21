#!/usr/bin/python3
# Black Hat Python 2nd Ed. Basic UDP Client

import socket

target_host = "127.0.0.1"
target_port = 9997

# Create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some data
client.sendto(b"QWERTY", (target_host, target_port))

# Receive response data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()