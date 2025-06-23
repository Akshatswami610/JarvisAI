import os
from  Core.speaker import speak
def open_app(command):
    if "notepad" in command:
        os.system("notepad")
    elif "calculator" in command:
        os.system("calc")
    elif "command prompt" in command:
        os.system("cmd")
    elif "chrome" in command:
        os.system("start chrome")
    else:
        speak("I am unable to perform this action")