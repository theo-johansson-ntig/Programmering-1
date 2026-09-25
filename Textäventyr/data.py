# Weapons
sword = 1.25

# Armor
breastplate = 0.8

# Entities
class player:
    hp = 100
    dmg = 10
    weapon = None
    armor = None

class zombie:
    hp = 25
    dmg = 7
    weapon = None
    armor = None

class boss:
    hp = 250
    dmg = 25
    weapon = None
    armor = None

# Actions
action = ("Fight", "Random Weapon", "Random Armor", "Rest")