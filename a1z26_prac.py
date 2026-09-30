import random

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
swedish = [ "Å", "Ä", "Ö"]

lang = input("1) A1Z26 2) A1Ö29\n")
if lang == "2":
    alphabet.extend(swedish)

while True:
    mode = input("1) Encode 2) Decode\n")
    while mode == "1":
        letter = random.choice(alphabet)
        position = alphabet.index(letter) + 1
        print(f"\n{letter}")
        if int(input()) == position:
            print("Correct!")
        else:
            print(f"Incorrect! {letter} = {position}")
    while mode == "2":
        letter = random.choice(alphabet)
        position = alphabet.index(letter) + 1
        print(f"\n{position}")
        if input().upper() == alphabet[position-1]:
            print("Correct!")
        else:
            print(f"Incorrect! {position} = {letter}")