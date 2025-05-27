#Alison Becker

#init
slot_symbols = ["❀", "✿", "7"]
print(slot_symbols)
credits = 100
import random
import time

#functions
def slotMachine():
    global slot_symbols
    global credits
    print("Welcome to the slot machine!")
    while True:
        print("You have " + str(credits) + " credits to play, and each game is 10 cedits")
        play = input("Would you like to spin or quit? Press (s) to spin or (q) to quit")
        if play == "s":
            credits = credits - 10
            one = random.choice(slot_symbols)
            two = random.choice(slot_symbols)
            three = random.choice(slot_symbols)
            print("spinning..")
            if one == two and two == three == "7":
                print(one, two, three)
                print("YOU WON 1000 CREDITS!!")
                credits = credits + 1000
                print("You now have " + str(credits) + " credits!")
            elif one == two and two == three:
                print(one, two, three)
                print("You won 100 credits!!")
                credits = credits + 100
                print("You now have " + str(credits) + " credits!")
            else:
                print(one, two, three)
                print("You lost :(")
        else:
            print("Thank you for playing!")
            break




#main
slotMachine()
#1. Introduction
#2. Ask player if they would like to spin or quit
#3. Randomly pull three symbols from our list (make them a variable)
#4. Determine the outcome (Jackpot, Match, Loss - If, elif, else)
