import random
import time

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
            setattr(man, random.choice(available), " ")
    elif health == 2:
        man.torso = " "
    else:
        man.torso = " "

while True:
    man = new_man()
    health = 6
    word = input("Ange ett ord som motståndaren ska gissa: ").upper()
    hint = ["_"] * len(word)
    guesses = []
    print("\n" * 100)
    
    while True:
        print("\n" + "\u2764 " * health)
        print(man.head + "\n" + man.l_arm + man.torso + man.r_arm + "\n" + man.l_leg + " " + man.r_leg)
        print(" ".join(hint))
        print(f"Gissningar: {", ".join(guesses)}\n")

        correct = False
        guess = input("Ange gissning: ").upper()
        if guess in guesses or len(guess) != 1:
            print("Du kan inte gissa det!")
            time.sleep(0.7)
            continue
        else:
            guesses.append(guess)

        for i in range(len(word)):
            if word[i] == guess:
                hint[i] = guess
                correct = True  
        if correct == False:
            remove_limb()
            health -= 1

        hint_clean = "".join(hint)
            
        if health == 0:
            print(f"Du förlorade! Ordet var '{word}'\n")
            break
        
        if hint_clean == word:
            print(f"Du vann! Ordet var '{word}'\n")
            break


