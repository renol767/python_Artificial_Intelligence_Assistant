import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init()
# Untuk mengganti Voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Voice Rate = Kecepatan Suara atau Ejaan
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Mendengarkan...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language="id-ID")
        print(query)
    except Exception as e:
        print(e)
        speak('Ulangi...')
        return "None"

    return query


takeCommand()
