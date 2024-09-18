# import random 
# print("Welcome to the hangman game!!")
# word_list = [
#     "Python",
#     "Flutter",
#     "Database",
#     "Algorithm",
#     "Function",
#     "Variable",
#     "Version",
#     "Debugging",
#     "Terminal",
#     "Middleware"
# ]
# random_word = random.choice(word_list).lower()
# life = len(random_word)
# spaces = ""
# for letter in random_word:
#     spaces +="-"


# print(random_word)
# while '-' in spaces and life > 0:
#     guess = input("Take a guess: ")
#     if guess in random_word:
#         position = [int(i)+1 for i, letter in enumerate(random_word) if letter == guess]
#         spaces = list(spaces)
#         for i in position:
#             spaces[i-1] = random_word[i-1]
#         spaces = ''.join(spaces)   
#     else:
#         life = life - 1 

#     print(spaces)
#     print(life)
    
# if not '-' in spaces:
#     print("You win!")
# else:
#     print("You loss")



import random

def hangman_game():
    print("Welcome to the Hangman Game!!")

    # Word list
    word_list = [
        "Python", "Flutter", "Database", "Algorithm", "Function",
        "Variable", "Version", "Debugging", "Terminal", "Middleware"
    ]

    # Randomly select a word and initialize game state
    random_word = random.choice(word_list).lower()
    life = len(random_word)
    guessed_word = ['-' for _ in random_word]  # Use list to store guessed letters

    print(f"The word has {len(random_word)} letters.")

    # Game loop
    while '-' in guessed_word and life > 0:
        print(f"Lives left: {life}")
        print("Word to guess: " + ''.join(guessed_word))

        guess = input("Take a guess: ").lower()

        # If the guess is correct
        if guess in random_word:
            for i, letter in enumerate(random_word):
                if letter == guess:
                    guessed_word[i] = letter
        else:
            life -= 1  # Deduct a life for wrong guess

        print()  # For better spacing

    # End of the game
    if '-' not in guessed_word:
        print(f"Congratulations! You guessed the word '{random_word}'. You win!")
    else:
        print(f"Sorry, you ran out of lives. The word was '{random_word}'. You lose.")

# Run the game
hangman_game()
