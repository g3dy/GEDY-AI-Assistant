from playsound import playsound as playsound
import eel
from engine.command import *
from engine.config import ASSISTANT_NAME 
import os

# The function for playing countdown sound
def playCountDownSound() :
    sound_dir = "www\\assets\\audio\\count-down.mp3"
    playsound(sound_dir)

# Allowing function to be accessed at JS file
@eel.expose
# click sound for mic button
def micClickSound() :
    sound_dir = "www\\assets\\audio\\mic-ready.mp3"
    playsound(sound_dir)

# Now creating the actual command function

def openCommand(query) :
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query != "" :
        speak(f"Opening {query}")
        os.system('Start ' + query)

    else:
        speak(f"{query} not found")

# WILL CHANGE THE OS MODULE SINCE ITS DEPRACETED