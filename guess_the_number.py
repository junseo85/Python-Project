
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
random_number = random.randint(0, 100)

hard = 5


def guess_number(difficulty):
    if difficulty == 'easy':
        easy = 10
        user_input = int(input("Make a guess: "))
        make_guess = True
        while make_guess is True:
            if user_input > random_number:
                easy -= 1
                print("Too high.")
                print("Guess again.")
                print(f"You have {easy} attemps remaining to guess the number.")
                user_input = int(input("Make a guess: "))

            if user_input < random_number:
                easy -= 1
                print("Too low.")
                print("Guess again.")
                print(f"You have {easy} attemps remaining to guess the number.")
                user_input = int(input("Make a guess: "))
            if user_input == random_number:
                print("you guessed it!")
                make_guess = False
            if easy <= 1:
                print("You've run out of guesses, you lose.")
                make_guess = False
    if difficulty == 'hard':
        hard = 5
        user_input = int(input("Make a guess: "))
        make_guess = True
        while make_guess is True:
            if user_input > random_number:
                hard -= 1
                print("Too high.")
                print("Guess again.")
                print(f"You have {hard} attemps remaining to guess the number.")
                user_input = int(input("Make a guess: "))

            if user_input < random_number:
                hard -= 1
                print("Too low.")
                print("Guess again.")
                print(f"You have {hard} attemps remaining to guess the number.")
                user_input = int(input("Make a guess: "))
            if user_input == random_number:
                print(f"you got it! The answer was {random_number}.")
                make_guess = False
            if hard <= 1:
                print("You've run out of guesses, you lose.")
                make_guess = False


guess_number(difficulty)