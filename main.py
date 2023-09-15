#Hangman game
from replit import clear
import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
logo = hangman_art.logo
stages = hangman_art.stages
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
print(logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:

        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
