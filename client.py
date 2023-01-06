import socket

port = 1234
socket_queue = 5
encoding = "utf-8"
dataSize = 1024

ipv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipv4.connect((socket.gethostname(), port))

while True:
    msg = ipv4.recv(dataSize)
    decoded = (msg.decode(encoding))