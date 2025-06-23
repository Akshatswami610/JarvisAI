from Core.speaker import speak
from Core.listener import listen
from Core.processor import process

def main():
    speak("Hello I am jarvis, How can I help you!!!")
    while True:
        command=listen()
        if command:
            process(command)
if __name__ == "__main__":
    main()
