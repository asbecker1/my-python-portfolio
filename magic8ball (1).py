#Alison Becker

import random
import time
magic_list = ["yes", "no", "maybe", "concentrate and ask again", "unlikely", "most likely", "certainly", "Absolutely not", "I wouldn't count on it", "No way Jose", "Reply hazy, try again", "Answer unclear", "Only time will tell...", "if the stars align", "no my sweetie pumpkin"] #magic 8 ball responces

def magic8ball():
    print("Welcome to magic 8 ball! We hope to answer some of your questions today")
    while True:
        question = str(input("Please ask as a yes or no question"))
        x = question.endswith("?")
        if x == True:
            for i in range(3):
                print("shaking..")
                time.sleep(2)
            print(random.choice(magic_list))
        else:
            print("ERROR: Please ask a question with a ? at the end!")
        again =input("Would you like to ask another question? Yes or no?")
        if again == "no":
            print("thank you for playing, come again soon!")
            break

#main
magic8ball()

