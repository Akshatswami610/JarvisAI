import re

def do_calculation(command: str) -> str:
    try:
        expression = re.sub(r"[^0-9+\-*/().]", "", command)
        result = eval(expression)
        return f"The result is {result}"
    except Exception:
        return "Sorry, I couldn't calculate that."
