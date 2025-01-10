#Alison Sophia
#Name Generator

print("Welcome to what snack are you?") #This welcomes them to my quiz to determine which snack they are
print("Answer the questions to find which fruit are you!")

def snack_generator(): #This is a function to determine which snack they are
    ans = input ("Salty or Sweet?") #This asks them to pick between salty or sweet
    if ans == str("salty"): #This creates an if statement depending on what the person picked
        ans = input ("Picnic (p) or Movie Night (m)?")
        if ans == "p":
            ans = input ("Shower (s) or bath (b)?")
            if ans == "s":
                ans = print ("You are prezels!") #This tells them which snack they are
            else:
                ans = print("You are cheese and crackers!")
        if ans == "m":
            ans = input("Summer (s) or Winter (w)?")
            if ans == "w":
                ans = print("You are popcorn!")
            else:
                ans = print("You are chips!")
    if ans == str("sweet"): #This creates a different if statement if the person picked sweet
        ans = input ("Hike (h) or Game Night(g)?")
        if ans == "h":
            ans = input ("morning (m) or evening(e)?")
            if ans == "m":
                ans = print ("You are fruit!")
            else:
                ans = print("You are a granola bar!")
        if ans == "g":
            ans = input("calm (c) or energetic (e)?")
            if ans == "c":
                ans = print("You are a cookie!")
            else:
                ans = print("You are animal crackers!")




#main
snack_generator() #This is the final snack generator
