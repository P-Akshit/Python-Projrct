# I HAVE MAKE THIS GAME USING PYTHON AT THE AGE OF 15YEAR'S ONLY
# MY NAME AKSHIT PANDEY
import random

computer_name = "hilo"
print("Hi, I am hilo.")
print("What is your name? Please tell me: ")
user_name = input()
print("Today, you and I will play a game of Rock, Paper, Scissors.")
print("Three rounds only, okay?")

choices = ["ROCK", "PAPER", "SCISSORS"]
rounds = 3
user_point = 0
computer_point =0

print("Are,you ready then , lets go!") 

for round_num in range(rounds):
    print(f"\nLet's play round {round_num + 1}")
    print("ROCK , PAPER , SCISSORS  , Choose one")
    user_choice = input().upper()
    computer_choice = random.choice(choices)
    print("Computer chooses:", computer_choice)


# Validate user input
    while user_choice not in choices:
     print("Invalid input. Please choose from ROCK, PAPER, or SCISSORS.")
     user_choice = input().upper()



    if user_choice == computer_choice:
       print("It's a tie!")
       user_point += 0
       computer_point +=0

    elif user_choice == "SCISSORS" and computer_choice == "PAPER":
      print("You win")
      computer_point +=0
      user_point += 1

    elif user_choice == "ROCK" and computer_choice == "SCISSORS":
        print("You win")
        user_point += 1
        computer_point +=0

    elif  user_choice == "PAPER" and computer_choice == "ROCK":
        print("You win")
        user_point += 1
        computer_point +=0

    else:
        print("You lose")
        computer_point += 1
else:
    print("It's a tie!")

play_again = input("\nWould you like to play another game? (yes/no): ").lower()
while play_again not in ("yes", "no"):
    play_again = input("Invalid input. Please enter 'yes' or 'no': ").lower()

if play_again == "yes":
    # Reset scores and start a new game
    user_point = 0
    computer_point = 0
    # (Continue with the game code)
else:
    print("Thanks for playing!")
