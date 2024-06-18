# User input and control flow
# Building rock paper scissors (rps)
#Import system, random and enum modules
import sys
import random
from enum import Enum
class RPS(Enum):
    ROCK= 1
    PAPER= 2
    SCISSORS= 3

playagain= True

while playagain:

    print(" ")
    player_choice= input("Enter...\n1 for rock, \n2 for paper, or \n3 for scissors:\n\n")
    # Add a control flow (Procedures)
    player= int(player_choice)
    if player < 1 or player > 3:
        sys.exit("Your input should be between 1-3")
    computer_choice= random.choice("123")
    computer = int(computer_choice)
    print(" ")
    print("You choose", str(RPS(player)).replace("RPS.", ""))
    print("Python choose", str(RPS(computer)).replace("RPS.", ""))
    print(" ")
    if player == computer:
        print("Tie game!")
    elif player == 1 and computer== 3:
        print("You Win 🎉")
    elif player == 2 and computer== 1:
        print("You Win 🎉")
    elif player == 3 and computer== 2:
        print("You Win 🎉")
    else:
        print("Python Win 😜😜😜")

    playagain= input("\n Wanna play again? \n Y for Yes \n Q for quit \n\n")
    if playagain.lower() == "y":
        continue
    else:
       print("Thanks for playing 🎉😍😍")
    sys.exit("Bye! 👋👋👋")
       

