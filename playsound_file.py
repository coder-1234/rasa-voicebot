from playsound import playsound
import os

def function_sound():
    playsound('./welcome.mp3')
    os.remove("./welcome.mp3")
