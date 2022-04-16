import time
import keyboard
while True:
    keyboard.write(f'Я бот!')
    keyboard.press("enter")
    keyboard.release("enter")
    time.sleep(0.9)

import keyboard
while True:
    keyboard.on_release(lambda e: print(e.name))