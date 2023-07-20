from pydub import AudioSegment
from pydub.playback import play
import os

initaudio = AudioSegment.from_file(r"libs\\audio\\jarvis_engage.mp3", format="mp3")
overaudio = AudioSegment.from_file(r"libs\\audio\\jarvis-disengage.mp3", format="mp3")

def speak(speech_rate=200, volume=1.0, speak_sentence=None):
    os.system(f'.\\virtvenv\\Scripts\\edge-tts.exe --text "{speak_sentence}" --write-media out.mp3')
    outputtts = AudioSegment.from_file("out.mp3", format="mp3")
    play(initaudio)
    play(outputtts)
    play(overaudio)
