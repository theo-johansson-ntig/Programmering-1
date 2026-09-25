import data
import random

def damage(char, target):
    char_weapon = char["weapon"]
    target_armor = target["armor"]
    return random.uniform(0.8, 1.25) * char["dmg"]
