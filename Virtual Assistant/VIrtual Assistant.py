import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


print("Welcome to our project")
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Welcome to our Project')
engine.runAndWait()

def talk(text):

      engine.say(text)
      engine.runAndWait()

def take_command():
   try:
      with sr.Microphone() as source:
        print("listening.....")
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        command=command.lower()
        if 'iris' in command:
            command=command.replace('iris','')
            print(command)
   except:
      pass
   return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
        print(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%p')
        print(time)
        talk('Current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'send' in command:
        talk("Will send the msg to the given number in few seconds")
        message=pywhatkit.sendwhatmsg("+917397424668","Macha epdi ok va automate msg",21,50)

    elif 'joke' in command:
        jk=pyjokes.get_joke()
        print(jk)
        talk(jk)
    elif 'introduce' in command:
        talk('Hi Everyone. I am iris and i was developed by many members. But now i was developed by the narikootam. My Important job is I wish to help many people')

    elif 'purpose' in command:
        talk("Yes. My purpose is to help and serve people by some works. I wish to spend most of the time with people. I also be a best friend for everyone")

    elif 'thank' in command:
        talk('Dont mention it.Its my Service for everyone')
    elif 'exit yourself' in command:
        talk("Ok.Thank you for your obedience with me.")
        exit()
    else:
        talk('Please say the command again.')

while True:
         run_alexa()






