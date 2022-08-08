import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
from sys import platform
import os
import sys
import smtplib
import pywhatkit
import psutil

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        print("Good Afternoon!")   
        speak("Good Afternoon!")   
    
    else:
        print("Good Evening!")  
        speak("Good Evening!")  

    print("I am Jarvis Sir. Please tell me how may I help you?")       
    speak("I am Jarvis Sir. Please tell me how may I help you?")       


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.energy_threshold = 450
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        speak("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('manas.gupta.2014@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    
    
    if platform == "linux" or platform == "linux2":
        chrome_path = "/usr/bin/google-chrome"

    elif platform == "darwin":
        chrome_path = "open -a /Applications/Google\ Chrome.app"

    elif platform == "win32":
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    else:
        print('Unsupported OS')
        exit(1)

    webbrowser.register(
        'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'hello' in query:
            speak("Hello Sir, How can I help You?")
        
        elif 'how are you' in query:
            speak("I am fine sir,what about you.")
            

        elif 'cpu' in query:
            cpu()

        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[1].id)
                speak("Hello Sir,I am Friday ,I have switched my voice. How is it?")
            else:
                engine.setProperty('voice', voices[0].id)
                speak("Hello Sir,I am JARVIS,I have switched my voice. How is it?")
        
        elif 'notepad' in query:
            npath="C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)


        elif 'song on youtube' in query:
            pywhatkit.playonyt(takeCommand())

        elif 'open whatsapp' in query:
            webbrowser.get('chrome').open('https://www.web.whatsapp.com')

        elif 'open youtube' in query:
            webbrowser.get('chrome').open('https://www.youtube.com')

        elif 'open google' in query:
            speak("Sir what should i search on Google")
            gcm=takeCommand().lower()
            webbrowser.open_new(f"{gcm}")

        elif 'open stack overflow' in query:
            webbrowser.get('chrome').open('https://www.stackoverflow.com')   

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Manas Gupta\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\\PYTHON\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'no thanks' in query:
            speak("Thanks for using me Sir, Have a Great day!")
            sys.exit()

        elif 'email to Manas' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "your@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, Not able to send email at the moment")    
        else:
            speak("Sorry sir, I cant do that")
    
        speak("Sir! Do you have any other work")