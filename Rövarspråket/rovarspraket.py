from os import system
from sys import exit

consonants = set("bcdfghjklmnpqrstvwxz")

def format_s_to_r(text):
    return text.replace("X", "Ks").replace("x", "ks")

def swedish_to_rovar(text):
    result = []
    text = format_s_to_r(text).strip()
    for x in text:
        if x.lower() in consonants:
            result.append(x + "o" + x.lower())
        else:
            result.append(x)
    return "".join(result)

def rovar_to_swedish(text):
    result = []
    i = 0
    text = text.strip()
    while i < len(text):
        result.append(text[i]) 
        if text[i].lower() in consonants:
            if i+2 >= len(text) or text[i+1].lower() != "o" or text[i].lower() != text[i+2].lower():
                return False
            else:
                i += 3
        else:
            i += 1
    return "".join(result)

def invalid_input():
    system("clear||cls")
    print("Felaktig input")
    input()


while True:
    system("clear||cls")
    choice = input("1) Rövarspråk till svenska\n2) Svenska till rövarspråk\n3) Avbryt programmet\n").strip()

    if choice not in ("1", "2", "3"):
        invalid_input()
        continue
    
    system("clear||cls")
    if choice == "1":
        string = input("RÖVARSPRÅK TILL SVENSKA\nAnge sträng att översätta:\n").strip()
        translated = rovar_to_swedish(string)
    elif choice == "2":
        string = input("SVENSKA TILL RÖVARSPRÅK\nAnge sträng att översätta:\n").strip()
        translated = swedish_to_rovar(string)
    elif choice == "3":
        exit()

    if translated is False:
        invalid_input()
        continue

    system("clear||cls")

    print(f'"{string}"\n->\n"{translated}"')
    input()