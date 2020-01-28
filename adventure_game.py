# name: Jadyn Kennedy
# date: 2020-01-28
# description: Text-based Adventure Game

import random
import time


def displayIntro():
    print("Hello Adventurer! Welcome to the game.")
    time.sleep(1)


def choosepath():
    path = ""
    while path != "1" and path != "2": # input validation
        path = input("Would you like to continue? (yes (1) or no(2)) :")

    return path

def checkpath(chosenpath):
    print("Interesting choice. Was it the right one?")
    time.sleep(2)
    print("Let's see.")
    time.sleep(5)

    correctpath = random.randint(1, 2)

    if chosenpath == str(correctpath):
        print("Congratulations. Let's begin.")
    else:
        print("You should have stayed home. Try again.") 

playAgain = "Okay"
while playAgain == "Okay" or playAgain == "Nah":
    displayIntro()
    choice = choosepath()
    checkpath(choice) # choice is equal to "yes" or "no"
    playAgain = input("Play Again?:")

              
