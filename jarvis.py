import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from random import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour < 12):
        speak("Good Morning Sir!")
    elif(hour >= 12 and hour <= 18):
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    speak("My name is Jarvis, I am your virtual assistant, Tell me how can I help you ?")

def takeCommand(): #For microphone Input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis is Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language= 'en-in')
            print(f"Milind: {query}\n")
        
        except Exception as e:
            if(str(e).startswith("recognition connection failed")):
                speak("Please Check Your Internet Connection")
            else:
                print(e)
                speak("Some Error Occured, Say that Again Please")
            return "None"

    return query

def wikipediaSearch(query):
    speak("Searching in Wikipedia")
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query, sentences= 3)
    speak(f"According to Wikipedia, {results}")

def openYoutube():
    webbrowser.open("youtube.com")

def openGoogle():
        webbrowser.open("google.com")

def openGithub():
        webbrowser.open("github.com")

def openStackOverFlow():
        webbrowser.open("stackoverflow.com")

def playMusic():
    music_dir = "D:\\7th Aug\\Softwares to be reinstall\\Music\\Martin Garrix"
    songs = os.listdir(music_dir)
    # print(songs)
    os.startfile(os.path.join(music_dir, songs[int(random()*len(songs))]))

def tellTime():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time right now is {datetime.datetime.now()}")

def openVScode():
    path = "C:\\Users\\techy\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(path)


if __name__ == "__main__":
    # wishMe()   
    while(True):
        query = takeCommand()

        #Logic for exexuting 
        if ( "wikipedia" in (query.lower())):
            wikipediaSearch(query)

        elif("open" in (query.lower())):

            if("youtube" in (query.lower())):
                openYoutube()

            elif("google" in (query.lower())):
                openGoogle()

            elif("stack over flow" in (query.lower())):
                openStackOverFlow()

            elif("git hub" in (query.lower())):
                openGithub()

        elif ("play music" in query.lower()):
            playMusic()

        elif("time" in query.lower()):
            tellTime()

        elif("open visual studio" in query.lower()):
            openVScode()

        if(input() == "a"):
            break