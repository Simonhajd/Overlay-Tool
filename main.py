import pyautogui
import osascript
import tkinter
from pynput import keyboard
import subprocess
import os
from playsound import playsound
from screeninfo import get_monitors

user_selection = None
service = input("\nEnter S for Spotify | Enter A for Apple Music\n")
subprocess.Popen(["python3", "controltest.py"])
controller = keyboard.Controller()
def on_press(key):
    global x
    try:
        if key == keyboard.Key.space:
            
            subprocess.run(("open -a "+service), shell=True)
    except Exception as e:
        print(f"Error: {e}")
if service == "S" or service == "s": 
    service = "Spotify"
    print("Opening Spotify")
if service == "A" or service == "a":
    service = "Music"
    print("Opening Apple Music")
listener = keyboard.Listener(on_press=on_press)
listener.start()

monitor = get_monitors()[0]
screen_width = monitor.width
screen_height = monitor.height
while True: 

    x, y = pyautogui.position()
    positionStr = ('X' + str(x)).rjust(4)
    y = 100 - (y/(screen_height/100))

    print(x, end='')

    if x >= screen_width-20:
      
        playsound('funk.aiff', block=False)
        pyautogui.moveTo((screen_width/2), None)

        # Use pynput for next track
        controller.press(keyboard.Key.media_next)

        controller.release(keyboard.Key.media_next)
   
        print("Next")
        
    if x <= 20:
        os.system(f'afplay funk.aiff')
        pyautogui.moveTo((screen_width/2), None)
        # Use pynput for previous track
        controller.press(keyboard.Key.media_previous)
        controller.release(keyboard.Key.media_previous)
        
        print("Prev")
        
    if y <= 2:
        os.system(f'afplay funk.aiff')
        pyautogui.moveTo(None, (screen_height/2))
        # Use pynput for play/pause
        controller.press(keyboard.Key.media_play_pause)
        controller.release(keyboard.Key.media_play_pause)
        
        print("Paused/Played")
    osascript.osascript("set volume output volume "+str(y))
    print('\b' * len(positionStr), end='', flush=True) 
    print("| x: ", x, end='\r')
    
        



