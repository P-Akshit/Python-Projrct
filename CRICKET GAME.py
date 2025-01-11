# I HAVE MAKE THIS GAME USING PYTHON AT THE AGE OF 15YEAR'S ONLY
# MY NAME AKSHIT PANDEY
import random

batorbowl = [ "Bat", "Bowl" ]
runs = [1, 2, 3, 4, 6, 10, 20, 30, 40, 50,]
toss = ["HEADS", "TAILS"]
choice = ["BATTING", "BOWLING"]
user_runs = 0
computer_runs = 0

computer_name = "Chinu"
print("Hi, I am Chinu.")
user_name = input("What is your name? Please tell me: ").upper()
print("Today, you and I will play a game of cricket.")
print("Two overs only, okay?")

print("Let's do the toss")
user_choice=input().upper()
computer_choice = random.choice(toss)


if user_choice in toss:
     if user_choice == "HEAD" and computer_choice == "TAILS":
          print("You win")
          print("What, do you choice")
          batorbowl=input()

          if batorbowl in choice:
                if batorbowl == "BATTING":
                     print("These are the runs: " + ", ".join(map(str, runs)) + ". Okay?")
                     print("Let's start")
                     run_choice=random.choice(runs)   
                     if run_choice == 1 :
                           user_runs += 1
                     elif run_choice == 2 :
                           user_runs += 2
                     elif run_choice == 3 :
                           user_runs +=3 
                     elif run_choice == 4 :
                           user_runs +=4
                     elif run_choice == 6: 
                          user_runs +=6
                else:
                  user_runs += 0
                  print("OUT")

                  
if user_choice in toss:
    if user_choice == "TAILS":
        if computer_choice == "HEAD":
            print("You win")
            print("What, do you choose? BATTING or BOWLING")
            batorbowl = input().upper()
            
            if batorbowl in choice:
                if batorbowl == "BATTING":
                    user_runs = 0
                    print("These are the runs: " + ", ".join(map(str, runs)) + ". Okay?")
                    print("Let's start")
                    run_choice = random.choice(runs)   
                    if run_choice == 1 :
                           user_runs += 1
                    elif run_choice == 2 :
                           user_runs += 2
                    elif run_choice == 3 :
                           user_runs +=3 
                    elif run_choice == 4 :
                           user_runs +=4
                    elif run_choice == 6: 
                          user_runs +=6
                    else:
                        user_runs += run_choice
                        print("OUT")


if user_choice in toss:
    if user_choice == "TAILS":
        if computer_choice == "HEAD":
            print("You win")
            print("What, do you choose? BATTING or BOWLING")
            batorbowl = input().upper()
            
            if batorbowl in choice:
                if batorbowl == "BOWLING":
                    computer_runs = 0
                    print("These are the runs: " + ", ".join(map(str, runs)) + ". Okay?")
                    print("Let's start")
                    run_choice = random.choice(runs)   
                    if run_choice == 1 :
                           user_runs += 1
                    elif run_choice == 2 :
                           user_runs += 2
                    elif run_choice == 3 :
                           user_runs +=3 
                    elif run_choice == 4 :
                           user_runs +=4
                    elif run_choice == 6: 
                          user_runs +=6
                    else:
                        user_runs += run_choice
                        print("OUT")


if user_choice in toss:
    if user_choice == "HEAD":
        if computer_choice == "TAILS":
            print("You win")
            print("What, do you choose? BATTING or BOWLING")
            batorbowl = input().upper()


            if batorbowl in choice:
                if batorbowl == "BOWLING":
                    computer_runs = 0
                    print("These are the runs: " + ", ".join(map(str, runs)) + ". Okay?")
                    print("Let's start")
                    run_choice = random.choice(runs)   
                    if run_choice == 1 :
                           computer_runs += 1
                    elif run_choice == 2 :
                           computer_runs += 2
                    elif run_choice == 3 :
                           computer_runs +=3 
                    elif run_choice == 4 :
                           computer_runs +=4
                    elif run_choice == 6: 
                          computer_runs +=6
                    else:
                        computer_runs += run_choice
                        print("OUT")


if computer_choice in toss:
    if computer_choice == "HEADS" and user_choice == "TAILS":
        print("You loss")
        print("Coumputer is decding")
        batorbowl=random.choice(batorbowl)

        if batorbowl in choice:
            if batorbowl == "Bat":
                user_runs = 0
                print("These are the runs: " + ", ".join(map(str, runs)) + ". Okay?")
                print("Let's start")
                run_choice = random.choice(runs)
                if run_choice == 1 :
                           computer_runs += 1
                elif run_choice == 2 :
                           computer_runs += 2
                elif run_choice == 3 :
                           computer_runs +=3 
                elif run_choice == 4 :
                           computer_runs +=4
                elif run_choice == 6: 
                          computer_runs +=6
                else:
                    computer_runs += run_choice
                    print("OUT")

       
if computer_choice in toss:
    if computer_choice == "HEADS" and user_choice == "TAILS":
        print("You loss")
        print("Coumputer is decding")
        batorbowl=random.choice(batorbowl)

        if batorbowl in choice:
            if batorbowl == "Bowl":
                print("Computer has choice to bowl first , you need to bat")
                user_runs = 0
                print("These are the runs: " + ", ".join(map(str, runs)) + ". Okay?")
                print("Let's start")
                run_choice = random.choice(runs)
                if run_choice == 1 :
                           computer_runs += 1
                elif run_choice == 2 :
                           computer_runs += 2
                elif run_choice == 3 :
                           computer_runs +=3 
                elif run_choice == 4 :
                           computer_runs +=4
                elif run_choice == 6: 
                          computer_runs +=6
                else:
                    computer_runs += run_choice
                    print("OUT")