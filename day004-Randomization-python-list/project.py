import random

game_choices = ["rock", "paper", "scissors"]

# Get valid input from the user
try:
    player_index = int(input("Please choose 0 for rock, 1 for paper, 2 for scissors: "))
    if player_index not in [0, 1, 2]:
        raise ValueError("Invalid choice!")
except ValueError as e:
    print(f"Error: {e}")
    exit()

player_choice = game_choices[player_index]
computer_choice = random.choice(game_choices)

print(f"Your choice: {player_choice}, Computer's choice: {computer_choice}")

if computer_choice == player_choice:
    print("It's a tie!")
else:
    if (player_choice == "rock" and computer_choice == "scissors") or \
       (player_choice == "scissors" and computer_choice == "paper") or \
       (player_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")
