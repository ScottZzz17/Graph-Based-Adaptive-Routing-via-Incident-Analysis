# radio_listener.py
import speech_recognition as sr

def listen_to_radio(audio_file="local_radio.wav"):
    """
    Simulate listening to local radio by reading an audio file.
    Returns the captured audio data.
    """
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    return audio