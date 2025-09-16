import pyjokes
from Core.speaker import speak

def tell_joke():
    speak(pyjokes.get_joke())