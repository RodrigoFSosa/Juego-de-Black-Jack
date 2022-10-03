############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random
from replit import clear


def blackjack():
    print(logo)

    player_cards = []
    computer_cards = []

    for i in range(2):
        random_card = random.choice(cards)
        player_cards.append(random_card)

    player_score = player_cards[0] + player_cards[1]
    random_card = random.choice(cards)
    computer_cards.append(random_card)
    computer_score = random_card

    if player_score > 21:
        player_cards = as_card(player_cards)

    give_card = True

    while give_card:

        print(f"Your cards: {player_cards}, current score: {player_score}")

        print(f"Computer's first card: {computer_cards[0]}")
        get_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if get_card == "y":
            player_score = another_card(player_score, player_cards)
        else:
            give_card = False

        if player_score >= 21:
            give_card = False

    print(f"Your final hand: {player_cards}, final score: {player_score}")

    while computer_score <= 17:
        computer_score = another_card(computer_score, computer_cards)

    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}"
    )

    if player_score > 21:
        print("You went over. You lose 😤")

    elif computer_score > 21:
        print("Opponent went over. You win 😁")

    elif player_score > computer_score:
        print("You Win 😃")

    elif player_score == computer_score:
        print("Draw 🙃")

    elif computer_score > player_score:
        print("You lose 😤")


def another_card(score, hand):
    random_card = random.choice(cards)
    hand.append(random_card)
    score += random_card
    if score > 21:
        hand = as_card(hand)
        score = 0
        for value in hand:
            score += value
    return score


def computers_hand(score, hand):
    random_card = random.choice(cards)
    hand.append(random_card)
    score += random_card
    return score


def as_card(list):
    len_list = len(list)
    for item in range(len_list):
        if list[item] == 11:
            list[item] = 1
    return list


end_game = False
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while not end_game:

    start_game = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if start_game == "y":
        clear()
        blackjack()
    else:
        end_game = True
