from os import system
from random import choice
from time import sleep

# Välj om valda ord måste finnas i den engelska ordboken (max 15 bokstäver)
force_engdic = True

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

    # Ta ord som input, kolla om det är giltigt ifall force_engdic == True
    while True: 
        word = input("Ange ett ord som motståndaren ska gissa: ").upper()
        if force_engdic:
            in_dic = False
            with open("CSW24.txt") as d:
                for line in d:
                    if word == line.strip():
                        in_dic = True
                        break
            if in_dic == False:
                print("Du måste välja ett giltigt ord!\n")
                sleep(1)
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
        print(f"Gissningar: {", ".join(guesses)}\n")

        correct = False
        guess = input("Ange gissning: ").upper() # Ta input från spelare
        if guess in guesses or len(guess) != 1: # Se till att gissning är giltig
            print("Du kan inte gissa det!")
            sleep(1)
            continue
        else:
            guesses.append(guess) # Lägg till gissning till listan guesses

        for i in range(len(word)): # Kolla om bokstav finns i ordet
            if word[i] == guess:
                known[i] = guess
                correct = True  
        if correct == False: # Ta bort kroppsdel och minska spelarens HP om gissning är fel
            remove_limb()
            health -= 1

        known_clean = "".join(known) 
            
        if health == 0:
            print(f"Du förlorade! Ordet var '{word}'\n")
            sleep(2)
            break
        
        if known_clean == word:
            print(f"Du vann! Ordet var '{word}'\n")
            sleep(2)
            break


