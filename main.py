import pygame
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from rp import *
import pynput
import fansi
import numpy

def audio_do():
    import speech_recognition as sr
    with sr.Microphone() as source:
        recognizer=sr.Recognizer()
        recognizer.adjust_for_ambient_noise(source)
        for _ in range(100) :
            try:
                audio=recognizer.listen(source,timeout=.25,phrase_time_limit=2)
                text=recognizer.recognize_google(audio)
                speech_text_handler(text)
                fansi_print(text,'red')
            except sr.WaitTimeoutError:
                fansi_print('Timed out','red','bold')
            except sr.UnknownValueError:
                fansi_print('Didnt understand','red','bold')
    return text

def speech_text_handler(text):
    text=text.lower()
    if 'north' in text:                     command_handler('north')
    elif 'south' in text or 'self' in text: command_handler('south')
    elif 'east' in text:                    command_handler('east')
    elif 'wes' in text or 'west' in text:   command_handler('west')
    elif 'stop' in text:                    command_handler('stop')
    elif 'exit' in text:                    command_handler('exit')
    else:
        return


keyboard=pynput.keyboard.Controller()
from time import sleep
def press_key(key):
    keyboard.press(key)
    sleep(.05)
    keyboard.release(key)

last_command=''
def command_handler(command):
    #Don't do duplicate commands in a row
    global last_command
    if last_command==command:
        return
    last_command=command

    print("COMMAND:",command)
    text_to_speech("do "+command)

    if   'north' == command:press_key("w")
    elif 'south' == command:press_key("s")
    elif 'east'  == command:press_key("d")
    elif 'west'  == command:press_key("a")
    elif 'stop'  == command:press_key("f")
    elif 'exit'  == command:press_key("x")

for _ in range(10):
    run_as_new_thread(audio_do)
    sleep(random_float())
    print("STARTED",_)
