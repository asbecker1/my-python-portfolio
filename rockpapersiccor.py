#Alison Sophia
#Jan 6
#Rock Paper Scissors

#init
import random #This imports the random library to chose which position the computer plays
wins = 0 #This is a variable for the amount of wins and loses the user has
loses = 0
ties = 0

#functions
print("welcome to rock paper scissors") #This welcomes the user to the rock paper scissors game

#step 1: player select option'
def rockpaperscissors():
    global wins
    global loses
    global ties
    while True: #This is a loop that is continued until it breaks
        player = input ("Selection: either rock, paper, scissors") #This asks the user what they want to play
        if player == "quit":
            break
        #step 2: making selection for the computer
        computer = random.randint(1,3) #This lets the computer chose a random number
        if computer == 1:
            computer = "rock"
            print("computer chose rock")
        elif computer == 2:
            computer = "paper"
            print("computer chose paper")
        else:
            computer = "scissors"
            print("computer chose scissors")

        #step 3: determine the outcome
        if player == "rock" and computer == "scissors":
            print("You won")
            wins = wins + 1
        elif player == "paper" and computer == "rock":
            print("you won")
            wins = wins + 1
        elif player == "scissors" and computer == "paper":
            print("You won")
            wins = wins + 1
        elif player == "rock" and computer == "paper":
            print("You lost")
            loses = loses + 1
        elif player == "paper" and computer == "scissors":
            print("You lost")
            loses = loses + 1
        elif player == "scissors" and computer == "rock":
            print("You lost")
            loses = loses + 1
        else:
            print("You tied")
            ties = ties + 1

        #step 4: loop the game
        print("current record: wins = " + str(wins) + ", loses = " + str(loses) + ", ties = " + str(ties)) #This prints the users amount of wins, loses, and ties

#main
rockpaperscissors() #This is the final function
