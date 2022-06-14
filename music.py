# from playsound import playsound
# playsound('sounds/beat1.mp3')

from pygame import mixer
import time
# import keyboard
from pynput import keyboard



mixer.init() #Initialzing pyamge mixer


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        if key.char == "q":
            mixer.Channel(0).play(mixer.Sound('sounds/beat1.mp3'))
            # break
        if key.char == "w":
            # mixer.Channel(0).stop()
            mixer.Channel(0).play(mixer.Sound('sounds/beat2.mp3'))
        if key.char == "e":
            mixer.Channel(0).play(mixer.Sound('sounds/beat3.mp3'))
        if key.char == "r":
            mixer.Channel(0).play(mixer.Sound('sounds/beat4.mp3'))
        if key.char == "t":
            mixer.Channel(0).play(mixer.Sound('sounds/beat5.mp3'))
        if key.char == "y":
            mixer.Channel(0).play(mixer.Sound('sounds/beat6.mp3'))
        if key.char == "u":
            mixer.Channel(0).play(mixer.Sound('sounds/beat7.mp3'))
        if key.char == "i":
            mixer.Channel(0).play(mixer.Sound('sounds/beat8.mp3'))
        if key.char == "o":
            mixer.Channel(0).play(mixer.Sound('sounds/beat9.mp3'))
        if key.char == "p":
            mixer.Channel(0).play(mixer.Sound('sounds/beat10.mp3'))
            
        #FX ywj ehelj bne
        if key.char == "Q":
            mixer.Channel(1).play(mixer.Sound('sounds/fx1.mp3'))
        if key.char == "W":
            mixer.Channel(1).play(mixer.Sound('sounds/fx2.mp3'))
        if key.char == "E":
            mixer.Channel(1).play(mixer.Sound('sounds/fx3.mp3'))
        if key.char == "R":
            mixer.Channel(1).play(mixer.Sound('sounds/fx4.mp3'))
        if key.char == "T":
            mixer.Channel(1).play(mixer.Sound('sounds/fx5.mp3'))
        if key.char == "Y":
            mixer.Channel(1).play(mixer.Sound('sounds/fx6.mp3'))
        if key.char == "U":
            mixer.Channel(1).play(mixer.Sound('sounds/fx7.mp3'))
        if key.char == "I":
            mixer.Channel(1).play(mixer.Sound('sounds/fx8.mp3'))
        if key.char == "O":
            mixer.Channel(1).play(mixer.Sound('sounds/fx9.mp3'))
        if key.char == "P":
            mixer.Channel(1).play(mixer.Sound('sounds/fx10.mp3'))
        if key.char == "A":
            mixer.Channel(1).play(mixer.Sound('sounds/fx11.mp3'))
        if key.char == "S":
            mixer.Channel(1).play(mixer.Sound('sounds/fx12.mp3'))

        #Voice
        if key.char == "g":
            mixer.Channel(2).play(mixer.Sound('sounds/voice1.mp3'))
        if key.char == "G":
            mixer.Channel(2).play(mixer.Sound('sounds/voice2.mp3'))
        if key.char == "j":
            mixer.Channel(2).play(mixer.Sound('sounds/voice3.mp3'))
        if key.char == "J":
            mixer.Channel(2).play(mixer.Sound('sounds/voice4.mp3'))
        if key.char == "k":
            mixer.Channel(2).play(mixer.Sound('sounds/voice5.mp3'))
        if key.char == "K":
            mixer.Channel(2).play(mixer.Sound('sounds/voice6.mp3'))
        if key.char == "l":
            mixer.Channel(2).play(mixer.Sound('sounds/voice7.mp3'))
        if key.char == "L":
            mixer.Channel(2).play(mixer.Sound('sounds/voice8.mp3'))
        if key.char == "z":
            mixer.Channel(2).play(mixer.Sound('sounds/voice9.mp3'))
        if key.char == "Z":
            mixer.Channel(2).play(mixer.Sound('sounds/voice10.mp3'))
        if key.char == "x":
            mixer.Channel(2).play(mixer.Sound('sounds/voice11.mp3'))

    except AttributeError:
        print('special key {0} pressed'.format(
            key))

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()





