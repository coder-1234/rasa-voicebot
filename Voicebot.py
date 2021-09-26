## Run this command in terminal  before executing this program
## rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
## and also run this in seperate terminal
## rasa run actions

from playsound import playsound
import requests
import speech_recognition as sr  
import subprocess
from gtts import gTTS
from translate import Translator

lang = ['en','hi']
option = input("Please select the language you prefer the bot should speak in? Type 0 for english 1 for hindi")
if option not in '0' or '1':
    option = '0'
lang_selected = lang[int(option)]

bot_message = ""
message=""

r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})

for i in r.json():
    bot_message = i['text']
    print(f"{bot_message}")

myobj = gTTS(text=bot_message,lang=lang_selected)
myobj.save("welcome.mp3")
playsound('welcome.mp3')

while bot_message != "Bye" or bot_message!='thanks':

    r = sr.Recognizer()  
    with sr.Microphone() as source:  
        print("Speak Anything :")
        audio = r.listen(source)  
        try:
            message = r.recognize_google(audio) 
            translator = Translator(to_lang='en')
            print("You said : {}".format(translator.translate(message)))

        except:
            print("Sorry could not recognize your voice") 
            myobj = gTTS(text="Sorry could not recognize your voice",lang=lang_selected)
            myobj.save("welcome.mp3")
            playsound('welcome.mp3')


    if len(message)==0:
        continue

    translator = Translator(to_lang='en')
    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": translator.translate(message)})

    print("Bot says, ",end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

    myobj = gTTS(text=bot_message,lang=lang_selected)
    myobj.save("welcome.mp3")
    playsound('welcome.mp3')