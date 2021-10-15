import pyttsx3
import datetime
import speech_recognition
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning")

    elif 12 <= hour <= 18:
        speak("Good Afternoon")

    else:
        speak("Good evening")

    speak("I am Jarvis! manthan, How may I help you?")


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


list = [
    "https://music.youtube.com/watch?v=iznXe9d79jw&list=MLCT",
    "https://music.youtube.com/watch?v=SKm_GN2LaXU&list=MLCT",
    "https://music.youtube.com/watch?v=aDkEJ-DdA0w&list=MLCT",
    "https://music.youtube.com/watch?v=8m77vBdtnAs&list=MLCT",
    "https://music.youtube.com/watch?v=fNWK3HlD0-A&list=MLCT",
    "https://music.youtube.com/watch?v=Y9Qpya1AlXM&list=MLCT",
    "https://music.youtube.com/watch?v=xOxNrZBTuP4&list=MLCT",
    "https://music.youtube.com/watch?v=VPPKfQ3adc4&list=MLCT",
    "https://music.youtube.com/watch?v=4eHABt5SIgc&list=MLCT",
    "https://music.youtube.com/watch?v=VmkNFegq7VI&list=MLCT",
    "https://music.youtube.com/watch?v=o-yueRd-k0c&list=MLCT",
    "https://music.youtube.com/watch?v=R4hDcd9fzRk&list=MLCT",
    "https://music.youtube.com/watch?v=6PL39H2B7UQ&list=MLCT",
    "https://music.youtube.com/watch?v=xBqpEpMGZe8&list=MLCT",
]

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for excecuting tasks based on query
        if "what is" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=100)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "who is" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=100)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open my website" in query:
            webbrowser.open("techfornerdz.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open whatsapp" in query:
            webbrowser.open("web.whatsapp.com")
        elif "play naruto music" in query:
            webbrowser.open(
                "https://music.youtube.com/watch?v=X4fIqbUjEEI&list=RDAMVMX4fIqbUjEEI"
            )
        elif "play hindi music" in query:
            webbrowser.open(
                "https://music.youtube.com/watch?v=NeXbmEnpSz0&list=RDAMVMNeXbmEnpSz0"
            )
        elif "play music" in query:
            x = random.randint(0, 13)
            webbrowser.open(list[x])

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir ji time is {strTime}")

        elif "open chrome" in query:
            filesPath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(filesPath)

        elif "who are you" in query:
            speak("I am JARVIS! your e-friend; Or you can say... your robo-friend.")

        elif "quit" in query:
            speak("Bye Bye manthan, have a nice day!")
