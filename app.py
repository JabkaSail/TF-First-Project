import speech_recognition as sr
import os
import sys
import time
import webbrowser
import requests
from pykeyboard import PyKeyboard
k = PyKeyboard()


def talk(words):
    print(words)
    os.system("say " + words)


talk("Слушаю")


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        zad = r.recognize_google(audio).lower()
        print(zad)

    except sr.UnknownValueError:
        zad = command()
    return zad
p = 1
def makesth(zad):
    if 'wolf' in zad and p == 0:
        talk("Я вас слушаю")
        p = 1
    elif 'music' in zad and p == 1:
        talk("Включаю музыку")
        url = 'https://music.yandex.ru/radio'
        webbrowser.open(url)
        time.sleep(5)
        print('pressed')
        k.tap_key('P')
        p = 0

    elif 'next' in zad and p == 1:
        talk("Следующая композиция")
        k.tap_key('L')
        p = 0


while True:
    makesth(command())
