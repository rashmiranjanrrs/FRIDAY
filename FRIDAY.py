#A Speech recognition Python Script
#Starting Date: 02/08/2019
#Still on developing phase
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
app_id = "XYY47G-2WGGEEYUT4"
client = wolframalpha.Client(app_id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening! Sir")

    speak("Friday is waiting for your command")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query1 = r.recognize_google(audio, language='en-in')
        print(f"User said: {query1}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query1

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:

    # if 1:
        query1 = takeCommand().lower()



        if 'wikipedia' in query1:
            speak('Searching Wikipedia...')
            query1 = query1.replace("wikipedia", "")
            results = wikipedia.summary(query1, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query1:
            webbrowser.open("youtube.com")

        elif 'open google' in query1:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query1:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query1:
            music_dir = 'C:\\Users\\LENOVO\\Music\\New'
            songs = os.listdir(music_dir)
            track = random.randint(1,100)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[track]))

        elif 'the time' in query1:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query1:
            codePath = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to rrs' in query1:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rrsyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend ranjan bhai. I am not able to send this email")

        elif 'whom i love' in query1:
            speak("Rashmi Ranjan Sahoo loves his father and mother more than anything in the world")

        elif 'what is my name' in query1:
            speak("your name is Rashmi Ranjan Sahoo")

        elif 'what is the' in query1:
            res = client.query(query1)
            answer = next(res.results).text
            print(answer)
            speak(answer)

        elif 'where is' in query1:
            res = client.query(query1)
            answer = next(res.results).text
            print(answer)
            speak(answer)

        elif 'what is the fullform of friday' in query1:
            print("Fullform of FRIDAY is Female Replacement Intelligent Digital Assistant Youth")
            speak("Fullform of FRIDAY is Female Replacement Intelligent Digital Assistant Youth")
