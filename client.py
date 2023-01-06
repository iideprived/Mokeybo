import socket
import pyautogui

port = 1234
socket_queue = 5
encoding = "utf-8"
dataSize = 1024
_screenSize = pyautogui.size()

ipv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipv4.connect((socket.gethostname(), port))


def fromDecodeToDict(decoded):
    return {
        "mousex": [decoded[0]],
        "mousey": [decoded[1]]
    }

while True:
    msg = ipv4.recv(dataSize)
    decoded = (msg.decode(encoding))[1:-1].split()
    mousexpct = ""
    mouseypct = ""
    try:
        mousexpct = float(decoded[0].replace(",", ""))
        mouseypct = float(decoded[1].replace(",", ""))
        pyautogui.moveTo(int(mousexpct * _screenSize.width), int(mouseypct * _screenSize.height) )
    except:
        pass
