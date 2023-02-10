from click import BaseCommand
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib 
import pyjokes
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am jarvis Sir. Please tell me how may i help you")


def takeCommand():
    # It takes microphone input from user and give string type output
    r = sr.Recognizer()
    r.pause_threshold = 1
    with sr.Microphone() as source:
        print('Your jarvis is Listening...')

        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query
 
         
                

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('arf4852@gmail.com', 'khdviiwajtshibfg')
    server.sendmail('arf4852@gmail.com', to, content)
    server.close()
    
if __name__ == '__main__':
    wishMe()
    while True:
    
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')
            
        elif 'open linkedin' in query:
            webbrowser.open('linkedin.com')
            
        elif 'open instagram' in query:
            webbrowser.open('instagram.com')
          
        elif 'shutdown my pc' in query:        
           
          speak("Do you really want to shutdown")
          reply = BaseCommand()   
          if 'yes'in reply:
              os.system('shutdown /s /t 5')
          else:
              break   
        

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\HP\\Desktop\\New folder'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"Sir, the time is {strTime}")
            
        elif 'my name' in query:
            myname= "Arif khan"
            speak(f"Sir, your name is {myname}")
            
        elif 'your name' in query:
            yourname= "Jarvis"
            speak(f"Sir, your name is {yourname}")
            
        elif 'old are you' in query:
            age = "i am two years old"
            speak(age)

        elif 'open code' in query:
            codePath = "C:\\Users\\HP\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'email to harshit' in query:
            try:
                speak('What should I say!')    
                content=takeCommand()
                to = 'harshitksingh@gmail.com'
                sendEmail(to,content)
                speak('email has been sent!')
            except Exception as e:
                print(e)    
                speak('Sorry I am unable to send this email at the moment')
                
        elif 'joke' in query:        
                joke_1 = pyjokes.get_joke(language="en", category="neutral")
                print(joke_1)
                speak(joke_1)
                
      
        elif "send message" in query:
         pywhatkit.sendwhatmsg("+917355165493", "Good afternoon", 13, 33)
                
        elif 'exit' in query:
            speak('Thank you')
            break    
