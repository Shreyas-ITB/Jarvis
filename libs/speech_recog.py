import os
import speech_recognition as sr
from dotenv import load_dotenv
import os
from platform import system

load_dotenv(r".env")
r = sr.Recognizer()
speechrate = os.getenv("SPEECH_RATE")
volume = os.getenv("VOLUME")
# if system == "win32" or system == "win64" or system == "windows":
#     audiopath = f"libs\{mp3_file}"
# elif system == "linux2" or system == "linux" or system == "darwin":
#     audiopath = f"libs/{mp3_file}"

def listen_and_transcribe():
    # Initialize the speech recognizer
    r = sr.Recognizer()

    # Start listening to the user's voice
    print("Listening...")
    with sr.Microphone() as source:
        audio = r.listen(source, 0, 100)
    try:
        global query
        query = r.recognize_google(audio)
        return query
    except sr.UnknownValueError:
        print("Could not transcribe the audio.")
    except sr.RequestError as e:
        print(f"Error during speech recognition: {str(e)}")