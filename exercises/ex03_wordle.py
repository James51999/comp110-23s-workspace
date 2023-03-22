"""EXO3 - Structured Wordle"""
__author__ = "730165858"

def contains_char(input_word: str, input_character: str) -> bool:
    """search the input word to see if it contains the input character and return a boolean"""
    assert len(input_character) == 1
    idx: int = 0
    while idx < len(input_word):
        if input_character == input_word[idx]:
            return True
        idx += 1
    return False
def emojified(guess: str, secret: str) -> str:
    """compare each index of the guess to the sectret return set of emojis"""
    assert len(guess) == len(secret)
    #emojis
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"  
    emoji: str = ""
    idx: int = 0
    #checking to see if the letter at the index of guess matches that of the secret and if not if that letter exist elsewhere in the secret word. 
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            emoji += green_box
        else:
            if contains_char(secret, guess[idx]) == True:
                emoji += yellow_box
            else:
                emoji += white_box
        idx += 1
    return emoji

def input_guess(expected_length: int) -> str:
    """prompts user for a guess and continues prompting until an input of expected length is given"""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "baits"
    turn: int = 1
    #iterating through the turns and calling the other funtions writen above to print feedback on the users guesses
    while (turn <= 6):
        print (f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret_word))
        if guess == secret_word: 
            print (emojified(guess, secret_word))
            print (f"you won in {turn}/6 turns!")
            return 
        else: 
            print (emojified(guess, secret_word))
        turn += 1
    print("X/6 - Sorry, try again tomorrow!")
    return
if __name__ == "__main__":
    main()