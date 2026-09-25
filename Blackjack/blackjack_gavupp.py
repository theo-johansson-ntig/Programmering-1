import random
import time
import re

suits = ["♣", "♦", "♥", "♠"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def new_deck():
    return [suit + value for suit in suits for value in values]

def random_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def hit(hand, deck):  
    hand.append(random_card(deck))
    return hand_value(hand) > 21 # True if busted

def dealer_play(dealer_hand, deck):
    while hand_value(dealer_hand) < 17:
        hit(dealer_hand, deck)
    return hand_value(dealer_hand) # returns dealer hand value

def card_parse(card): # removes symbols leaving only the value of the card
    return re.sub("[^A-Za-z0-9]", "", card)

def hand_parse(hand): # card_parse but for entire hand
    return re.sub("[^A-Za-z0-9♣♦♥♠, ]", "", str(hand))

def hand_value(hand): # uses card_parse and checks combined value of all cards in hand
    value = 0
    for i in hand:
        k = card_parse(i)
        if k.isdigit():
            k = int(k)
            value += k
        elif k in ("J", "Q", "K"):
            value += 10
        elif k == "A":
            value += 11 if (value + 11) <= 21 else 1
    return value

def is_natural(hand):
    return len(hand) == 2 and hand_value(hand) == 21

while True:
    balance = 1000
    while balance > 0:
        print(f"\nBalance: {balance}") # bet size and balance check
        bet = int(input("Enter bet: "))
        if bet > balance:
            bet = balance
        balance -= bet

        deck = new_deck() # reset hands and deck
        player_hand = [] 
        dealer_hand = []

        for i in range(2): # 2 cards to player, 1 card to dealer
            hit(player_hand, deck)
        hit(dealer_hand, deck)

        if is_natural(player_hand):
            print("Natural!")
            time.sleep(1)
            balance += int(bet * 2.5)
            continue


        busted = False
        while True:
            print(f"\nDealer's hand: {hand_parse(dealer_hand)} ({hand_value(dealer_hand)})") # prints current hands and awaits action
            print(f"Your hand: {hand_parse(player_hand)} ({hand_value(player_hand)})")
            action = input("\n1) Hit | 2) Stand\n")

            if action == "1":
                if hit(player_hand, deck):
                    print("Bust!")
                    busted = True
                    time.sleep(1)
                    break
            elif action == "2":
                break

        if not busted:
            dealer_total = dealer_play(dealer_hand, deck)
            player_total = hand_value(player_hand)
            print(f"Dealer's hand: {hand_parse(dealer_hand)} ({hand_value(dealer_hand)})")
            print(f"Your hand: {hand_parse(player_hand)} ({hand_value(player_hand)})")

            if dealer_total > 21:
                print("Dealer bust! You win!")
                balance += bet*2
                time.sleep(1)
            elif dealer_total > player_total:
                print("Dealer wins! You lose!")
                time.sleep(1)
            elif dealer_total == player_total:
                print("Push! Bet refunded!")
                time.sleep(1)
            else:
                print("You win!")
                balance += bet*2
                time.sleep(1)
       
    print("You're out of money!")
    time.sleep(1)
    if input("Play again? (y/n): ").lower() != "y":
        break   

