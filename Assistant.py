# -*- coding: utf-8 -*-
"""
Created on Mon May  4 12:27:55 2020
@author: Farhad
"""


import speech_recognition as sr
from time import ctime
import os
import random

import webbrowser 
import time

import playsound
from gtts import gTTS

r=sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
            
        voice_data=''
        try:
            audio =r.listen(source)
            voice_data=r.recognize_google(audio)
            #speak(voice_data)
        except sr.UnknownValueError:
            speak('Sorry sir,  I did not get this ')
        except sr.UnknownValueError:
            speak('Sorry sir,  My speech service down ')
    return voice_data;


def speak(audio_string):
    tts=gTTS(text=audio_string , lang='en', slow = False)
    r=random.randint(1, 100000000)
    audio_file='audio_'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    
    


def respond(voice_data):
    
    if 'hay zero' in voice_data:
        speak('Yes sir, what can i do for you? ' )
        
    if 'what can you do for me' in voice_data:
        speak('I can search anything you want  , i can find any location you want ,  i can say instant date and time and i am now in  building , in future i can help you many thing inshaallah  sir .' )
        
    if 'tumi kemon acho' in voice_data:
        speak('ami valo achi sir , apni kemon achen? ' )
   
    if 'what is your name' in voice_data:
        speak('My Name is Zero sir, i am your assistant . what can i do for you ?' )
        
    if 'find a girlfriend for me' in voice_data:
        speak('Sorry sir, find it yourself ' )
        
    if 'what time is it' in voice_data:
        speak(ctime())
    if 'search' in voice_data:
        search=record_audio('what do you want to search for sir ?')
        url='https://google.com/search?q='+search
        webbrowser.get().open(url)
        speak('Here is what i found for you sir - ' + search)
        
    if 'find location' in voice_data:
        location=record_audio('what location do you want sir ?')
        url='https://google.nl/maps/place/'+location+'/&amp;'
        webbrowser.get().open(url)
        speak('Here is the Location ' + location)
    
    if 'exit' in voice_data:
        print('OK sir , Exitting ')
        os._exit(0)
        

        





















time.sleep(1)

speak('I am listening sir ....   ')
while 1:
    
    voice_data=record_audio()
    respond(voice_data)