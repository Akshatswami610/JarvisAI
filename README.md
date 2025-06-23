# Jarvis AI - Voice Assistant (Python Backend)

A modular and extensible offline-first Python voice assistant that listens to your commands and performs smart tasks — just say "Hey Jarvis" and get going.

---

Features

Basic Functions
- Tell time and date
- Launch apps (like Notepad, Chrome)
- Perform Google or YouTube searches
- Shutdown, restart, or log off the system
- Voice-based note-taking

Internet-Based Features
- Get current weather updates
- Fetch latest news headlines
- Send emails using SMTP
- Google Calendar integration (add/view reminders)
- Manage a voice-controlled to-do list
- Get crypto and stock prices
- Detect unsafe links or files

Fun and Experimental Features
- Play music using YouTube
- Tell programming jokes
- Voice quiz mode
- Translate languages
- Take photos using webcam
- Change desktop wallpaper
- Wake word detection: "Hey Jarvis" using Vosk

---

Project Structure

jarvis_ai/
├── main.py
├── core/
│ ├── listener.py
│ ├── speaker.py
│ ├── processor.py
│ ├── config.py
│ └── wakeword.py
├── plugins/
│ ├── time_date.py
│ ├── app_launcher.py
│ ├── web_search.py
│ ├── system_control.py
│ ├── notes.py
│ ├── weather.py
│ ├── news.py
│ ├── openai_chat.py
│ ├── email_sender.py
│ ├── calendar.py
│ ├── todo.py
│ ├── crypto_stocks.py
│ ├── file_checker.py
│ ├── location_info.py
│ ├── music_player.py
│ ├── jokes.py
│ ├── quiz.py
│ ├── translator.py
│ ├── camera.py
│ └── wallpaper.py
└── utils/
├── logger.py
├── helpers.py
└── api_utils.py
