from playsound import playsound as playsound
import eel

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