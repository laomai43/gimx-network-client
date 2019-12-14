import threading
import time
from pynput import keyboard
from client import *
from pynput.keyboard import Key, KeyCode
from functools import partial
from singleton import autoFightInstance

maxSpeed = 200



myDict = {
    'p': partial(press, button=Ps4Controls.PS),
    'o': partial(press, button=Ps4Controls.CIRCLE),
    'w': partial(move, button=Ps4Controls.LEFT_STICK_Y, speed=-maxSpeed),
    's': partial(move, button=Ps4Controls.LEFT_STICK_Y, speed=maxSpeed),
    'a': partial(move, button=Ps4Controls.LEFT_STICK_X, speed=-maxSpeed),
    'd': partial(move, button=Ps4Controls.LEFT_STICK_X, speed=maxSpeed),
    'i': partial(move, button=Ps4Controls.RIGHT_STICK_Y, speed=-maxSpeed),
    'k': partial(move, button=Ps4Controls.RIGHT_STICK_Y, speed=maxSpeed),
    'j': partial(move, button=Ps4Controls.RIGHT_STICK_X, speed=-maxSpeed),
    'l': partial(move, button=Ps4Controls.RIGHT_STICK_X, speed=maxSpeed),
    '1': partial(press, button=Ps4Controls.L1),
    '2': partial(press, button=Ps4Controls.L2),
    '0': partial(press, button=Ps4Controls.R1),
    '9': partial(press, button=Ps4Controls.R2),
    '4': partial(press, button=Ps4Controls.UP),
    '5': partial(press, button=Ps4Controls.DOWN),
    '6': partial(press, button=Ps4Controls.LEFT),
    '7': partial(press, button=Ps4Controls.RIGHT),
    'm': partial(autoFightInstance.fight),
    'n': partial(autoFightInstance.stop),

}

myDict2 = {
    'p': partial(release, button=Ps4Controls.PS),
    'o': partial(release, button=Ps4Controls.CIRCLE),
    'w': partial(move, button=Ps4Controls.LEFT_STICK_Y, speed=0),
    's': partial(move, button=Ps4Controls.LEFT_STICK_Y, speed=0),
    'a': partial(move, button=Ps4Controls.LEFT_STICK_X, speed=0),
    'd': partial(move, button=Ps4Controls.LEFT_STICK_X, speed=0),
    'i': partial(move, button=Ps4Controls.RIGHT_STICK_Y, speed=0),
    'k': partial(move, button=Ps4Controls.RIGHT_STICK_Y, speed=0),
    'j': partial(move, button=Ps4Controls.RIGHT_STICK_X, speed=0),
    'l': partial(move, button=Ps4Controls.RIGHT_STICK_X, speed=0),
    '1': partial(release, button=Ps4Controls.L1),
    '2': partial(release, button=Ps4Controls.L2),
    '0': partial(release, button=Ps4Controls.R1),
    '9': partial(release, button=Ps4Controls.R2),
    '4': partial(release, button=Ps4Controls.UP),
    '5': partial(release, button=Ps4Controls.DOWN),
    '6': partial(release, button=Ps4Controls.LEFT),
    '7': partial(release, button=Ps4Controls.RIGHT),
}

myDict1 = {
    Key.media_previous: '1',
    Key.media_volume_up: 'a',
    Key.media_volume_down: 's',
}


def get_original_key(key):
    try:
        return str(key.char)
    except AttributeError:
        return myDict1[key]


def on_press(key):
    print(get_original_key(key))
    action = myDict.get(get_original_key(key))
    if action:
        action()

    # try:
    #     print('alphanumeric key {0} pressed'.format(key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(key))


def on_release(key):
    print(get_original_key(key))
    action = myDict2.get(get_original_key(key))
    if action:
        action()
    # try:
    #     print('alphanumeric key {0} release'.format(key.char))
    #     button = myDict[str(key.char)]
    #     release(button)
    # except AttributeError:
    #     print('special key {0} released'.format(key))
    #
    # if key == keyboard.Key.esc:
    #     return False


if __name__ == '__main__':

    while True:
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
