import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio





engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)                                 system voice
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon! Sir")
    else:
        speak("Good night! Sir")
    speak("I am a jarvis . please tell me how may I help you ")

def takeCommand():
    ''' it takes micrpphone input from the user and string input'''

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")

    except Exception as e:
            # print(e)              if recogize google are not clear the audio then the error are show (e)
        print("say that again  please...")
        return "None"
    return query


def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mukeshagur199931@gmail.com','8447070601')
    server.sendmail('mukeshgaur199931@gmail.com',to,content)
    server.close()

#
if __name__ == '__main__':
    # speak("hey mukesh you are so good boy and  ")
    wishMe()
    # while( True):
    if 1:
        query=takeCommand().lower()

    #logic for executing task ased on query
        if "wikipedia" in query:
            speak("searching wikipedia ......")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir='D:\\MUKESH\\mx songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "the time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(strtime)

        elif 'open code'  in query:
            codepath="C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
            os.startfile(codepath)

        elif 'email to mukesh' in query:
            try:
                speak("what should i say?")
                content= takeCommand()
                to='mukrsh199894@gmail.com'
                sendEmail(to,content)
                speak("email has een sent")

            except Exception as e :
                print(e)
                speak("sorry .I am not ale to send this email ")
