import os
import signal
import time

import psutil


def sigint_handler(signum, frame):
    print(os.getpid())
    print('CTRL + C/Z Pressed, app is now killed!')
    os.kill(os.getpid(), 9)




count = 0
while True:
    print('1')
    time.sleep(1)
    count += 1
    if count % 5 == 0:
        signal.signal(signal.SIGINT, sigint_handler)
