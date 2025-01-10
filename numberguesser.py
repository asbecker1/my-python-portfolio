#Alison Becker
#11/11/2024

#Initialize
import random

#functions
#Guessing game
play = "" #This makes the play variable 
def guessing_game(): #This makes it into a function
    if play == "yes": #This starts the game if they want to play
        level = str(input("Would you like to play level easy(e), medium(m), or hard(h)?")) #This asks what level
        if level == "e": #This starts the easy game
            guess = int(input("Enter Number (1-10)")) #This asks them for a number
            secretNumber = random.randint(0,10) #This picks a random number
            if secretNumber == guess:
                print("You are correct, you got 10 points!") #This lets them know if they are correct
            else:
                print("You are incorrect, the correct answer was "+str(secretNumber)) #This lets them know they are incorrect and the correct answer
        if level == "m":
            guess = int(input("Enter Number (1-100)"))
            secretNumber = random.randint(0,100)
            if secretNumber == guess:
                print("You are correct, you got 25 points!")
            else:
                print("You are incorrect, the correct answer was "+str(secretNumber))
        if level == "h":
            guess = int(input("Enter Number (1-1000)"))
            secretNumber = random.randint(0,1000)
            if secretNumber == guess:
                print("You are correct, you got 50 points!")
            else:
                print("You are incorrect, the correct answer was "+str(secretNumber))
    else:
        print("Ok, goodbye!") #This is if they said no to playing the game


def final_game(): #This makes another function so the player is able to play again
    global play
    play = str(input("Welcome to Number Guesser, would you like to play?"))
    guessing_game()
    if play == "yes": #This makes sure they only ask you to play again if you have already played
        again = str(input("Would you like to play again?")) #This asks if they would like to play again
        if again == "yes":
            guessing_game()
        else:
            print("Ok, thank you for playing") #This is said if they do not want to play


#main
final_game() #This is my final function
