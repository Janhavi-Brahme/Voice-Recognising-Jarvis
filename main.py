import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recoginizer = sr.Recognizer
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("http://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    #elif "news" in c.lower():
    #else :
        # let OpenAI handle the request


if __name__ == "__main__":
    speak("Initializing jarvis....")
    while True:
        # listen for the wake word "jarvis"
        #obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout = 2, phrase_time_limit = 1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))