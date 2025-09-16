import os

def handle_system(command: str) -> str:
    if "shutdown" in command:
        os.system("shutdown /s /t 1")
        return "Shutting down the computer."
    elif "restart" in command:
        os.system("shutdown /r /t 1")
        return "Restarting the computer."
    elif "lock" in command:
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return "Locking the computer."
    else:
        return "System command not recognized."
