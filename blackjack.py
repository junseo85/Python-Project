from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
random_card = random.sample(cards, 2)
computer_start_card = random.sample(cards, 2)


def balckjack_game(random_card, computer_start_card):
    print(logo)
    game = {}
    computer = []
    current_score = 0
    computer_current_score = 0
    game["player"] = random_card
    game["computer"] = computer_start_card
    for num in game["player"]:
        current_score += num
    for numb in game["computer"]:
        computer_current_score += numb
    print(f"Your cards: {random_card}, current score: {current_score}")
    print(f"Computer's first card: {game['computer'][0]}")

    if computer_current_score == 21:
        print(f"Your final hand: {game['player']}, current score: {current_score}")
        print(f"Computer's final hand: {game['computer']}, current score: {computer_current_score}")
        print("Lose, opponent has Blackjack")
        play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
        if play_game == 'y':
            new_random = random.sample(cards, 2)
            new_computer_start_card = random.sample(cards, 2)
            balckjack_game(new_random, new_computer_start_card)

    if current_score > 21 and current_score > computer_current_score:
        print(f"Your final hand: {game['player']}, current score: {current_score}")
        print(f"Computer's final hand: {game['computer']}, current score: {computer_current_score}")
        print("You went over. You lose")
        play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
        if play_game == 'y':
            new_random = random.sample(cards, 2)
            new_computer_start_card = random.sample(cards, 2)
            balckjack_game(new_random, new_computer_start_card)
    if current_score > 21 and current_score < computer_current_score:
        print(f"Your final hand: {game['player']}, current score: {current_score}")
        print(f"Computer's final hand: {game['computer']}, current score: {computer_current_score}")
        print("Computer went over. You win")
        play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
        if play_game == 'y':
            new_random = random.sample(cards, 2)
            new_computer_start_card = random.sample(cards, 2)
            balckjack_game(new_random, new_computer_start_card)
    if computer_current_score > 21 and computer_current_score > current_score:
        print(f"Your final hand: {game['player']}, current score: {current_score}")
        print(f"Computer's final hand: {game['computer']}, current score: {computer_current_score}")
        print("Computer went over. You win")
        play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
        if play_game == 'y':
            new_random = random.sample(cards, 2)
            new_computer_start_card = random.sample(cards, 2)
            balckjack_game(new_random, new_computer_start_card)
    if computer_current_score > 21 and computer_current_score < current_score:
        print(f"Your final hand: {game['player']}, current score: {current_score}")
        print(f"Computer's final hand: {game['computer']}, current score: {computer_current_score}")
        print("You went over. You lose")
        play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
        if play_game == 'y':
            new_random = random.sample(cards, 2)
            new_computer_start_card = random.sample(cards, 2)
            balckjack_game(new_random, new_computer_start_card)
    play_game = input("Type 'y' to get another card, type 'n' to pass:")
    if play_game == 'y':
        add_random_card = random.sample(cards, 1)
        game["player"] += add_random_card
        game["computer"] += random.sample(cards, 1)
        balckjack_game(random_card, computer_start_card)
    elif play_game == 'n':
        if current_score == computer_current_score:
            print(f"Your final hand: {game['player']}, current score: {current_score}")
            print(f"Computer's final hand: {game['computer']}, current score: {computer_current_score}")
            print("Draw")
            play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
            if play_game == 'y':
                new_random = random.sample(cards, 2)
                new_computer_start_card = random.sample(cards, 2)
                balckjack_game(new_random, new_computer_start_card)
        if current_score > computer_current_score:
            print(f"Your final hand: {game['player']}, current score: {current_score}")
            print(f"Computer's final hand: {game['computer']}, current score: {computer_current_score}")
            print("You win")
            play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
            if play_game == 'y':
                new_random = random.sample(cards, 2)
                new_computer_start_card = random.sample(cards, 2)
                balckjack_game(new_random, new_computer_start_card)
        if current_score < computer_current_score:
            print(f"Your final hand: {game['player']}, current score: {current_score}")
            print(f"Computer's final hand: {game['computer']}, current score: {computer_current_score}")
            print("You lose")
            play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
            if play_game == 'y':
                new_random = random.sample(cards, 2)
                new_computer_start_card = random.sample(cards, 2)
                balckjack_game(new_random, new_computer_start_card)


play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")

if play_game == 'y':
    balckjack_game(random_card, computer_start_card)

