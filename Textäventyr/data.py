import random

# Weapons
weapons = {
    "Sword": 1.25,
    "Bow": 1.5,
    "Crossbow": 1.75,
    "Handgun": 2.25,
    "Assault Rifle": 3,
}

# Armor
armors = {
    "Apron": 0.9,
    "Chainmail": 0.8,
    "Kevlar": 0.6,
    "Breastplate": 0.5,
    "Exoskeleton": 0.4,
}

# Player
class player:
    name = "Player"
    hp = 100
    dmg = 10
    weapon = None
    armor = None

# Boss
class boss:
    hp = 500
    dmg = 35
    weapon = None
    armor = None

# Enemies
class zombie:
    name = "Zombie"
    hp = 50
    dmg = 8
    weapon = None
    armor = None

class skeleton:
    name = "Skeleton"
    hp = 20
    dmg = 16
    weapon = None
    armor = None

class wolf:
    name = "Wolf"
    hp = 35
    dmg = 12
    weapon = None
    armor = None

# Random enemy
enemies = [zombie, skeleton,]
def random_enemy():
    return random.choice(enemies)()