from libs.vocal import speak
from libs.speech_recog import listen_and_transcribe
from libs.webcom import webcomms
from dotenv import load_dotenv
import os, time
from random import choices


load_dotenv(r".env")
speechrate = os.getenv("SPEECH_RATE")
volume = os.getenv("VOLUME")
wakesentence = choices(["At your service sir!"])
listening_duration = int(os.getenv("LISTENING_DURATION"))

while True:
    user_input = listen_and_transcribe()
    inp = str(user_input).lower()
    print(f"You said: {user_input}")
    if inp == "jarvis" or inp == "jarvis you there" or inp == "wake up jarvis":
        speak(220, volume, speak_sentence=str(wakesentence))
        start_time = time.time()  # Start measuring elapsed time
        while time.time() - start_time < listening_duration:
            new_user_input = listen_and_transcribe()
            if new_user_input:
                print(f"You said: {new_user_input}")
                web = webcomms(new_user_input)
        print("Listening time is up. Jarvis is going back to sleep...")
    else:
        print("Jarvis is asleep...")