import webbrowser

def search_web(command):
    if "search" in command:
        query=command.replace("search","").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return 'Sure !!'
