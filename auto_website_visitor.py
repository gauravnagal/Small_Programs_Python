'''
Author: Gaurav Nagal
Description: This program automatically visits the first url in the list, waits for 10 seconds, closes the tab and
opens-up the next url on the list in a loop for 50 times.
Uses: Increase productivity by automatically visiting certain websites for example, news, weather etc for a quick
period of time to get updates.
'''

import webbrowser
import time
from pynput import keyboard
from pykeyboard import PyKeyboard

k = PyKeyboard()

urls = ['https://github.com/gauravnagal/',
        'https://www.linkedin.com/in/gaurav-nagal-20836327/']

def on_press_start(key):
    if key == keyboard.Key.enter:
        print('starting...')
        return False

def on_press_end(key):
    if key == keyboard.Key.end:
        print('ended by user')
        return False

with keyboard.Listener(on_press = on_press_start) as listener:
    print('press Enter key to start')
    listener.join() # wait for Enter...

# open new tabs 50 times
with keyboard.Listener(on_press = on_press_end) as listener:
    for _ in range(50):
        print('still running...press End key to quit')
        for url in urls:
            webbrowser.open(url, new=0)
            time.sleep(10)
            # close previously opened tab
            k.press_keys([k.control_key, 'w'])

        if not listener.running:
            break