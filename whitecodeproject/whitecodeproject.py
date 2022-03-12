import beepy
import random
import webbrowser
import os
import time
import urllib.request
import urllib.parse
import re
import pyttsx3
import datetime
import wikipedia

engine = pyttsx3.init()

rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)     # setting up new voice rate


def speak(audio):
    engine.say(audio)
    # Without this command, speech will not be audible to us.
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("WhiteCode: Good Morning!")

        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        print("WhiteCode: Good Afternoon!")

        speak("Good Afternoon!")

    else:
        print("WhiteCode: Good Evening!")

        speak("Good Evening!")


wishMe()

engine.say("Ok let's begin: ")
engine.runAndWait()
print("WhiteCode: Ok let's begin ")


engine.say("Please enter your name: ")
engine.runAndWait()
name = input("WhiteCode: Please enter your name \nUser: ")


engine.say("Hi " + name + " my name is WhiteCode")
engine.runAndWait()
print("WhiteCode: Hi " + name + " my name is WhiteCode")
print("========================================")

while True:

    try:
        engine.say("How old are you? ")
        engine.runAndWait()
        age = int(input("WhiteCode: How old are you? \n" + name + ": "))

        if age <= 18:
            engine.say("Oh so you are still a kid!")
            engine.runAndWait()
            print("WhiteCode: Oh so you are still a kid!")

            break
        elif age >= 18:
            engine.say("You are very old hahahaha... im just kidding")
            engine.runAndWait()
            print("WhiteCode: You are very old hahahaha... im just kidding")

            break

    except Exception as e:
        print(e)

        beepy.beep(2)
        engine.say("This is not a whole number.")
        engine.runAndWait()
        print("WhiteCode: This is not a whole number.")

        break
print("========================================")
while True:
    engine.say(
        "I'm gonna give you a sound that describes you, give me a number between 1 and 7 ")
    engine.runAndWait()
    sound = int(input(
        "WhiteCode: I'm gonna give you a sound that describes you, give me a number between 1 and 7 \n" + name + ": "))

    beepy.beep(sound)
    print("========================================")

    break

engine.say("Now let's play a game")
engine.runAndWait()
print("WhiteCode: Now let's play a game")


computer = random.choice(["rock", "paper", "scissors"])

while True:
    engine.say("rock, paper or scissors? ")
    engine.runAndWait()
    player = input("WhiteCode: rock, paper or scissors? \n" + name + ": ")

    engine.say("i choose: " + computer)
    engine.runAndWait()
    print("WhiteCode: i choose: " + computer)

    if player == "rock":
        if computer == "paper":
            engine.say("you lose")
            engine.runAndWait()
            print("WhiteCode: you lose")

        elif computer == "rock":
            engine.say("you tied")
            engine.runAndWait()
            print("WhiteCode: you tied")

        else:
            engine.say("you won")
            engine.runAndWait()
            print("WhiteCode: you won")

    elif player == "paper":
        if computer == "paper":
            engine.say("you tied")
            engine.runAndWait()
            print("WhiteCode: you tied")

        elif computer == "rock":
            engine.say("you won")
            engine.runAndWait()
            print("WhiteCode: you won")

        else:
            engine.say("you lose")
            engine.runAndWait()
            print("WhiteCode: you lose")

    elif player == "scissors":
        if computer == "paper":
            engine.say("you won")
            engine.runAndWait()
            print("WhiteCode: you won")

        elif computer == "rock":
            engine.say("you lose")
            engine.runAndWait()
            print("WhiteCode: you lose")

        else:
            engine.say("you tied")
            engine.runAndWait()
            print("WhiteCode: you tied")

    else:
        beepy.beep(3)
        engine.say(
            "No one wins. Please check your spelling again. Something is wrong!")
        engine.runAndWait()
        print(
            "WhiteCode: No one wins. Please check your spelling again. Something is wrong!")

    computer = random.choice(["rock", "paper", "scissors"])
    break
print("========================================")
engine.say("Here is my website!")
engine.runAndWait()
print("WhiteCode: Here is my website!")


while True:
    engine.say("Do you want to see it? Please write yes or no: ")
    engine.runAndWait()
    website = input(
        "WhiteCode: Do you want to see it? Please write yes or no: \n" + name + ": ")

    if website == "yes":
        engine.say("Look at it")
        engine.runAndWait()
        print("WhiteCode: Look at it")

        webbrowser.open("https://stoacommunity.com")
        time.sleep(5)
        engine.say(
            "How does it look? Make sure to subscribe for better content! Press any key! ")
        engine.runAndWait()
        opinion = input(
            "WhiteCode: How does it look? Make sure to subscribe for better content! Press any key! \n" + name + ": ")

        webbrowser.open("https://stoacommunity.com/subscribe")
        break
    elif website == "no":
        engine.say("Oh ok, maybe next time")
        engine.runAndWait()
        print("WhiteCode: Oh ok, maybe next time")

        break
    else:
        beepy.beep(3)
        engine.say("Im sorry, but you didn't specify yes or no.")
        engine.runAndWait()
        print("WhiteCode: Im sorry, but you didn't specify yes or no.")

        break
print("========================================")
engine.say("Now who is your favorite scientist? ")
engine.runAndWait()
sci = input("WhiteCode: Now who is your favorite scientist? \n" + name + ": ")

engine.say("Wow, " + sci +
           " was one of the greatest minds in history! Mine was Nikola Tesla! ")
engine.runAndWait()
print("WhiteCode: Wow, " + sci +
      " was one of the greatest minds in history! Mine was Nikola Tesla! ")

print("========================================")
engine.say("What kind of music do you like? ")
engine.runAndWait()
music = input("WhiteCode: What kind of music do you like? \n" + name + ": ")

engine.say(music + " " + "is an amazing genre.")
engine.runAndWait()
print("WhiteCode: " + music + "is an amazing genre.")


engine.say(
    "Lets see whats you favorite song? (Please write your song and the artist) ")
engine.runAndWait()
search_keyword = input(
    "WhiteCode: Lets see whats you favorite song? (Please write your song and the artist): \n" + name + ": ")

new_keyword = search_keyword.replace(" ", "+")
html = urllib.request.urlopen(
    "https://www.youtube.com/results?search_query=" + new_keyword)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
url = "https://www.youtube.com/watch?v=" + video_ids[0]
webbrowser.open(url)

engine.say("I have found the song for you!")
engine.runAndWait()
print("WhiteCode: I have found the song for you!")

print("WhiteCode: Here it is: " "http://www.youtube.com/watch?v=" +
      video_ids[0])

print("========================================")
speak("Please, before you go, try one of my features: ")
print("WhiteCode: Please, before you go, try one of my features: ")

speak("You can search anything in wikipedia, youtube, google, i can give you the time too! ")
print("WhiteCode: You can search anything in wikipedia, youtube, google, i can give you the time too! ")

# Converting user query into lower case
query = input("WhiteCode: Please try one of my features: \n" + name + ": ")


# Logic for executing tasks based on query
if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=5)
    speak("According to Wikipedia")
    print("WhiteCode: " + results)

    speak(results)
elif 'open youtube' in query:
    webbrowser.open("https://youtube.com")
elif 'open google' in query:
    webbrowser.open("https://google.com")
elif 'the time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"WhiteCode: Sir, the time is {strTime}")
elif 'search' in query:
    text = query.replace("search", "")
    webbrowser.open("https://www.google.com/search?q=" + text)
    time.sleep(5)
else:
    speak("Function is not available")
    print("WhiteCode: Function is not available")

print("========================================")
engine.say("Goodbye!")
engine.runAndWait()
print("WhiteCode: Goodbye!")


time.sleep(5)

engine.say("Please press enter to finish the dialogue")
engine.runAndWait()
input("WhiteCode: Please press enter to finish the dialogue \n" + name + ": ")
