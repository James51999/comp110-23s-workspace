"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730165858"

user_word: str = input("Enter a 5-character word: ")
instances_of_character: int = 0
if (len(user_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
else: 
    user_character: str = input("Enter a single character: ")
    if (len(user_character) != 1):
        print("Error: Character must be a single character.") 
        exit()
    print("Searching for " + user_character + " in " + user_word)
    if (user_word[0] == user_character):
        print(user_character + " found at index 0")
        instances_of_character += 1
    if (user_word[1] == user_character):
        print(user_character + " found at index 1")
        instances_of_character += 1
    if (user_word[2] == user_character):
        print(user_character + " found at index 2")
        instances_of_character += 1
    if (user_word[3] == user_character):
        print(user_character + " found at index 3")
        instances_of_character += 1
    if (user_word[4] == user_character):
        print(user_character + " found at index 4")
        instances_of_character += 1
if (instances_of_character == 0):
    print("No instances of " + user_character + " found in " + user_word)
else:
    if (instances_of_character == 1):
        print("1 instance of " + user_character + " found in " + user_word)
    else:
        print(str(instances_of_character) + " instances of " + user_character + " found in " + user_word)