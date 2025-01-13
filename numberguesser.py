#Raffi Barber
#NumberGuesser
#Init
import random
#Functions
def Guess(x, y):
    raf = random.randrange(x,y)
    guess = int(input("Enter any number " + str(x) + "-" + str(y)))
    while raf!= guess:
        if guess < raf:
            print("Too low!")
            guess = int(input("Enter number again: "))
        elif guess > raf:
            print("Too high!")
            guess = int(input("Enter number again: "))
        else:
            break
    print("you guessed it right!!")

def easyGuess():
    Guess(1, 10)
def mediumGuess():
    Guess(1, 20)
def hardGuess():
    Guess(1, 100)

#Main
hardGuess()
