import webbrowser
from Core.speaker import speak
def play_music():
    speak("Playing music on spotify")
    webbrowser.open("https://spotify.com")