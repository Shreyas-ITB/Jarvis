import pyttsx3
from pydub import AudioSegment
from pydub.playback import play

initaudio = AudioSegment.from_file(r"libs\\audio\\jarvis_engage.mp3", format="mp3")
overaudio = AudioSegment.from_file(r"libs\\audio\\jarvis-disengage.mp3", format="mp3")

def speak(speech_rate=200, volume=1.0, speak_sentence=None):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Find the desired voice
    selected_voice = None
    for voice in voices:
        if "IVONA 2 Brian - British English male voice [22kHz]" in voice.name:
            selected_voice = voice
            break

    # Set the desired voice
    if selected_voice:
        engine.setProperty('voice', selected_voice.id)
        engine.setProperty('rate', speech_rate)
        engine.setProperty('volume', volume)
    else:
        print("Desired voice not found.")
        return

    # Check if surprise sentences are provided
    if not speak_sentence:
        print("No speak sentences provided.")
        return

    # Modify and express the surprise sentences
    modified_sentence = speak_sentence.upper() + "!"
    play(initaudio)
    engine.say(modified_sentence)
    engine.runAndWait()
    play(overaudio)