from pynput import keyboard
from screen import Screen
import os

screen = Screen()
positions = [(screen.max_rows//2, screen.max_cols//2)]

def fill_and_draw():
    strings = [' '*screen.max_cols for _ in range(screen.max_rows)]
    for i,(r,c) in enumerate(positions):
        fill = 'O'
        if(i==0):
            fill = 'o'
        mod = strings[r]
        strings[r] = ' '*c + fill + ' '*(screen.max_cols - c - 1)
    screen._draw_from_rows(strings)

def listen():
    def on_press(key):
        try:
            (r,c) = positions[0]
            keyid = key.char
        except AttributeError:
            keyid = key
        if(keyid == keyboard.Key.up):
            positions.insert(0,(r-1,c))
        elif(keyid == keyboard.Key.down):
            positions.insert(0,(r+1,c))
        elif(keyid == keyboard.Key.right):
            positions.insert(0,(r,c+1))
        elif(keyid == keyboard.Key.left):
            positions.insert(0,(r,c-1))
        fill_and_draw()

    os.system("stty -echo")
    try:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except:
        os.system("stty echo")
        exit(1)

listen()