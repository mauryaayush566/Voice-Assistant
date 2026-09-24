# Voice assistant
# pip install SpeechRecognition pyttsx3 pyaudio

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()
engine.setProperty("rate", 170)


def speak(text):
    # prints the text and also says it out loud
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand. Please say that again.")
        return ""
    except sr.RequestError:
        speak("Cannot reach the speech service. Check your internet.")
        return ""


def search_web(command):
    # "search python tutorials" -> topic = "python tutorials"
    topic = command.replace("search", "").replace("for", "").strip()

    # if the user didn't say a topic, ask for one
    while topic == "":
        speak("What do you want me to search?")
        topic = listen()

    speak("Searching for " + topic)
    webbrowser.open("https://www.google.com/search?q=" + topic.replace(" ", "+"))


speak("Hi, I am your voice assistant. Say hello to start.")

while True:
    command = listen()

    # nothing understood, listen again
    if command == "":
        continue

    if "hello" in command:
        speak("Hello! Nice to meet you. How can I help you today?")

    elif "time" in command:
        now = datetime.datetime.now()
        speak("The time is " + now.strftime("%I:%M %p"))

    elif "date" in command or "day" in command:
        today = datetime.datetime.now()
        speak("Today is " + today.strftime("%A, %d %B %Y"))

    elif "search" in command:
        search_web(command)

    elif "exit" in command or "stop" in command or "bye" in command:
        speak("Goodbye, have a nice day!")
        break

    else:
        speak("I can't do that yet. Try hello, time, date or search.")