import threading
import time
from client import *


class AutoFight:
    def __init__(self):
        self.isFighting = False

    def loop(self):
        while self.isFighting:
            press(Ps4Controls.R2)
            time.sleep(0.5)
            release(Ps4Controls.R2)
            time.sleep(0.1)
            press(Ps4Controls.L1)
            time.sleep(0.1)
            click(Ps4Controls.SQUARE)
            time.sleep(0.1)
            click(Ps4Controls.TRIANGLE)
            time.sleep(0.1)
            click(Ps4Controls.R2)
            time.sleep(0.1)
        else:
            release(Ps4Controls.L1)

    def fight(self):
        if self.isFighting:
            return
        self.isFighting = True
        t = threading.Thread(target=self.loop)
        t.start()

    def stop(self):
        self.isFighting = False


autoFightInstance = AutoFight()
