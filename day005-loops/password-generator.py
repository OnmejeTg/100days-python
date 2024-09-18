import random

alphabets = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

special_characters = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "&",
    "*",
    "(",
    ")",
    "-",
    "_",
    "+",
    "=",
    "[",
    "]",
    "{",
    "}",
    ";",
    ":",
    "<",
    ">",
    ",",
    ".",
    "?",
    "~",
]

alphabet_length = int(input("How many alphabet characters do you want: "))
number_length = int(input("How many digits do you want: "))
special_character_length = int(input("How many special characters do you want: "))


password = ""
for _ in range(alphabet_length):
    password += random.choice(alphabets)

for _ in range(number_length):
    password += random.choice(numbers)

for _ in range(special_character_length):
    password += random.choice(special_characters)
# print(password)
password = "".join(random.sample(password, len(password)))
print(password)





# Refactord version

# import random

# # Grouping characters into a dictionary for easier reference
# character_sets = {
#     "alphabets": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
#     "numbers": "0123456789",
#     "special_characters": "!@#$%&*()-_+=[]{};:<>.,?~"
# }

# # Input for number of each type of character in the password
# alphabet_length = int(input("How many alphabet characters do you want: "))
# number_length = int(input("How many digits do you want: "))
# special_character_length = int(input("How many special characters do you want: "))

# # Function to generate a random selection of characters from a given set
# def generate_random_chars(char_set, length):
#     return ''.join(random.choice(char_set) for _ in range(length))

# # Generate the different parts of the password
# alphabet = generate_random_chars(character_sets["alphabets"], alphabet_length)
# number = generate_random_chars(character_sets["numbers"], number_length)
# special_character = generate_random_chars(character_sets["special_characters"], special_character_length)

# # Combine all parts into a single password
# password = alphabet + number + special_character

# # Optional: Shuffle the final password for better randomness
# password = ''.join(random.sample(password, len(password)))

# print(password)
