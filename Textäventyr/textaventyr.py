import data
import action
import time
import random

while True:
    player = data.player() # Nollställ spelet
    enemy = None
    alive = True
    boss_defeated = False

    while alive:

        if enemy == None: # Skapar ny enemy efter den förra dör
            enemy = data.random_enemy()

        print(f"\n{player.name} health: {player.hp}\n{enemy.name} health: {enemy.hp}")

        act = input("\n1) Attack 2) Heal 3) Player info 4) Enemy info 5) Fight boss\n")

        action.actions[act](player, enemy)

        if enemy.hp > 0 and act in ("1", "2"): # Om enemy fortfarande lever, låt enemy attackera player
            action.attack(enemy, player)
            if player.hp < 0: # Kolla om spelare är död
                alive = False
        elif enemy.hp <= 0: # Se till att enemy är död 
            print(f"{enemy.name} defeated!")
            enemy = None
            if random.randint(1,2) == 1:
                
        time.sleep(0.8)

    if boss_defeated:
        print(f"Congratulations! You win!")
    else:
        print(f"You died! Game over!")
    time.sleep(5)