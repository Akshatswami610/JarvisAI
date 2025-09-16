import datetime
from Plugins import (
    jokes,
    music_player,
    app_launcher,
    weather,
    web_search,
    system_control,
    note,
    calculator,
    news,
    wiki,
)

def process_command(command: str) -> str:
    """
    Process a Jarvis command and return a text response.
    Works for both Flask (web) and CLI.
    """
    if not command:
        return "I didn’t catch that. Please try again."

    command = command.lower()

    # Basic greetings
    if "hello" in command:
        return "Hello! How can I help you today?"

    elif "time" in command:
        return f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}"

    elif "date" in command:
        return f"Today's date is {datetime.datetime.now().strftime('%A, %B %d, %Y')}"

    elif "your name" in command:
        return "I am Jarvis, your AI assistant."

    # Plugins
    elif "joke" in command:
        return jokes.tell_joke()

    elif "weather" in command:
        return weather.get_weather("your_city")


    elif "open" in command:

        # Remove the word "open" from the command

        app_name = command.replace("open", "").strip()

        if app_name:  # make sure something is left

            return app_launcher.open_app(app_name)

        else:

            speak("Please tell me which app to open.")

    elif "search" in command:
        return web_search.search_web(command)

    elif "play" in command:
        return music_player.play_music()

    elif "stop" in command:
        return "Stopping now. Goodbye!"

    # New features
    elif "shutdown" in command or "restart" in command or "lock" in command:
        return system_control.handle_system(command)

    elif "note" in command:
        return notes.handle_notes(command)

    elif "calculate" in command or "convert" in command:
        return calculator.do_calculation(command)

    elif "news" in command:
        return news.get_news()

    elif "who is" in command or "what is" in command or "wikipedia" in command:
        return wiki.lookup(command)

    else:
        return f"You said: {command}. I'm still learning how to handle that."
