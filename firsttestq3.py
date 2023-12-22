import random

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("Welcome to the Number Guessing Game! Guess a number between 1 and 100.")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number!")
            return

    print(f"Game over! You've run out of guesses. The number was {number_to_guess}.")

guess_number_game()
