import pyttsx3
import pywhatkit
import pyjokes
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning Sir!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    
    else:
        speak("Good Evening Sir!")
        
    speak("I am Friday. Please tell me how may I help you")
    speak("Adjusting for background noise...One second. I am ready.")


def takeCommand():
    """It takes microphone input from user and returns string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("recognizing...")     
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        if 'arc' in query:
            query = query.replace('arc', "")
            print(query)
        
    except Exception as e:
        #print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "none"
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
    
        """logic for executing tasks based on query"""
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'hello' in query:
            speak('Hello Sir. It is nice meeting you.')
            
        elif 'Arc' in query:
            speak("I am Arc created by Sojal Patil. I am still in development.")     
            
        elif 'open youtube' in query:
            speak(f"Opening Youtube")
            webbrowser.get("C://Program Files//Google//Chrome//Application//chrome.exe %s").open("http://youtube.com")
        
        elif 'open google' in query:
            speak(f"Opening Google")
            webbrowser.get("C://Program Files//Google//Chrome//Application//chrome.exe %s").open("http://google.com")
        
        elif 'open stackoverflow' in query:
            speak(f"One Second")
            webbrowser.get("C://Program Files//Google//Chrome//Application//chrome.exe %s").open("http://stackoverflow.com")
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I %M %p")
            speak(f"Sir, the currrent time is" +strTime)
            
        elif 'spotify' in query:
            speak(f"Opening Spotify")
            spath = "C:\\Users\\Sojal\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spath)
            
        elif 'game' in query:
            speak(f"Opening Epic Games")
            egames = "D:\\Program Files (x86)\\Epic Games\\Launcher\\Engine\\Binaries\\Win64\\EpicGamesLauncher.exe"
            os.startfile(egames)
            
        elif 'open code' in query:
            speak(f"Opening vs code")
            vcode = "C:\\Users\\Sojal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vcode)
        
        elif 'open mail' in query:
            speak(f"opening mail")
            mail = webbrowser.get("C://Program Files//Google//Chrome//Application//chrome.exe %s").open("gmail.com")
            os.startfile(mail)
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        elif 'are you single' in query:
            speak(f"I am in relationship with WiFi")
            
        elif 'play' in query:
            song = query.replace('play',"")
            speak("playing" + song)
            pywhatkit.playonyt(song)
                
        elif 'send a message on whatsapp' in query:
            pywhatkit.sendwhatmsg("+91 9890490350", 
                                "Hi from Jarvis",
                                13, 18)
            speak("Message sent succesfull")
            print("Sent succesfully")  
            
        elif 'search' in query:
            query = query.replace("search","")
            result = pywhatkit.search('search',"")
            print("Searching...")
        
        elif 'brief info' in query:
            speak('Searching google...')
            print(f"Searching...")
            query = query.replace("brief info","")
            result = pywhatkit.info(query, lines=4)
            speak(f"Do you want me to speak it for you?")
            land=takeCommand()
            if 'yes' in land:
                speak(result)
                print(result)      
        
        elif 'good night' in query:
            speak("Good Night!")
            
        elif 'stop the program' in query:
            speak("Tum jaa rhe ho. Bye bye")
            sys.exit()