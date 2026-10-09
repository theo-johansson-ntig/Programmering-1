from os import system
from random import choice
from time import sleep

# Språk
eng = {
    "word_prompt": "Enter a word for the opponent to guess: ",
    "invalid_word": "You must enter a valid word!",
    "prev_guesses": "Guesses: ",
    "enter_guess": "Enter guess: ",
    "invalid_guess": "Guess is invalid!",
    "player_lose": "You lost! The word was ",
    "player_win": "You won! The word was "
}
swe = {
    "word_prompt": "Ange ett ord som motståndaren ska gissa: ",
    "invalid_word": "Du måste välja ett giltigt ord!",
    "prev_guesses": "Gissningar: ",
    "enter_guess": "Ange gissning: ",
    "invalid_guess": "Gissning är inte giltig!",
    "player_lose": "Du förlorade! Ordet var ",
    "player_win": "Du vann! Ordet var "
}

# Välj språk
lang = eng

# Välj om valda ord måste finnas i den engelska ordboken (max 15 bokstäver)
force_engdic = False

class new_man:
    head = " O"
    torso = "|"
    l_arm = "/"
    r_arm = "\\"
    l_leg = "/"
    r_leg = "\\"

def remove_limb():
    if health >= 3:
        names = ["l_arm", "r_arm", "l_leg", "r_leg"]
        available = [n for n in names if getattr(man, n) != " "]
        if available:
            setattr(man, choice(available), " ")
    elif health == 2:
        man.torso = " "
    else:
        man.head = " "

while True:
    # Rensa terminalen för ny omgång
    system("clear||cls")

    # Ta ord som input, kolla om det är giltigt
    while True: 
        word = input(lang["word_prompt"]).upper().strip()

        # Se till att ordet endast använder bokstäver
        if not word.isalpha():
            print(lang["invalid_word"] + "\n")
            sleep(1)
            continue

        # Kolla om ordet finns i engelsk ordbok
        if force_engdic:
            in_dic = False
            with open("CSW24.txt") as d:
                for line in d:
                    if word == line.strip():
                        in_dic = True
                        break
            if not in_dic:
                print(lang["invalid_word"] + "\n")
                sleep(1)
                continue
        break
    
    # Nollställ spelet
    man = new_man() 
    health = 6
    known = ["_"] * len(word)
    guesses = []

    while True:
        # Rensa terminalen efter varje gissning
        system("clear||cls")

        # Printa HUD
        print("\n" + "\u2764 " * health)
        print(man.head + "\n" + man.l_arm + man.torso + man.r_arm + "\n" + man.l_leg + " " + man.r_leg)
        print(" ".join(known))
        print(lang["prev_guesses"] + ", ".join(guesses) + "\n")

        correct = False
        guess = input(lang["enter_guess"]).upper() # Ta input från spelare
        if guess in guesses or len(guess) != 1 or not guess.isalpha(): # Se till att gissning är giltig
            print(lang["invalid_guess"])
            sleep(1)
            continue
        else:
            guesses.append(guess) # Lägg till gissning till listan guesses

        for i in range(len(word)): # Kolla om bokstav finns i ordet
            if word[i] == guess:
                known[i] = guess
                correct = True  
        if not correct: # Ta bort kroppsdel och minska spelarens HP om gissning är fel
            remove_limb()
            health -= 1

        # Rensa terminal innan vinst/förlustmeddelande
        system("clear||cls")

        if health == 0:
            print(lang["player_lose"] + f"'{word}'\n")
            sleep(2)
            break
        
        if "".join(known)  == word:
            print(lang["player_win"] + f"'{word}'\n")
            sleep(2)
            break


