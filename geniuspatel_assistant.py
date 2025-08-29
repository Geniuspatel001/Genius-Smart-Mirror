# geniuspatel_assistant.py

import pyttsx3
import speech_recognition as sr
import webbrowser
import cv2
import os

def initialize_tts():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Female voice
    engine.setProperty('rate', 150)  # Speed
    engine.say("Hello, I am your Genius Smart Mirror assistant.")
    engine.runAndWait()
    return engine

engine = initialize_tts()

def speak(text):
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("I am listening now.")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

def process_command(command):
    command = command.lower()

    if "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "camera" in command:
        speak("Opening camera")
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    elif "weather" in command or "temperature" in command:
        speak("Fetching weather details")
        webbrowser.open("https://www.google.com/search?q=current+weather")

    elif "location" in command:
        speak("Showing your location")
        webbrowser.open("https://www.google.com/maps")

    elif "music" in command:
        speak("Playing music")
        os.system("start wmplayer")

    elif "exit" in command or "stop" in command:
        speak("Goodbye Genius!")
        exit()

    else:
        speak("Sorry, I didn’t catch that command.")

# Main driver loop
if __name__ == "__main__":
    while True:
        user_command = listen()
        if user_command:
            process_command(user_command)