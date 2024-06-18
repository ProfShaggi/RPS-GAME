import sys
import random
from enum import Enum

def play_rps():
    Game_count= 0
    tie_game= 0
    player_wins= 0
    python_wins= 0

    def rps():
        nonlocal player_wins
        nonlocal python_wins
        nonlocal tie_game
        class RPS(Enum):
            ROCK= 1
            PAPER= 2
            SCISSORS= 3

        print(" ")
        player_choice= input("Enter...\n1 for rock, \n2 for paper, or \n3 for scissors:\n\n")
        # Add a control flow (Procedures)
        if player_choice not in ["1", "2", "3"]:
            print("Your input should be between 1-3")
            return rps()
        player= int(player_choice)
        computer_choice= random.choice("123")
        computer = int(computer_choice)
        print(" ")
        print("You choose", str(RPS(player)).replace("RPS.", ""))
        print("Python choose", str(RPS(computer)).replace("RPS.", ""))
        print(" ")
        def decision_making(player, computer):
            nonlocal tie_game
            nonlocal player_wins
            nonlocal python_wins

            if player == computer:
                tie_game += 1
                return "Tie game!"
            elif player == 1 and computer== 3:
                player_wins += 1
                return "You Win 🎉"
            elif player == 2 and computer== 1:
                player_wins += 1
                return "You Win 🎉"
            elif player == 3 and computer== 2:
                player_wins += 1
                return "You Win 🎉"
            else:
                python_wins += 1
                return "Python Win 😜😜😜"
        game_result= decision_making(player, computer)
        print(game_result)

        nonlocal Game_count
        Game_count += 1
        print("Game Count:" + str(Game_count))
        print("Tie game:" + str(tie_game))
        print("Player wins:" + str(player_wins))
        print("Python wins:" + str(python_wins))

        print("\nWanna play again?")
        playagain = True
        while playagain:
            playagain= input("\n Y for Yes \n Q for quit \n")
            if playagain not in ["Y", "Q"]:
                print("Oops! Incorrect Input".center(25, "*"))
                continue
            elif playagain == "Y":
                return rps()
            else:
                print("Thanks for playing 🎉😍😍")
                sys.exit("Bye! 👋👋👋")

    return rps

play= play_rps()
play()

if __name__ == "__main__":
    play_rps()

    
