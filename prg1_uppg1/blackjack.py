import random
import time
import re

suits = ["♣", "♦", "♥", "♠"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = [suit + value for suit in suits for value in values]

def actions(action):
    if action == "1":
        card_deal(player_hand)
    elif action == "2":
        while hand_value(dealer_hand) < 17:
            card_deal(dealer_hand)
    elif action == "3":
        if bet <= (balance/2):
            balance -= bet
            bet *= 2
        card_deal(player_hand)
        while hand_value(dealer_hand) < 17:
            card_deal(dealer_hand)

def card_deal(hand):
    dealt_card = random.choice(deck)
    hand.append(dealt_card)
    deck.remove(dealt_card)

def card_parse(card):
    return re.sub("[^A-Za-z0-9]", "", card)

def hand_value(hand):
    value = 0
    for i in hand:
        k = card_parse(i)
        if k.isdigit():
            k = int(k)
            value += k
        elif k in ("J", "Q", "K"):
            value += 10
        elif k == "A":
            if (value + 11) > 21:
                value += 1
            else:
                value += 11
        else:
            print("Error in function hand_value")
    return value

def hand_parse(hand):
    return re.sub("[^A-Za-z0-9♣♦♥♠, ]", "", str(hand))

def is_natural(hand):
    if len(hand) == 2 and hand_value(hand) == 21:
        return True
    else:
        return False

while True:
    balance = 1000
    while True:
        print(f"Current Balance: {balance}")
        bet = int(input("Input bet: "))
        if bet > balance:
            bet = balance
        balance -= bet

        deck = [suit + value for suit in suits for value in values]
        player_hand = []
        dealer_hand = []

        for i in range(2):
            card_deal(player_hand)
        card_deal (dealer_hand)

        print(f"Your hand: {hand_parse(player_hand)}\n{hand_value(player_hand)}\n")
        if is_natural(player_hand):
            print("Natural!\n")
            balance += (2.5*bet)
            continue
        print(f"Dealer's hand: {hand_parse(dealer_hand)}\n{hand_value(dealer_hand)}\n")
        time.sleep(1)

        print("1) Hit | 2) Stand | 3) Double Down | 4) Split | 5) Surrender")
        actions(input("Select action: "))



