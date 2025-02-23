# speech_to_text.py
import speech_recognition as sr

def transcribe_audio(audio):
    """
    Transcribe audio data into text using Google's Speech Recognition API.
    """
    r = sr.Recognizer()
    try:
        transcript = r.recognize_google(audio)
        return transcript
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""