import pygame
import speech_recognition as speech
import threading as thread
from time import sleep
from random import randint

# Load sprites to memory
back_img = pygame.image.load("spath.png")
health_img = pygame.image.load("health.png")
player_img = pygame.image.load("testgal.png")
monster_img = pygame.image.load("tsarm.png")

# Initialize window
pygame.display.set_icon(player_img)
screen = pygame.display.set_mode((800, 800))

# Draw GUI elements to screen
screen.blit(health_img, (0, 0))

# Initialize player position
player_x = 400
player_y = 400

# Initialize speech recognition object
recognizer = speech.Recognizer()

def random_bground():
    if randint(0, 1):
        return pygame.image.load("spath.png")
    return pygame.image.load("spath2.png")

def move_player_to(x, y):
    screen.blit(player_img, (x, y))

def audio_clip():
    # Attempt to get audio clip from user
    audio = {}
    with speech.Microphone() as mic_handle:
        try:
            # Get audio from microphone
            audio = recognizer.listen(mic_handle, timeout=100, phrase_time_limit=100)
            # Adjust microphone for background noise
            recognizer.adjust_for_ambient_noise(audio)
        except Exception as e:
            print("Warning: " + str(e))
            pass

    return audio

def speech_input():
    '''
    Attempts to get user input as a string. If Google fails to get user input, will recursively try until input is "gotten"
    :return:
    '''
    try:
        return recognizer.recognize_google(audio_clip())
    except Exception as e:
        if str(e) == "":
            print("Invalid input!")
        else:
            print("Error: " + str(e))
        return speech_input()

def user_input():
    global player_x, player_y, screen, player_img

    while True:
        # Get text from user and output it to console
        input_text = speech_input()
        print("User input: \"" + input_text + "\"")

        if "North" in input_text:
            for i in range(25):
                player_y -= 4

                if player_y < 0:
                    player_y = 800
                    back_img = random_bground()

                sleep(0.01)
        if "West" in input_text:
            for i in range(25):
                player_x -= 4

                if player_x < 0:
                    player_x = 800
                    back_img = random_bground()

                sleep(0.01)
        if "East" in input_text:
            for i in range(25):
                player_x += 4

                if player_x > 800:
                    player_x = 0
                    back_img = random_bground()

                sleep(0.01)
        if "South" in input_text:
            for i in range(25):
                player_y += 4

                if player_y > 800:
                    player_y = 0
                    back_img = random_bground()

                sleep(0.01)
        if "check health" in input_text:
            print("Check health")
        if "exit" in input_text:
            exit(0)

def render():
    # Handle window events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

    # Clear last frame
    screen.blit(back_img, (0, 0))

    # Draw player at (player_x, player_y)
    move_player_to(player_x, player_y)

    # Swap framebuffer (Output updated rendered image to screen)
    pygame.display.update()

# Main loop
thread.Thread(target=user_input, daemon=True).start()

while True:
    render()