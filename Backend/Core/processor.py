from Plugins import time_date, weather, app_launcher, web_search, jokes, music_player

def process(command):
    if "time" in command:
        time_date.tell_time()
    elif "weather" in command:
        weather.get_weather("your_city")
    elif "open" in command:
        app_launcher.open_app(command)
    elif "search" in command:
        web_search.search_web(command)
    elif "joke" in command:
        jokes.tell_joke()
    elif "music" in command:
        music_player.play_music()
    elif "stop" in command:
        return
    else:
        from Core.speaker import speak
        speak("Sorry, I didn't understand that")