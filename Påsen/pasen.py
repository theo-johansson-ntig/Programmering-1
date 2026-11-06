from os import system

bag = []

menu = {
    "view": "[V] Visa innehållet i påsen",
    "save": "[S] Spara i påsen",
    "find": "[F] Leta (finns) i påsen",
    "quit": "[Q] Avsluta programmet",
}

def view():
    print("I påsen finns just nu:\n" + ", ".join(bag))

def save():
    item = input("Vad vill du lägga i påsen?\n")
    bag.append(item)
    print(f"{item} är nu i påsen")

def find():
    

while True:
    system("clear||cls")
    print("\n".join(menu.values()))
    action = input()
