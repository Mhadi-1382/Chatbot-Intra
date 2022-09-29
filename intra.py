
# Intra (ChatBot)
# Built by Mahdi Rabiee
# Created: Wendnesday, Sep 14, 2022


from colorama import Fore
from time import ctime
import webbrowser
import wikipedia
import datetime
import platform
import winsound
import pyttsx3
import random
import os
import re


# Engine speak
Engine = pyttsx3.init('sapi5')
Engine.setProperty('rate', 140)
Voice = Engine.getProperty('voices')
Engine.setProperty('voice', Voice[0].id)

def speak(text):
    Engine.say(text)
    Engine.runAndWait()


# Get username PC
Platform_get_user = platform.uname()
Get_username = Platform_get_user.node


# CLS
os.system("cls")


# Splash screen
Splash_screen = """
    I N T R A.
==============
"""
print(Fore.BLUE + Splash_screen + Fore.WHITE + "\n")


# Sound Log on
winsound.PlaySound("logon.wav", winsound.SND_FILENAME)


# Take commands (Input)
def Take_commands():
    query = input("You: ")
    return query

# Bot (Output)
def Bot(output):
    print("Bot: " + output)


# Wish me
def Wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")


# Play sound
def Play_sound(address = str):
    winsound.PlaySound(address, winsound.SND_FILENAME)


# Commands
while True:

    query = Take_commands().lower()


    if 'hello' in query or 'hi' in query or 'hey' in query:
        List_output = ["Hello ", "Hi "]
        List_output_random = random.choice(List_output)
        Bot(List_output_random + Get_username)
        speak(List_output_random + Get_username)
        Wish_me()

    elif 'what are you doing' in query:
        Bot("Responding to your commands")
        speak("Responding to your commands")

    elif 'what\'s up' in query:
        List_output = ["Fine!", "Thanks i\'m ok."]
        List_output_random = random.choice(List_output)
        Bot(List_output_random)
        speak(List_output_random)

    elif 'how are you' in query:
        List_output = ["I\'m good!", "Not bad, how are you?", "Good. And you?"]
        List_output_random = random.choice(List_output)
        Bot(List_output_random)
        speak(List_output_random)

    elif 'thanks' in query or 'thank' in query or 'thank you' in query:
        List_output = [f"Thank you {Get_username} 😍", "Thanks you very much."]
        List_output_random = random.choice(List_output)
        Bot(List_output_random)
        speak(List_output_random)

    elif 'fine' in query:
        List_output = ["Very great.", "It is awesome"]
        List_output_random = random.choice(List_output)
        Bot(List_output_random)
        speak(List_output_random)

    elif 'what can you do' in query:
        Bot("I\'m your virtual chatbot. and i can talk to you or greet you, and i can also do a series of small things like: change the voice, announce the time, search web - Wikipedia, etc.")
        speak("I\'m your virtual chatbot. and i can talk to you or greet you, and i can also do a series of small things like: change the voice, announce the time, search web - Wikipedia, etc.")

    elif 'who made you' in query or 'who developed you' in query or 'who created you' in query:
        Bot("I\'ve been developed by Mahdi Rabiee")
        speak("I\'ve been developed by Mahdi Rabiee")

    elif 'who are you' in query:
        Bot("My name is Intra. I\'m your virtual chatbot.")
        speak("My name is Intra. I\'m your virtual chatbot.")

    elif 'when is your birthday' in query:
        Bot("I made my debut on Wendnesday, September 14, 2022")
        speak("I made my debut on Wendnesday, September 14, 2022")

    elif 'where do you live' in query:
        Bot("I live in your computer...")
        speak("I live in your computer...")

    elif 'in what language are you written' in query:
        Bot("I\'m programmed in Python")
        speak("I\'m programmed in Python")

    elif 'do you know me' in query:
        List_output = [f"You told me your name was {Get_username}. I could never forget that 😊" , f"I remember you telling me your name was {Get_username}"]
        List_output_random = random.choice(List_output)
        Bot(List_output_random)
        speak(List_output_random)

    elif 'who am i' in query:
        Bot(f"{Get_username}")
        speak(f"{Get_username}")

    elif 'what my favorite color?' in query or 'what my favorite color' in query:
        try:
            file = open("temp_color.txt", "r")
            Read_speak = file.read()
            Bot(f"Your favorite color is {Read_speak}")
            speak(f"Your favorite color is {Read_speak}")
        except:
            print(" What is your favorite color?")
            speak("What is your favorite color?")
            Input_color = input(" Type your color (Blue, White ...): ")
            if Input_color == '':
                print(Fore.RED + " Your data is not valid." + Fore.WHITE)
                speak("Your data is not valid.")
            else:
                Path_file = "temp_color.txt"
                with open(Path_file, "w") as file:
                    file.write(Input_color)
                    file.close()
                    print(" Great, I remember your favorite color in my mind.")
                    speak("Great, I remember your favorite color in my mind.")

    elif 'what my favorite movie?' in query or 'what my favorite movie' in query:
        try:
            file = open("temp_movie.txt", "r")
            Read_speak = file.read()
            Bot(f"Your favorite movie is {Read_speak}")
            speak(f"Your favorite movie is {Read_speak}")
        except:
            print(" What is your favorite movie?")
            speak("What is your favorite movie?")
            Input_movie = input(" Type your movie (Spider Man ...): ")
            if Input_movie == '':
                print(Fore.RED + " Your data is not valid." + Fore.WHITE)
                speak("Your data is not valid.")
            else:
                Path_file = "temp_movie.txt"
                with open(Path_file, "w") as file:
                    file.write(Input_movie)
                    file.close()
                    print(" Great, I remember your favorite movie in my mind.")
                    speak("Great, I remember your favorite movie in my mind.")

    elif 'can you change your voice' in query or 'change voice' in query:
        Bot("Yes, i can do...")
        speak("Yes, i can do...")
        An = input(" Change your voice (M / F): ")
        if 'm' in An.lower():
            Engine.setProperty('voice', Voice[0].id)
            print(" Change your voice: Male")
            speak("Change your voice: Male")
        elif 'f' in An.lower():
            Engine.setProperty('voice', Voice[1].id)
            print(" Change your voice: Female")
            speak("Change your voice: Female")
        else:
            print(Fore.RED + " Changes failed." + Fore.WHITE)
            speak("Changes failed.")

    elif 'open code' in query or 'open source code' in query:
        Code_path = "https://github.com/"
        Bot(Code_path)
        webbrowser.open_new(Code_path)
        speak("Opening source code")

    elif 'time' in query or 'what time is it' in query:
        Bot(ctime())
        speak(ctime())

    elif 'search' in query:
        Searching = re.search("search (.*)", query)
        if Searching:
            q = Searching.group(1)
            url = "https://www.google.com/search?q=" + q
            print(" Searching for " + q)
            webbrowser.open_new(url)
            speak(" Searching for " + q)
        else:
            List_output = [" Invalid search result. please, try again.", " Search not found."]
            List_output_random = random.choice(List_output)
            print(Fore.YELLOW + List_output_random + Fore.WHITE)
            speak(List_output_random)

    elif 'wiki' in query:
        speak("Searching Wikipedia")
        Enter_text = input(" Searching Wikipedia: ")
        Result = wikipedia.summary(Enter_text)
        print(Result)
        speak(Result)

    elif 'reboot' in query or 'reset' in query or 'restart' in query:
        Bot("Reboot bot")
        speak("Reboot bot")
        Play_sound("reboot.wav")
        for i in range(3):
            os.system("cls")
            
        print(Fore.BLUE + Splash_screen + Fore.WHITE + "\n")

    elif 'goodbye' in query or 'bye' in query:
        Bot(f"Goodbye {Get_username}.")
        speak(f"Goodbye {Get_username}.")
        Play_sound("shutdown.wav")
        exit()

    else:
        Bot(Fore.YELLOW + "Please, try again." + Fore.WHITE)
        speak("Please, try again.")
