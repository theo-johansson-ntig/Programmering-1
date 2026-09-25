import data
import random

def damage(attacker, target):
    attacker_weapon = attacker.weapon or 1
    target_armor = target.armor or 1
    return round(attacker.dmg * attacker_weapon * target_armor * random.uniform(0.8, 1.25))

while True:
    player = data.player()

    print(f"Current health: {player.hp}")
    input(f"1) {data.action[0]} 2) {data.action[1]} 3) {data.action[2]} 4) {data.action[3]}\n")
