#####################################
##    Guessing Game By Author-R    ##
#####################################
import random           #Random Module (For randomly selecting a number).
x=random.randint(1,100)          #Selecting a random number between 1-100
g=1             #Initial guess (default value 1)
n=input("Guess a number(betwen 1-100): ")
while int(n)!=x: 
        g+=1
        if int(n)>x:            #If user guesses greater number
                print("Too high...")
                n=input("guess again: ")
        if int(n)<x:            #If user guesses smaller number
                print("Too low...")
                n=input("guess again: ")
if int(n)==x:                   #When guess is correct
        print(f"You guess correct! in {g} attempts.")
