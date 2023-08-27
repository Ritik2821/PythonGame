import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour< 18:
        speak("Good AfterNoon!")
    
    else:
        speak("Good Evening!")
    
    speak("I am Ram, How may I help you Ritik Sir?")

def takeCommand():
    # it takes microphone input from the user ans return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('ritik1488@gmail.com','wrongpassword')
    server.sendmail('ritik1488@gmail.com',to,content)
    server.close()
if __name__=="__main__":
   wishMe()
   while True:
       query=takeCommand().lower()
#logic for executing task based on query
       if 'wikipedia' in query:
           speak('Searching Wikipedia...')
           query= query.replace("wikipedia","")
           results=wikipedia.summary(query,sentences=2)
           speak("According to Wikipedia")
           print(results)
           speak(results)

       elif 'open google' in query:
           webbrowser.open("google.com")
       elif 'open youtube' in query:
           webbrowser.open("youtube.com")
       elif 'the time'in query:
           strTime=datetime.datetime.now().strftime("%H:%M:%S")  
           speak(f"Sir, the time is {strTime}")
           print(strTime)
       elif 'open code' in query:
           codePath="D:\\small projects\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)
       elif 'open blender' in query:
           codePath="C:\\Program Files\\Blender Foundation\\Blender 2.90\\blender.exe"
           os.startfile(codePath)
       elif 'email to hrithik' in query:
           try:
               speak("What should I say?")
               content=takeCommand()
               to="ritik1488@gmail.com"
               sendEmail(to,content)
               speak("Email has been sent!")
           except Exception as e:
                print(e)
                speak("Sorry Sir.I am not able to send this mail")




        

           


   
   

 
       
   
    