import gtts
import speech_recognition as sr
from pydub import AudioSegment


def text_to_speech(message):
    tts = gtts.gTTS(message, lang="ru")
    tts.save("text_to_speech.mp3")


def ogg2wav(message):
    wav = message.replace(".ogg", ".wav")
    segment = AudioSegment.from_file(message)
    segment.export(wav, format="wav")


def speech_to_text():
    ogg2wav("voice.ogg")
    r = sr.Recognizer()
    with sr.AudioFile("voice.wav") as source:
        audio = r.record(source)
        text = r.recognize_google(audio_data=audio, language="ru-RU")
        return text
