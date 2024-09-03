# Control flow
print("Welcome to the Treasure Island. Your mission is to find the treasure. GoodLuck!")

# Get the player's initial direction
direction = input("Which direction do you want to go?, L for left and  R for right:\n")
if direction.lower() != "l":
    print("Fall into a whole, Game over!")
    exit()
else:
    river_decision = input(
        "You have reached a river, do you want to swim or wait for a boat? S for swim and W for wait:\n"
    )
    if river_decision.lower() != "w":
        print("Get attacked by a monster, Game over!")
        exit()
    else:
        door_choice = input(
            "You are now before a red, blue and yellow door. make your choice, R for red, B for blue and Y for yellow: \n"
        )
        if door_choice.lower() == "y":
            print("You found the treasure, Congratulations!")
            exit()
        elif door_choice.lower() == "r":
            print("Burned by fire, Game over!")
            exit()
        elif door_choice.lower() == "b":
            print("You have been killed")
            exit()
