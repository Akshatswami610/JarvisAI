NOTES_FILE = "notes.txt"

def handle_notes(command: str) -> str:
    if "take" in command or "add" in command:
        note = command.replace("note", "").replace("take", "").replace("add", "").strip()
        with open(NOTES_FILE, "a") as f:
            f.write(note + "\n")
        return f"Note added: {note}"
    elif "show" in command:
        try:
            with open(NOTES_FILE, "r") as f:
                return "Your notes:\n" + f.read()
        except FileNotFoundError:
            return "You have no notes yet."
    else:
        return "I didn’t understand the note command."
