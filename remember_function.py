import pyttsx3
import datetime
import speech_recognition as sr
# Untuk Menggunakan Bahasa Indonesia agar ejaan nya benar setting dulu Microsoft Andika nya di regedit

engine = pyttsx3.init()
# Untuk mengganti Voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Voice Rate = Kecepatan Suara atau Ejaan
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)


# Speak Function, masukan kata untuk membuat engine berbicara dari text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Fungsi untuk Menyambut saya/ucapan selamat datang kembali


def wishme():
    speak('Hallo paduka maharaja raja dari segala raja di dunia')
    # Membuat ucapan selamat dengan if
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak('Selamat Pagi')
    elif hour >= 12 and hour < 18:
        speak('Selamat Siang')
    elif hour >= 18 and hour <= 24:
        speak('Selamat Malam')
    else:
        speak('Selamat Petang')
    speak('Ada yang bisa saya bantu?')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Mendengarkan...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language="id-ID")
    except Exception as e:
        print(e)
        speak('Ulangi...')
        return "None"

    return query


if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand().lower()
        print('Perintah : ', query)

        if "offline" in query:
            quit()
        elif "ingat" in query:
            speak('Apa yang harus saya ingat?')
            data = takeCommand()
            speak("Anda bilang saya harus mengingat" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "tahu sesuatu" in query:
            remember = open("data.txt", "r")
            speak("Anda menyuruh saya untuk mengingat" + remember.read())
        else:
            print('Perintah tidak diketahui, ulangi..')