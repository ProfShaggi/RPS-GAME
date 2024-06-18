import sys
import random

def guess_number():
    game_count= 0
    player_wins= 0

    def play_game():
        nonlocal game_count
        nonlocal player_wins
        username= input("\nEnter Username\n\n")
        if username == username:
            print(username , + '''guess which number I'm thinking of...1, 2, or 3''')
        enter_number= input("\n")
        return play_game()
    
play= guess_number()
play()
        