# JarvisAI - Python Voice Assistant (Flask + Plugins)

**JarvisAI** is a Python-powered voice assistant built using **Flask** and modular **plugin-based architecture**. It supports both text and voice commands and offers functionalities like telling jokes, checking the weather, playing music, launching apps, taking notes, performing calculations, and more!
<img width="1919" height="897" alt="image" src="https://github.com/user-attachments/assets/70c6629c-917a-475f-ada8-be14059c45eb" />

---

## 🚀 Features

- 🎙️ **Voice & Text Commands** – Use your voice or keyboard to interact
- 📅 **Date & Time Info** – Ask for current time or date
- 🤖 **Jarvis Identity** – Responds to "what is your name" etc.
- 🔌 **Modular Plugin System**:
  - 🃏 Tell jokes
  - 🎵 Play music
  - ☁️ Get weather updates
  - 🔍 Perform web searches
  - 💻 Launch installed applications
  - 🖥️ Shutdown, restart, or lock the system
  - 📝 Take and retrieve notes
  - ➗ Perform calculations and conversions
  - 📰 Fetch latest news headlines
  - 📚 Wikipedia lookups

---

## 🛠️ Installation

1. **Clone the repository**:
    ```bash
    git clone <your_repository_url>
    cd JarvisAI
    ```

2. **Create and activate virtual environment**:
    ```bash
    python -m venv jarvis_env
    # Windows
    jarvis_env\Scripts\activate
    # macOS/Linux
    source jarvis_env/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask app**:
    ```bash
    python app.py
    ```

5. **Open in browser**:
    Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧠 Usage

- 🖋️ **Text**: Type your command in the input field and press Send
- 🎤 **Voice**: Use the mic to speak your command
- ❌ **Stop**: Say or click "Stop" to exit or pause

---

## 🧪 Example Commands

| Category       | Example Commands                         |
|----------------|-------------------------------------------|
| Greeting       | `hello`, `hi`                             |
| Date/Time      | `what's the time`, `today's date`         |
| App Control    | `open chrome`, `shutdown`                 |
| Fun/Utility    | `tell me a joke`, `play music`            |
| Info Search    | `search Python`, `who is Einstein`        |
| Notes          | `take a note "Buy groceries"`             |
| Calculations   | `calculate 45 * 12`, `convert 10 kg to lb`|
| Weather/News   | `weather`, `news`                         |

---

## 📁 Project Structure
<pre>
JarvisAI/
│
├── App/
│ ├── Core/
│ │ ├── jarvis.py # Main logic for command handling
│ │ └── speaker.py # Text-to-speech / voice-related
│ ├── Plugins/
│ │ ├─ jokes.py
│ │ ├─ music_player.py
│ │ ├─ app_launcher.py
│ │ ├─ weather.py
│ │ ├─ web_search.py
│ │ ├─ system_control.py
│ │ ├─ note.py
│ │ ├─ calculator.py
│ │ ├─ news.py
│ │ └─ wiki.py
│ ├── templates/
│ │ └── index.html # Flask HTML frontend
│ └── app.py # Flask app entry point
│
├── jarvis_env/ # Python virtual environment
│
├── requirements.txt # Python dependencies
├── README.md # This file
├── .gitignore
└── .gitattributes
</pre>

---

## 🤝 Contributing

Pull requests are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a PR.

---

## 📄 License

This project is **open-source**. You are free to use, modify, and share it.
