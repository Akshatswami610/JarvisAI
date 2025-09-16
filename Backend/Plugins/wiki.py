import wikipedia

def lookup(command: str) -> str:
    try:
        topic = command.replace("who is", "").replace("what is", "").replace("wikipedia", "").strip()
        summary = wikipedia.summary(topic, sentences=2)
        return summary
    except Exception:
        return "Sorry, I couldn't find that on Wikipedia."
