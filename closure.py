
def parent_funtion(person):
    coins = 3

    def play_game():
        nonlocal coins
        coins -=1

        if coins > 1:
            print("\n", person, " has ", str(coins), " coins left")
        elif coins == 1:
            print("\n", person, " has ", str(coins)," coin left")
        else:
            print("\n" + person + " is out of coins.")
    return play_game
david= parent_funtion("David")
david= parent_funtion("David")
femi= parent_funtion("Femi")

david()
david()
david()

femi()



            


    