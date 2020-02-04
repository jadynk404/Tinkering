import time
import random

def main():
    print("Welcome to the game.")
    time.sleep(3)

def choice():
    answer = str(input("Would you like to continue?"))
    proceed = "Yes" or "yes"
    if answer==proceed:
        choice2()
    else:
        print("very well. See you soon.")

def choice2():
    answer2 = str(input("I will ask one more time. Are you sure you'd like to continue?"))
    proceed2 = "Yes" or "yes"
    if answer2==proceed2:
        choice3()
    else:
        print("very well. See you soon.")

def choice3():
    answer3 = str(input("Then we have come to the first of our challenges. There are two doors ahead of you. Which would you like to go through (1 or 2)"))
    proceed3 = "1"
    if answer3==proceed3:
        choice41()
    else:
        choice42()

def choice41():
    answer41 = str(input("Congratulations. You have chosen the safer path... for now. Now you must decide yet again. Left or Right?"))
    proceed41 = "Left"
    if answer41==proceed41:
        Left()
    else:
        Right()

def choice42():
    answer42 = str(input("You have chosen the difficult path. Now we must place an unfortunate game of truth or dare. Please don't try to avoid completing this in real life. Computers watch you know. So now I ask you. Truth or dare?"))
    proceed42 = "Truth"
    if answer42==proceed42:
        Truth()
    else:
        Dare()


main()
choice()

