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
        #beat   
        if key.char == "q":
            mixer.Channel(0).play(mixer.Sound('sounds/beat1.wav'))
            # break
        if key.char == "w":
            # mixer.Channel(0).stop()
            mixer.Channel(0).play(mixer.Sound('sounds/beat2.wav'))
        if key.char == "e":
            mixer.Channel(0).play(mixer.Sound('sounds/beat3.wav'))
        if key.char == "r":
            mixer.Channel(0).play(mixer.Sound('sounds/beat4.wav'))
        if key.char == "t":
            mixer.Channel(0).play(mixer.Sound('sounds/beat5.wav'))
        if key.char == "y":
            mixer.Channel(0).play(mixer.Sound('sounds/beat6.wav'))
        if key.char == "u":
            mixer.Channel(0).play(mixer.Sound('sounds/beat7.wav'))
        if key.char == "i":
            mixer.Channel(0).play(mixer.Sound('sounds/beat8.wav'))
        if key.char == "o":
            mixer.Channel(0).play(mixer.Sound('sounds/beat9.wav'))
        # if key.char == "p":
        #     mixer.Channel(0).play(mixer.Sound('sounds/beat10.wav'))
            
        #FXLong ywj ehelj bne
        if key.char == "Q":
            mixer.Channel(1).play(mixer.Sound('sounds/fxlong1.wav'))
    
        if key.char == "W":
            mixer.Channel(1).play(mixer.Sound('sounds/fxlong2.wav'))
            
        
            
        if key.char == "R":
            mixer.Channel(1).play(mixer.Sound('sounds/fxlong3.wav'))
            
        if key.char == "T":
            mixer.Channel(1).play(mixer.Sound('sounds/fxlong4.wav'))
            
        
            
        if key.char == "U":
            mixer.Channel(1).play(mixer.Sound('sounds/fxlong5.wav'))
            
        if key.char == "I":
            mixer.Channel(1).play(mixer.Sound('sounds/fxlong6.wav'))
             
         #FXShort ywj ehelj bne
        if key.char == "E":
                mixer.Channel(3).play(mixer.Sound('sounds/fxshort1.wav'))
        if key.char == "Y":
                    mixer.Channel(3).play(mixer.Sound('sounds/fxshort3.wav'))
        if key.char == "O":
                    mixer.Channel(3).play(mixer.Sound('sounds/fxshort5.wav'))
        if key.char == "P":
                    mixer.Channel(3).play(mixer.Sound('sounds/fxshort2.wav'))
        if key.char == "A":
                    mixer.Channel(3).play(mixer.Sound('sounds/fxshort6.wav'))
        if key.char == "S":
                    mixer.Channel(3).play(mixer.Sound('sounds/fxshort4.wav'))


        #Voice
        if key.char == "g":
            mixer.Channel(2).play(mixer.Sound('sounds/shodorgoyos.wav'))
        if key.char == "G":
            mixer.Channel(2).play(mixer.Sound('sounds/wooow.wav'))
        if key.char == "j":
            mixer.Channel(2).play(mixer.Sound('sounds/bayrlalaa.wav'))
        if key.char == "J":
            mixer.Channel(2).play(mixer.Sound('sounds/ahiad1.wav'))
        if key.char == "k":
            mixer.Channel(2).play(mixer.Sound('sounds/odoobolnoodaraagin.wav'))
        if key.char == "K":
            mixer.Channel(2).play(mixer.Sound('sounds/yaalaayaalaagenee.wav'))
        if key.char == "p":
            mixer.Channel(2).play(mixer.Sound('sounds/bichiniiajiltanymu.wav'))
        if key.char == "l":
            mixer.Channel(2).play(mixer.Sound('sounds/yaaygoybnshde.wav'))
        # if key.char == "L":
        #     mixer.Channel(2).play(mixer.Sound('sounds/yaaygoybnshde.wav'))
        if key.char == "x":
             mixer.Channel(2).play(mixer.Sound('sounds/aliwahdaadansaa.wav'))
        if key.char == "Z":
            mixer.Channel(2).play(mixer.Sound('sounds/soliotei.wav'))
        if key.char == "z":
            mixer.Channel(2).play(mixer.Sound('sounds/yaaraadyahawde.wav'))
        if key.char == "2":
            # mixer.Channel(2).play(mixer.Sound('sounds/voice11.mp3'))
            mixer.Channel(0).stop()
            mixer.Channel(1).stop()
            mixer.Channel(2).stop()
            mixer.Channel(3).stop()


    except AttributeError:
        print('special key {0} pressed'.format(
            key))

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()






