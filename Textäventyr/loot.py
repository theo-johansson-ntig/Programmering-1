import random
import data

weapon_pool = data.weapons 
weapon_weights = [16, 8, 4, 2, 1]

armor_pool = data.armors
armor_weights = [16, 8, 4, 2, 1]

def weapon_loot():
    return random.choices(weapon_pool, weights=weapon_weights, k=1)[0]

def armor_loot():
    return random.choices(armor_pool, weights=armor_weights, k=1)[0]