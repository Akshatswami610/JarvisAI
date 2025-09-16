import os
from Core.speaker import speak

def open_app(app_name):
    try:
        app_name = app_name.lower().strip()

        # Special handling for Camera, system apps, and other common apps
        special_apps = {
            "camera": "start microsoft.windows.camera:",
            "settings": "start ms-settings:",
            "calculator": "calc",
            "notepad": "notepad",
            "paint": "mspaint",
            "wordpad": "write",
            "cmd": "cmd",
            "clock": "clock",
            "powershell": "start powershell",
            "task manager": "taskmgr",
            "explorer": "explorer",
            "control panel": "control",
            "microsoft edge": "start msedge",
            "chrome": "start chrome",
            "firefox": "start firefox",
            "vlc": "start vlc",
            "word": "start winword",
            "excel": "start excel",
            "powerpoint": "start powerpnt",
            "onenote": "start onenote",
            "outlook": "start outlook",
            "teams": "start teams",
            "zoom": "start zoom",
            "spotify": "start spotify",
            "skype": "start skype",
            "discord": "start discord",
            "notion": "start notion",
            "edge": "start msedge",
            "sticky notes": "stikynot",
        }

        if app_name in special_apps:
            os.system(special_apps[app_name])
            speak(f"Opening {app_name}")
        else:
            # Try normal open
            os.system(f"start {app_name}")
            speak(f"Opening {app_name}")

    except Exception as e:
        speak(f"I couldn't open {app_name}. Error: {str(e)}")
