#Raffi Barber
#1/7/2025
#Rock Paper Scissors

#Init
import random
options = ["Rock", "Paper", "Scissors"]

#Functions
def rockpaperscissors():
    global options
    while True:
        print("Welcome to Rock Paper Scissors")
        print("What's your move?")
        player = input("Rock, Paper, Scissors, Shoot: ")
        player = player.capitalize()
        #Step 2: Generate the computer's move
        computer = random.choice(options)

        print("You chose: ", player)
        print("Computer chose: ", computer)

        #Step 3:
        if player == computer:

            print("Tie 😐... boring!")

        elif player == "Rock" and computer == "Scissors":

            print("Good stuff 💯")

        elif player == "Paper" and computer == "Rock":

            print("Good stuff 💯")

        elif player == "Scissors" and computer == "Paper":

            print("Good stuff 💯")

        else:

            print("Yikes 😬 You stink!!")
        answer = input("Continue playing? Yes or No: ")
        answer = answer.capitalize()
        if answer == "Yes":
            print("Running it back...")
        else:
            print("Ciao 👋")
            break

#Main
rockpaperscissors()
#Step 1: Get the player's move


