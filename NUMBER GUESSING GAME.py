#1 NUMBER GUESSING GAME

import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    while True:
        # Ask the user to guess the number
        guess = input("Guess a number between 1 and 100: ")
        
        # Try to convert the user input into an integer
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess < secret_number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")

if __name__ == "__main__":
    guess_number()