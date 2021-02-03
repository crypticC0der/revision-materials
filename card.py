from sys import argv
from os import system
from time import sleep
from random import randrange
argv.append("lol")
voice = argv[1] == "-v"
if voice:
    from gtts import gTTS
    from mutagen.mp3 import MP3

cards = open("cards").read().split("\\/")
cards = [x.split("/\\") for x in cards]

def getCard():
    o = cards[randrange(0,len(cards))]
    if len(o[0]) ==0 or len(o[1]) ==0:
        return getCard()
    return o

card = getCard()
if voice:
    tts = gTTS(card[0],lang="en",tld="com")
    tts.save("front.mp3")
    tts = gTTS(card[1],lang="en",tld="com")
    tts.save("back.mp3")
    
print(card[0])
if voice:
    f = MP3("back.mp3")
    system("mpv front.mp3 2&>/dev/null")
    sleep(f.info.length+5)
    system("mpv back.mp3 2&>/dev/null")
else:
    sleep(5)
print(card[1])
