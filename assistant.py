import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
from urllib.parse import quote


# Text-to-Speech
engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            print("Recognizing...")

            # English only
            command = recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            print("You:", command)

            return command.lower()

        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I could not understand you.")
            return ""

        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
            return ""


def google_search(query):

    query = quote(query)

    url = (
        "https://www.google.com/search?q="
        + query
    )

    speak("Searching Google.")

    webbrowser.open(url)


def youtube_search(query):

    query = quote(query)

    url = (
        "https://www.youtube.com/results?search_query="
        + query
    )

    speak("Searching YouTube.")

    webbrowser.open(url)


def run_assistant():

    speak(
        "Hello! I am your voice assistant. "
        "How can I help you?"
    )

    while True:

        command = listen()

        if command == "":
            continue

        # TIME
        if "time" in command:

            current_time = datetime.datetime.now().strftime(
                "%I:%M %p"
            )

            speak(
                "The current time is "
                + current_time
            )

        # DATE
        elif "date" in command:

            current_date = datetime.datetime.now().strftime(
                "%d %B %Y"
            )

            speak(
                "Today's date is "
                + current_date
            )

        # OPEN GOOGLE
        elif "open google" in command:

            speak("Opening Google.")

            webbrowser.open(
                "https://www.google.com"
            )

        # OPEN YOUTUBE
        elif "open youtube" in command:

            speak("Opening YouTube.")

            webbrowser.open(
                "https://www.youtube.com"
            )

        # YOUTUBE SEARCH
        elif "youtube" in command:

            query = command

            query = query.replace(
                "youtube", ""
            )

            query = query.replace(
                "search", ""
            )

            query = query.replace(
                "on", ""
            )

            query = query.replace(
                "for", ""
            )

            query = query.strip()

            if query:

                youtube_search(query)

            else:

                speak(
                    "What should I search for on YouTube?"
                )

        # GOOGLE SEARCH
        elif "search" in command:

            query = command

            query = query.replace(
                "search", ""
            )

            query = query.replace(
                "google", ""
            )

            query = query.replace(
                "for", ""
            )

            query = query.strip()

            if query:

                google_search(query)

            else:

                speak(
                    "What should I search for?"
                )

        # EXIT
        elif (
            "exit" in command
            or "quit" in command
            or "stop" in command
            or "goodbye" in command
        ):

            speak(
                "Goodbye! Have a nice day."
            )

            break

        # UNKNOWN COMMAND
        else:

            speak(
                "Sorry, I don't know that command yet."
            )


if __name__ == "__main__":
    run_assistant()