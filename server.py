import socket
import json
import pyautogui

port = 1234
socket_queue = 5
encoding = "utf-8"
hostname = socket.gethostname()  # Change to public ip

ipv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipv4.bind((hostname, port))
ipv4.listen(socket_queue)

client_socket, address = ipv4.accept()
print(f"Connection from {address} has been established!")

while True:
    mouse_x = pyautogui.position().x / float(3840)
    mouse_y = pyautogui.position().y / float(2180)
    client_socket.send(bytes(f"{[mouse_x, mouse_y]}", encoding))
