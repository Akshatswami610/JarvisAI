from datetime import datetime
from Core.speaker import speak
def tell_time():
    now=datetime.now().strftime("%H:%M")
    speak(f"Current time is {now}")
