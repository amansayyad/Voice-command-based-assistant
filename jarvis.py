import pyttsx3  #we use this module because this convert text into speak  
import speech_recognition as sr   #we use this module because It takes microphone input from the user and returns string output
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5') #sapi5 is use to take inbuild voice from our windowsv api
voices = engine.getProperty('voices')#gets the current value of an engine property
print(voices[0].id) # we have tow voice at zero location we have david and at one location we have zira
engine.setProperty('voice',voices[0].id) # we use setproperty to set voice or any property in pyttsx3.




#speak function will pronounce the string which is passed to it
def speak(audio):      #we use def speak(audio) function because our program should speek some thing. and we gave 'audio 'argument beacause it will speek that argument.
    engine.say(audio)   # the audio string engine will speak
    engine.runAndWait() # this will run and wait to audio to pronounce.



def wishMe(): # we use this function because when we will run the program our ai will wis us according to that current time. 
    hour = int(datetime.datetime.now().hour) # in simple wordsthis syntax of taking current time

    if hour>=0 and hour<12:
        speak("Good Morning ,i am Jarvis ,your virtual assistant, developed by Amaan")

    elif hour>=12 and hour<18:
        speak("Good Afternoon ,i am Jarvis, your virtual assistant, developed by Amaan")

    elif hour>=18 and hour<0:
        speak("hii!,i am Jarvis, your virtual assistant, developed by Amaan")

    else:
        speak("Good Evining ,i am Jarvis ,your virtual assistant, developed by Amaan ")


    speak("Please Tell Me How  Can i Help You")

# main program start from here
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening...")
        r.pause_threshold =1 # it stops non speaking audio 1sec means when we are speaking it should take gap of one sec.
        audio = r.listen(source) 

    try:   
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
       
        return "None"
    return query

    
if __name__ == "__main__":
      wishMe()
      while True:
        query=takeCommand().lower()
        #logic for executing taks based on query
        if 'wikipedia' in query:
            speak("searching from wikipedia...")
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak("opening youtube for you ")
            url="youtube.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' 
            webbrowser.get(chrome_path).open(url)


        elif 'open google' in query:
            speak("opening goggle for you ")
            url="google.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

            
        elif 'open facebook' in query:
             speak("opening facebook for you ")
             url="facebook.com"
             chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
             webbrowser.get(chrome_path).open(url)

        elif 'open instagram' in query:
            speak("opening insta for you ")
            url="instagram.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)


        elif 'open amazon' in query:
            speak("opening amazon for you")
            url="amazon.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)


        elif 'open flipkart' in query:
            speak("opening flipkart for you")
            url="flipkart.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)


        elif 'open myntra' in query:
            speak("opening myntra for you")
            url="myntra.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open hotstar' in query:
            speak("opening hotstar for you")
            url="hotstar.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open movies folder' in query:
            speak("opening movies folder")
            moviepath = "D:\\movie"
            os.startfile(moviepath)

        elif 'open bollywood folder' in query:
            speak("opening bollywood folder")
            bollywoodpath ="D:\\movie\\bollywood"
            os.startfile(bollywoodpath)

        elif 'd drive' in query:
            speak("opening bollywood D drive")
            dpath ="D:\\"
            os.startfile(dpath)
            
        elif 'open hollywood folder' in query:
            speak("opening hollywood folder")
            hollywoodpath ="D:\\movie\\hollywood"
            os.startfile(hollywoodpath)

        elif 'open chrome' in query:
            speak("opening chrome ")
            chromepath ="C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)

        elif 'open cmd' in query:
            speak("opening command prompt ")
            cmdpath ="C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(cmdpath)

        elif 'your name' in query:
            speak("i am jarvis, created by mister Amaan Sayyad")

        elif 'your birthday' in query:
            speak("i think that, only biological,entities can have birthday")

        elif 'created you' in query:
            speak("i was, Designed by Aman")
        
        elif 'you live' in query:
            speak("wherever you are, that's where i am")

        elif 'your father' in query:
            speak("i dont have any family!!,but i have you aman!")

        elif 'your mother' in query:
            speak("i dont have any family!!,but i have you aman!")

        elif 'your brother' in query:
            speak("i dont have any family!!,but i have you aman!")
        
        elif 'your sister' in query:
            speak("i dont have any family!!,but i have you aman!")

        elif 'play iron man movie 1' in query:
            ironmanpath="D:\\movie\\hollywood\\marvel movie\\ironman\\Iron Man (2008) 720p BRRip [Dual Audio] [Eng-Hin].sbaz44[fokatworld.com].mkv"
            os.startfile(ironmanpath)

        elif 'play iron man movie 2' in query:
            ironpath="D:\movie\hollywood\marvel movie\ironman\\Iron Man 2 2010 720p  BRRiP Dual Audio Hindi Eng[Sub]--ChEtAn.mkv"
            os.startfile(ironpath)
            
        elif 'sleep' in query:
            speak("ok,nice talking with you")
            quit()

       
       

    
            
                


    

  

    
        

        


    

        
        


        

       


    