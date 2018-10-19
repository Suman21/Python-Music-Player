import os, fnmatch
import playsound
from pygame import *
import keyboard

listOfFiles = os.listdir('./Musics')
pattern = "*.mp3"
music=[]
mixer.init()
for entry in listOfFiles: 
    if fnmatch.fnmatch(entry, pattern):
            music.append('./Musics/'+entry)

count=0
length=len(music)
pause=0
while True:
    
    print("1: For Play the Music")
    print("2: For Next Music")
    print("3: For previous Music")
    print("4: For Pause the Music")
    print("5: For Quite")
    c=input()
    if c=="1":
        mixer.music.load(music[count])
        mixer.music.play(-1)
        c='a'

    if c=="2":
        count=(count+1)%length
        mixer.music.load(music[count])
        mixer.music.play(-1)
        c='a'
    if c=="3":
        count=(count-1)%length
        mixer.music.load(music[count])
        mixer.music.play(-1)
        c='a'
    if c=="4":
        if pause==0:
            mixer.music.pause()
            pause=1
        else:
            mixer.music.unpause()
            pause=0
        c='a'  
    if c=="5":
        print("Thanks for listenting")
        break
    print("Now playing "+music[count][9:])
    
