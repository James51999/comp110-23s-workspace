"""EXO2 - One-Shot wordle - Loops"""
__author__ = 730165858

SECRET: str = "python"
length_secret: int = len(SECRET)
guess: int = input(f"What is your {length_secret}-Letter guess? ")
#emoji box code
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
#check to see that the guess is the correct number of letters
while len(guess) != length_secret:
        guess = input(f"That was not {length_secret} letters! Try again: ")
#innitiallize index and emoji storage
idx: int = 0
emoji: str = ""
#iterate through the guess and add emojis to the strig to keep track of correct letters
while idx < length_secret: 
     if guess[idx] == SECRET[idx]:
         emoji += GREEN_BOX
     else:
         #is the letter in guess exist somewhere else in the secret word?
         idx_yello: str = 0
         instances: str = 0
         while idx_yello < length_secret:
            if guess[idx] == SECRET [idx_yello]:
              instances += 1
            else:
                instances += 0
            idx_yello +=1
         if instances >= 1:
             emoji += YELLOW_BOX
         else:
             emoji += WHITE_BOX
     idx += 1
#is the word correct?
if guess == SECRET:
    print(emoji)
    print("Woo! You got it!")
else:
    print(emoji)
    print("Not quite. Play again soon!")

