import random

def damage(attacker, target):
    attacker_weapon = attacker.weapon or 1
    target_armor = target.armor or 1
    return round(attacker.dmg * attacker_weapon * target_armor * random.uniform(0.8, 1.25))

def attack(attacker, target):
    dmg = damage(attacker, target)
    target.hp -= dmg
    print(f"{attacker.name} dealt {dmg} damage to {target.name}!")

def heal(attacker, target):
    healing = round(attacker.hp * 0.15 * random.uniform(0.8, 1.25))
    attacker.hp += healing
    print(f"{attacker.name} healed {attacker.name} by {healing} HP!")

def profile(char):
    print(f"Name: {char.name}\nHealth: {char.hp}\nDamage: {char.dmg}\nWeapon: {char.weapon}\nArmor: {char.armor}")

def player_profile(attacker, target):
    profile(attacker)

def enemy_profile(attacker, target):
    profile(target)
   
actions = {
    "1": attack,
    "2": heal,
    "3": player_profile,
    "4": enemy_profile,
}




