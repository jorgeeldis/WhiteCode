import beepy
import random
import webbrowser
import os
import time
import urllib.request
import urllib.parse
import re

print("Ok let´s begin: ")

name = input("Please enter your name: ")
print("Hi " + name + " my name is WhiteCode")

while True:
    
    try:
        age = int(input("How old are you? "))

        if age <= 18:
            print("Oh so you are still a kid!")
            break
        elif age >= 18:
            print("You are very old haha im just kidding")
            break

    except Exception as e:
        print(e)
        beepy.beep(2)
        print("This is not a whole number.")
        break

while True:
    sound = int(input("I'm gonna give you a song that describes you, give me a number between 1 and 7 "))
    beepy.beep(sound)
    print("========================================")
    break


print("Now let´s play a game")

computer = random.choice(["rock", "paper", "scissors"])

while True:
    player = input("rock, paper, scissors? ")
    print ("computer: " + computer)
    if player == "rock":
        if computer == "paper":
            print("you lose")
        elif computer == "rock":
            print("you tied")
        else:
            print("you won")
    elif player == "paper":
        if computer == "paper":
            print("you tied")
        elif computer == "rock":
            print("you won")
        else:
            print("you lose")
    elif player == "scissors":
        if computer == "paper":
            print("you won")
        elif computer == "rock":
            print("you lose")
        else:
            print("you tied")
    else:
        beepy.beep(3)
        print("No one wins. Please check your spelling again. Something is wrong!")
    computer = random.choice(["rock", "paper", "scissors"])
    break

print("Here is my website!")

while True:
    website = input("Do you want to see it? Please write yes or no: ")
    if website == "yes":
        print("Look at it")
        webbrowser.open("https://stoacommunity.com")
        time.sleep(5)
        opinion = input("How does it look? Make sure to subscribe for better content! Press any key! ")
        webbrowser.open("https://stoacommunity.com/subscribe")
        break
    elif website == "no":
        print("Oh ok, maybe next time")
        break
    else:
        beepy.beep(3)
        print("Im sorry, but you didn´t specify yes or no.")
        break

sci = input("Now who is your favorite scientist? ")
print("Wow " + sci + " was one of the greatest minds in history! Mine was Nikola Tesla! ")

music = input("What kind of music do you like? ")
print(music + " is an amazing genre.")

search_keyword = input("Lets see whats you favorite song? ")
html = urllib.request.urlopen(
    "https://www.youtube.com/results?search_query=" + search_keyword)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
url = "https://www.youtube.com/watch?v=" + video_ids[0]
webbrowser.open(url)

print("I have found the song for you!\nHere it is: " "http://www.youtube.com/watch?v=" + video_ids[0])


print("Goodbye!")

time.sleep(5)

input("Please press enter to finish the dialogue")
