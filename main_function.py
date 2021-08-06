import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import random

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


# Jika anda ingin membuat fungsi time untuk dibacakan oleh AI
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak('Waktu Saat Ini')
    speak(Time)


# Membuat fungsi agar AI membacakan Tanggal sekarang
def date():
    now = datetime.datetime.now()
    tanggal = now.strftime("%d-%B-%Y")
    speak('Tanggal Hari ini')
    speak(tanggal)

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
        return "None"

    return query


def screenshot():
    img = pyautogui.screenshot()
    img.save('ss.png')


def cpu():
    usage = str(psutil.cpu_percent())
    speak("Penggunaan CPU" + usage)

    batery = psutil.sensors_battery()
    speak("Batre tersisa ")
    speak(batery.percent)


if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "jam" in query:
            time()
        elif "kabar" in query:
            speak('Bacot lu, gausah banyak tanya anjing, langsung aja mau apa?')
        elif "tanggal" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak('Mencari...')
            query = query.replace('wikipedia', "")
            # setting language to indo
            wikipedia.set_lang("id")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        elif "logout" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "musik" in query:
            songs_dir = "C:\\Users\\Renol N\\Downloads\\Music"
            songs = os.listdir(songs_dir)
            shuffle = random.randint(1, 100)
            print(shuffle)
            os.startfile(os.path.join(songs_dir, songs[shuffle]))
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
        elif "screenshot" in query:
            screenshot()
            speak("Screenshot berhasil di simpan")
        elif "kondisi laptop" in query:
            cpu()
