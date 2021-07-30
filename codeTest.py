#Personal Assisstant Project
import wolframalpha 
import pyttsx3  
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os 
import pyjokes 
import ctypes 
import time 
import subprocess
import winshell
from tkinter import *


engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
uname = ''


def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 
  
def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    if hour>= 0 and hour<12: 
        speak("Good Morning Sir !") 
   
    elif hour>= 12 and hour<18: 
        speak("Good Afternoon Sir !")    
   
    else: 
        speak("Good Evening Sir !")   
   
    assname =("Jennifer") 
    speak(f"I am {assname}, your Assistant")
      
  
def usrname(): 
    speak("What should i call you sir") 
    global uname 
    uname = takeCommand()
    speak(f"Welcome Mister {uname}") 
    speak(f"How can i Help you ,{uname}") 
  
def takeCommand():     
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        r.adjust_for_ambient_noise(source)
        print("Listening...") 
        r.pause_threshold = 1
        # audio = r.listen(source, phrase_time_limit = 5)
        audio = r.listen(source, timeout = 1)
   
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language ='en-us') 
        print(f"User said: {query}\n") 
   
    except Exception as e: 
        print(e)     
        print("Unable to Recognizing your voice.")   
        return "None"
      
    return query 

if __name__ == '__main__':
    # root = Tk()
    # w = Label(root, text='GeeksForGeeks.org! just this a code test for wht to say but to check whether the window is dynamic or not \n And from here whether the height is increasing or not!!!')
    # w.pack()
    # root.mainloop()

    # exit()

    clear = lambda: os.system('cls')
    clear() 

    # wishMe() 
    # usrname() 
    
    JenniferRuntime = True
    while JenniferRuntime:

        clear()
        query = takeCommand().lower()   

        if 'wikipedia' in query: 
            speak('Searching Wikipedia...')
            speak('What do you want to search on Wikipedia?')
            query = takeCommand() 
            results = wikipedia.summary(query, sentences = 10) 
            speak("According to Wikipedia") 
            print(results) 
            speak(results) 
  
        elif 'open youtube' in query: 
            speak("Here you go to Youtube\n")
            webbrowser.open_new_tab("https://youtube.com")
        
        elif 'open maps' in query: 
            speak("Here you go to Maps\n")
            webbrowser.open_new_tab("https://google.com/maps")
  
        elif 'open google' in query: 
            speak("Here you go to Google\n") 
            webbrowser.open("https://google.com") 
  
        elif 'open stackoverflow' in query: 
            speak("Here you go to Stack Over flow. Happy coding") 
            webbrowser.open("https://stackoverflow.com")    
  
        elif 'play music' in query or "play song" in query: 
            speak("Here you go with music") 
            music_dir = "C:\\Users\\Spedrik Webster\\Music" 
            songs = os.listdir(music_dir) 
            print(songs)     
            random = os.startfile(os.path.join(music_dir, songs[0])) 
  
        elif 'the time' in query: 
            hour = int(datetime.datetime.now().hour)
            minute = int(datetime.datetime.now().minute)
            if minute == 0:
                speak('Its {hour} O clock')
            elif minute in range(1,40):
                speak(f'Its {minute} minutes past {hour} hours')
            else:
                speak(f'Its {minute} minutes to {hour+1} hours')
  
        elif 'how are you' in query: 
            speak("I am fine, Thank you") 
            speak("How are you, Sir")

            query = takeCommand().lower() 
            if 'fine' in query or "good" in query: 
                speak("It's good to know that your fine") 
  
        elif "change my name to" in query: 
            query = query.replace("change my name to", "") 
            assname = query 
  
        elif "change name" in query: 
            speak("What would you like to call me, Sir ") 
            assname = takeCommand() 
            speak("Thanks for naming me") 
  
        elif "what's your name" in query or "What is your name" in query: 
            speak("My friends call me") 
            speak(assname) 
            print("My friends call me", assname) 
  
        elif 'exit' in query: 
            speak("Thanks for giving me your time") 
            exit() 
  
        elif "who made you" in query or "who created you" in query:  
            speak("I have been designed by Yuuvraaj, Mayank and Suuraaj.") 
              
        elif 'joke' in query:
            j = pyjokes.get_joke()
            print(j)
            speak(j) 
              
        elif "calculate" in query:  
              
            app_id = "VJL6YW-E7LE749J57" 
            client = wolframalpha.Client(app_id) 
            indx = query.lower().split().index('calculate')  
            query = query.split()[indx + 1:]  
            res = client.query(' '.join(query))  
            answer = next(res.results).text 
            print("The answer is " + answer)  
            speak("The answer is " + answer)  
  
        elif 'search' in query:   
            query = query.replace("search", "")            
            webbrowser.open('https://www.google.com/search?q='+query)  
        
        elif 'play' in query:   
            query = query.replace("play", "")            
            webbrowser.open('https://www.youtube.com/results?search_query='+query)
  
        elif "who i am" in query: 
            speak("If you talk then definately your human.") 
  
        elif "How you came to world" in query: 
            speak("Thanks to Yuvraj. further It's a secret") 
  
        elif 'powerpoint presentation' in query: 
            speak("opening Power Point presentation") 
            webbrowser.open_new_tab("https://docs.google.com/presentation/")
  
  
        elif "who are you" in query: 
            speak("I am your virtual assistant created by Yuvraj") 
  
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Yuvraj")  
  
        elif 'news' in query:       
            speak('here are some of the top news') 
            webbrowser.open('https://news.google.com/')
          
        elif 'lock window' in query: 
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation() 
  
        elif 'shutdown system' in query: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f')
                  
        elif 'empty recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Recycled") 

        elif "don't listen" in query or "stop listening" in query: 
            speak("for how much time you want to stop me from listening commands") 
            a = int(takeCommand()) 
            time.sleep(a) 
            print(a) 
  
        elif "where is" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("User asked to Locate") 
            speak(location) 
            webbrowser.open("https://www.google.com/maps/place/" + location) 
  
        elif "restart" in query: 
            subprocess.call(["shutdown", "/r"]) 
              
        elif "hibernate" in query or "sleep" in query: 
            speak("Hibernating") 
            subprocess.call("shutdown / h") 
  
        elif "log off" in query or "sign out" in query: 
            speak("Make sure all the application are closed before sign-out") 
            time.sleep(5) 
            subprocess.call(["shutdown", "/l"]) 
  
        elif "write a note" in query or 'make a note' in query or 'note down' in query: 
            speak("What should i write, sir") 
            note = takeCommand() 
            file = open('note.txt', 'w') 
            file.write(note)
            file.close()
          
        elif "my note" in query: 
            speak("Showing Notes") 
            file = open("note.txt", "r")  
            notes = file.read()
            print(notes) 
            speak(notes) 
  
        elif 'jennifer' in query:      
            wishMe() 
            speak("Jennifer 1 point o in your service") 
  
        elif "weather" in query: 
            speak("here's the weather results")   
            webbrowser.open('https://www.google.com/search?q='+'weather')
  
        elif "open wikipedia" in query: 
            webbrowser.open("wikipedia.com") 
  
        elif "good morning" in query: 
            wishMe()
        
        elif "good afternoon" in query: 
            wishMe()
        
        elif "good night" in query: 
            wishMe()

        elif "how are you" in query: 
            speak("I'm fine, glad you asked me that")  
  
        elif "what is" in query or "who is" in query:  
            client = wolframalpha.Client("VJL6YW-E7LE749J57") 
            res = client.query(query) 
              
            try: 
                print (next(res.results).text) 
                speak (next(res.results).text) 
            except StopIteration: 
                print ("No results") 
  
        elif "calculate" in query: 
            query = query.replace("calculate", "")
            client = wolframalpha.Client("VJL6YW-E7LE749J57") 
            res = client.query(query) 
              
            try: 
                print (next(res.results).text) 
                speak (next(res.results).text) 
            except StopIteration: 
                print ("No results")
        
        # print('You Said:- ',query)
        # speak(f'You Said:- {query}')                         # Testing Purpose.
        # speak('You Said:- ',query)
        JenniferRuntime = False
        
