import pyttsx3
import datetime

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
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak('Tanggal Hari ini')
    speak(day)
    speak(month)
    speak(year)


# Fungsi untuk Menyambut saya/ucapan selamat datang kembali
def wishme():
    speak('Hallo paduka maharaja raja dari segala raja di dunia')
    time()
    date()
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

# AI Akan berbicara waktu sekarang
# time()


# AI Akan berbicara tanggal sekarang
# date()

wishme()
# Menggunakan fungsi speak
# speak('Perkenalkan nama saya Udin, saya akan memberitahu kamu sesuatu. Kamu Tamvan')
