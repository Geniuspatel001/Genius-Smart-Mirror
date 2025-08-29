import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I didn't catch that.")
        return ""

def process_command(cmd):
    if "time" in cmd:
        speak(datetime.datetime.now().strftime("%H:%M:%S"))
    elif "weather" in cmd:
        # call your weather function here
        speak("It's sunny right now.")
    elif "open youtube" in cmd:
        webbrowser.open("https://youtube.com")
    elif "open google" in cmd:
        webbrowser.open("https://google.com")
    else:
        speak("I can't do that yet.")

# Main loop
while True:
    command = listen_command()
    if command:
        process_command(command)
