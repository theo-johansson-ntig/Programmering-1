import random

def show_status(player_hp, monster_hp):
    print(f"Player: {player_hp} HP | Monster: {monster_hp} HP")
    print("\n--------------------\n")

def show_menu():  
    for i in ACTIONS:
        action = ACTIONS[i]
        print(f"{i}) {action["name"]}")

def player_move(choice):
    action = ACTIONS[choice]
    if random.randint(1, 100) > action["accuracy"]:
        return action["type"], 0
    else:
        return action["type"], random.randint(action[min], action[max])




ACTIONS = {
    1: {"name": "Svärdshugg", "type": "attack", "min": 15, "max": 20, "accuracy": 95,},
    2: {"name": "Eldklot", "type": "attack", "min": 35, "max": 40, "accuracy": 50,},
    3: {"name": "Läkande dryck", "type": "heal", "min": 20, "max": 20, "accuracy": 100,},
}

show_menu()
