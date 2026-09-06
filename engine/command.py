import time
import pyttsx3
import speech_recognition as sr
import eel
###########
import sounddevice as sd
import numpy

def speak(text) :
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    eel.DisplayMessage(text)
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
        query = sr.recognize_google(audio, language="en")
        print(f"User said: {query}")
        # speak(query)
        time.sleep(2)
        eel.DisplayMessage(query)
        

    except Exception as e:
        return ""

    return query.lower()

####################################################################

def pyaudioReplacement():
    fs = 16000
    seconds = 5
    print(f"Listening...")
    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    r = sr.Recognizer()
    audio_data = sr.AudioData(audio.tobytes(), fs, 2)

    try:
        text = r.recognize_google(audio_data)
        print(f"You said: {text}")
        speak(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        speak("Could not understand")
        return ""

####################################################################

# DEMO
# text = takeCommand()

# speak(text)

# This part is made to access all the functions. and this is where the 'commands' we give the assistant will be implemented.
@eel.expose
def allCommand() :
    query = pyaudioReplacement()
    print(query)

    # Implementing the "OPEN" command; where when the user says "OPEN".... the task will be archieved
    if "open" in query:
        # print("Success") # Testing was successful
        from engine.features import openCommand
        from engine.features import execute_voice_command
        execute_voice_command(query)
        # openCommand(query)

    elif 'on youtube' in query:
        from engine.features import PlayYoutube
        PlayYoutube(query)

    else:
        print("Ooops") #Testing the command

    eel.ShowHood()