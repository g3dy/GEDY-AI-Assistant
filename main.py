import os
import eel
import webbrowser
from engine.features import *
from engine.command import *

# Playing countdown
playCountDownSound()

# function to specify where our frontend files are located
eel.init('www/assets')

# now opeining project in desktop app mode
webbrowser.open("http://localhost:8000/index.html")
eel.start('index.html', mode='chrome', host='localhost', block=True)
