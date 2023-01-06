import string
import scheduler
from pynput import keyboard
from pynput import mouse

from apscheduler.schedulers.background import BackgroundScheduler

schedule = BackgroundScheduler()
pressedKeys = []
mousex = 0
mousey = 0
mouseClickLeft = []
mouseClickRight= []
mouseClickMiddle= []
mouseScroll = []


def some_job():
    global pressedKeys, mousex, mousey
    return str(pressedKeys)


def on_press(key):
    global pressedKeys
    if key not in pressedKeys:
        pressedKeys += [key]


def on_release(key):
    global pressedKeys
    if key in pressedKeys:
        pressedKeys.remove(key)


def get_pressed_keys():
    global pressedKeys
    return pressedKeys


def on_move(x, y):
    global mousex, mousey
    mousex = x
    mousey = y

def on_click(x, y, button, pressed):
    mouseClickLeft = [[x, y, button, pressed]]


def on_scroll(x, y, dx, dy):
    pass


schedule.add_job(some_job, 'interval', seconds=float(1 / 60))
schedule.start()

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as keyboardListener:
    keyboardListener.join()

with mouse.Listener(
        on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mouseListener:
    mouseListener.join()

# while True:
#     pressedKeys = []
#     for letter in string.ascii_lowercase:
#         if keyboard.is_pressed(letter):
#             pressedKeys += letter
#
#     for digit in string.digits:
#         if keyboard.is_pressed(digit):
#             pressedKeys += digit
#
#     for modifier in list(keyboard.sided_modifiers):
#         if keyboard.is_pressed(modifier):
#             pressedKeys += [modifier]
#
#     print(str(pressedKeys))
