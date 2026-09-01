import webbrowser

from playsound import playsound as playsound
import eel
from engine.command import *
from engine.config import ASSISTANT_NAME 
import os
import pywhatkit as kit
import re
from engine.db import *

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
    query = query.replace("open", "").strip().lower()


    if query != "":
        try:
            # Tries to find the application is sys_command table
            cursor.execute('SELECT path FROM sys_command WHERE LOWER(name) = ?', (query,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening " + query)
                os.startfile(results[0][0])
                return

            # If not found, try to find the command in the web_command table
            cursor.execute('SELECT url FROM web_command WHERE LOWER(name) = ?', (query,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening " + query)
                webbrowser.open(results[0][0])
                return

            # This is for if still the path is not found in the database we use the os mode
            speak("Opening " + query)
            try:
                os.system('start ' + query)
            except Exception as e:
                speak(f"Unable to open {query}. Error: {str(e)}")

        except Exception as e:
            speak(f"Something went wrong: {str(e)}")

# WILL CHANGE THE OS MODULE SINCE ITS DEPRACETED

# Adding function to play a Youtube video

def PlayYoutube(query) :
    search_term = extract_yt_term(query)
    if search_term:
        speak(f"Playing {search_term} on YouTube")
        kit.playonyt(search_term)

    else:
        speak("Sorry, I couldn't find what to play on YouTube")

def extract_yt_term(command):
    pattern = r'play\$+(.*?)\$+on\$+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None
# This functon extracts the dynamic term from a youtube query 