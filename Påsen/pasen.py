from os import system
from sys import exit
from time import sleep
from termcolor import colored, cprint
from re import match

def act(name):
    actions[name]()

def view():
    print(colored("I påsen finns:\n", "yellow", attrs=["underline"]) + ", ".join(bag))

def save():
    item_s = input("Vad vill du lägga i påsen?\n")
    if not item_s:
        print("Felaktig input")
    else:
        bag.append(item_s)
        print(f"{item_s} finns nu i påsen.")

def take(): 
    item_r = input("Vad vill du ta ut ur påsen?\n")
    if item_r in bag:
        bag.remove(item_r)
        print(f"Du tog ut '{item_r}' ur påsen.")
    else:
        print(f"Du kunde inte hitta '{item_r}' i påsen.")

def find():
    item_f = input("Vad vill du leta efter i påsen?\n")
    if item_f in bag:
        print(f"Du hittade '{item_f}' i påsen!")
    else:
        print(f"Du kunde inte hitta '{item_f}' i påsen.")

def num_key(s):
    return int(match(r"\d+", s).group()) # inte min kod

def sort_bag():
    srt_alpha = sorted((i for i in bag if i[0].isalpha()), key=str.lower)
    srt_num = sorted((i for i in bag if i[0].isdigit()), key=num_key)
    srt_rest = sorted(i for i in bag if not i[0].isdigit() and not i[0].isalpha())
    bag[:] = srt_alpha + srt_num + srt_rest
    print("Du sorterade påsen.")


actions = {
    "v": view,
    "s": save,
    "t": take,
    "f": find,
    "o": sort_bag,
    "q": exit,
}

bag = []

while True:
    system("clear||cls")
    cprint("[V] Visa innehållet i påsen\n[S] Spara i påsen\n[T] Ta ut ur påsen\n[F] Leta (finns) i påsen\n[O] Sortera påsen\n[Q] Avsluta programmet\n", "yellow", attrs=["bold"])

    action = input().lower()
    if action in ("v", "s", "t", "f", "o", "q"):
        system("clear||cls")
        act(action)
    else:
        print("Felaktig input")
        sleep(3)
        continue
    
    if action == "v":
        sleep(5)
    else:
        sleep(2)




