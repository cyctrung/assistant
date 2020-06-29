import speech_recognition as sr
import pyttsx3
import random
import webbrowser
from time import localtime, strftime
import os

r = sr.Recognizer()
text = None #save text 
sound = None #save sound to speech
Exit = False
query = None
engine = pyttsx3.init()  
engine.setProperty('rate', 125)     
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)


count_exit = 0 
with sr.Microphone() as source:
    engine.say("Hello everyone!")
    engine.runAndWait() 
    while True:
        audio = r.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
        print("Robot listening...")
        try:
            audio=r.listen(source, timeout=10) #now when we listen, the energy threshold is already set to a good value, and we can reliably catch speech right away
        except:
            audio =""
    
        try:    
            text = r.recognize_google(audio,language='en-EN')
        except:
            text = ""
        print("You: "+text)
        if ("hello" in text or "hi" in text or "hey" in text ):
            sound = random.choice(("I'm here","Hello","Nice to meet you","What do you need?","I'm ready hear you"))
        elif ("hear" in text):
            sound = "Yes, I'm hearing"
        elif ("bye" in text or "thank" in text):
            sound = random.choice(("Ok, goodbye","See you again"))
            Exit = True
        elif ("yes" in text or "yep" in text or "okay" in text or "ok" in text):
            url="https://www.google.com/search?q={}".format(query)  
            webbrowser.open_new(url)    
            sound = "There are your search results"
        elif ("time" in text):
            sound = strftime("%H:%M ", localtime())
        elif ("date" in text or "day" in text):
            sound = strftime("%a, %d %b ", localtime())
        elif ("open" in text):
            list_program = os.listdir("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs")
    
            program = text.strip("open").replace(" ","")
            for each in list_program:
                if (program in each or program.upper() in each.upper()):
                    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"+"\\"+each)
                    sound = "Open "+program
                    break
            else: sound = "Not found "+program
        elif text =="":
            sound = random.choice(("I don't hear anything!","I can not hear well", "please speak louder"))
        else:
            sound = "I don't know, Do you want to search for this?"
            query=text
        
        if text =="":
            count_exit +=1
        else: 
            count_exit=0
        if (count_exit>3):
            sound = "Auto Exit, Bye!"
            Exit = True
        print("Robot: " + sound)
        engine.say(sound)
        engine.runAndWait() 
        if Exit is True: break