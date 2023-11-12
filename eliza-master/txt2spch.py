import pyttsx3

engine = pyttsx3.init()

def spch2txt(str):
    engine.say(str)
    engine.runAndWait()
