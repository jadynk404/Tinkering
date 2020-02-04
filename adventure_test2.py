
import random
import time

def main():
    print("Hello Adventurer! Welcome to the game.")
    time.sleep(1)

def choice():
    path = ""
    while path != "yes" and path != "no":
        path = input("Would you like to continue? (yes or no)")

    return path
def checkpath(chosenpath):
    print("Interesting.")
    time.sleep(2)

    correctpath = yes


    if checkpath(chosenpath) == str(correctpath):
        def choice2():
            path1 = ""
            while path1 != "yes" and path1 != "no":
                path1 = input("I will ask one more time. just to be sure. are you sure you want to continue?")
            return path1
    else:
        print("Fair enough. See you later.")
                   

main()
choice()
checkpath()
choice2()

