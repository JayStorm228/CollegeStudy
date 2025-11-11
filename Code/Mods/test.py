import keyboard
import time as t
while not(keyboard.is_pressed('esc')): 
    if keyboard.is_pressed('w'):
        print(1)
        t.sleep(0.2)