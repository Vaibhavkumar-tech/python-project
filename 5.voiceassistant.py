# This is a simple voice assistant program 
# Peter can perform various tasks such as telling the time, playing music, opening websites, and generating QR codes.

import pyttsx3  # Text to Speech
import speech_recognition as sr   # Speech Recognition
import datetime as dt
import pyjokes
import webbrowser
import os
import qrcode as qr
import time   # for time delay

def srtext():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio=r.listen(source)   #audio varaible mei store krwa liya
        try:
            print("Recognizing...")
            data=r.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("nothing recognized")
def speechtxt(x):
    e=pyttsx3.init()
    voices=e.getProperty('voices')
    e.setProperty('voice',voices[1].id)
    rate=e.getProperty('rate')
    e.setProperty('rate',150)
    e.say(x)
    e.runAndWait()
speechtxt("Hello, I am peter. How can I help you?")
if __name__=="__main__":       #split the code into functions
       
            while True:
                data1=srtext()
                if data1:
                    data1=data1.lower()
                else:
                    print("Sorry, I didn't catch that.")
                    continue
                if "your name" in data1:
                    name="My name is peter"
                    speechtxt(name)
                elif "your branch" in data1:
                    branch="Electronics and Communication Engineering"
                    speechtxt(branch)
                elif "current time" in data1:
                    time=dt.datetime.now().strftime("%I%M%p")    #strf for searching the time
                    speechtxt(time)   
                    print(time)
                elif "play music" in data1:
                    str="opening your song"
                    speechtxt(str)
                    webbrowser.open("https://www.youtube.com/watch?v=vsWxs1tuwDk")
                elif "youtube" in data1:
                    mtr="I am peter,opening youtube"
                    speechtxt(mtr)
                    webbrowser.open("https://www.youtube.com/")
                elif "open google" in data1:
                    n="opening google"
                    speechtxt(n)
                    webbrowser.open("https://www.google.com/")
                elif "open gmail" in data1:
                    m="opening gmail"
                    speechtxt(m)
                    webbrowser.open("https://mail.google.com/")
                
                elif "joke" in data1:
                    joke=pyjokes.get_joke(language="en", category="neutral")
                    print(joke)
                    speechtxt(joke)
                elif "laptop music" in data1:
                    addressplaylist=(input("Enter the address of your playlist:"))
                    listsongs=os.listdir(addressplaylist)
                    print(listsongs)
                    speechtxt("playing your laptop song")
                    os.startfile(os.path.join(addressplaylist,listsongs[0]))
              
                elif "Generate QR" in data1:
                    link=input("Enter the link you want to generate qr code:")
                    image=qr.make(link)
                    speechtxt("Say Name for Saving the file")
                    name=srtext()
                    image.save("name.png")

                elif "else" in data1:
                    speechtxt("thank you")
                    break
                time.sleep(10)
            
            
             
    