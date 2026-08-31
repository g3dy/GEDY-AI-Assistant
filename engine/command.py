import pyttsx3
import speech_recognition as sr
import eel

def speak(text) :
    engine = pyttsx3.init()

    engine.setProperty('rate', 170)
    engine.say(text)

    engine.runAndWait()

@eel.expose
def takeCommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1 #This 1 means if you pause for more than 1s, the recognizer will take it as you're done speaking
        r.adjust_for_ambient_noise(source) #it listens to surrounding noise and adjust the recognizer accordingly
        audio = r.listen(source, timeout=10, phrase_time_limit=6) 
        # the timeout means that the listening will stop after 10s if there is no speech
        # whereas phrase_time_limit=6 means each phrase should be no longer than 6s

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = sr.recognize_google(audio, lan="en")
        print(f"User said: {query}")
        speak(query)
        eel.DisplayMessage(query)
        eel.ShowHood()

    except Exception as e:
        return ""

    return query.lower()

# DEMO
# text = takeCommand()

# speak(text)