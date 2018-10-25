import random
print("                                       Guessing Game!")
print("Win at 1st attempt: Rs.50")
print("Win at 2nd attempt: Rs.30")
print("Win at 3rd attempt: Rs.15")
comGuess=random.randint(1,10)

while True:
    userGuess=int(input("Guess no. b/w (1-10): "))
    if(userGuess>comGuess):
        print("Guess Lower...")
    elif(userGuess<comGuess):
        print("Guess Heigher...")
    elif(userGuess==comGuess):
        print("Cogngo! Your guess was correct.")
        break
