import pygame
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
#creats image
back = pygame.image.load("spath.png")
playeri = pygame.image.load("testgal.png")
monster = pygame.image.load("tsarm.png")
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
        r.adjust_for_ambient_noise(source)
        #r.adjust_for_ambient_noise(source)
       # audio = r.listen(source,timeout=3,phrase_time_limit=1)
        try:

            audio = r.listen(source,timeout=0.75,phrase_time_limit=1)
        except:
            pass

       # r.operation_timeout
        said = ""
       # r.operation_timeout

    try:
        said = r.recognize_google(audio)
        print(str(said))
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
    print(voice)
    # makes it go north
    if "North" in voice:
        hi = 1
        #print(hi)
        voice = audio()
        while hi == 1:
            if playery <= 0:
                playery = 0
            else:
                for i in range(0,5):
                    playery += -5
            # updates and makes to go forward
            sc.blit(back, (0, 0))
            play(playerx, playery)
            pygame.display.update()
            #playery += -35
            voice = audio()
           # print(voice)
            # stops going forward
            if "stop" in voice:
                hi = 0
        # change y axes up
        #playery += -35
        print(voice)
    if "West" in voice:
        hi = 1
        while hi == 1:
        # change y axes left
            if playerx <= 0:
                playerx = 0
            else:
                playerx += -95
            sc.blit(back, (0, 0))
            play(playerx, playery)
            pygame.display.update()
            voice = audio()
            if "stop" in voice:
                hi = 0

    if "East" in voice:
        hi = 1
        while hi == 1:
        # change x axis right
            if playerx >= 800:
                playerx = 780
            else:
                playerx += 95
            sc.blit(back, (0, 0))
            play(playerx, playery)
            pygame.display.update()
            voice = audio()
            if "stop" in voice:
                hi = 0
    if "South" in voice:
        hi = 1
        while hi == 1:
        # change y axes down
            if playery >= 800:
                playery = 0
            else:
                playery += 45
            sc.blit(back, (0, 0))
            play(playerx, playery)
            pygame.display.update()
            voice = audio()
            if "stop" in voice:
                hi = 0
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