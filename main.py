import pygame
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
#creats image
back = pygame.image.load("backg.png")
playeri = pygame.image.load("player.png")
pygame.display.set_icon(playeri)
#Makes screen
sc = pygame.display.set_mode((800,800))
sc.blit(back,(0,0))
# can be color of background
#sc.fill((56,0,67))
#sets background
player = pygame.image
playerx = 370
playery = 400
playerx_ch = 0
#sc.blit(player,(playerx,playery))
# makes player
def play(x,y):
    sc.blit(playeri,(x,y))
#recounds voice
def audio():
# sets up mic
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
    try:
        said = r.recognize_google(audio)
    except Exception as e:
        print("I did not understand that")
    return said


#playerx += 56
# makes so it dose not close
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    voice = audio()
    # makes it jump
    if "jump" in voice:
        # change y axes up
        playery += -35
    if "left" in voice:
        # change y axes left
        playerx += -35
    if "right" in voice:
        # change x axis right
        playerx += 35
    if "down" in voice:
        # change y axes down
        playery += 35
    if "exit" in voice:
        # this exits the game
        run = False
    #playerx_ch = -70.0
    #sc.remove(playeri)
    #playerx += 56
    sc.blit(back,(0,0))
    play(playerx,playery)
    # chages ever thing
    pygame.display.update()

