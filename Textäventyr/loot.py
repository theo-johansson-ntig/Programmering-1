import random
import data

weapon_pool = data.weapons 
weapon_weights = [16, 8, 4, 2, 1]

armor_pool = data.armors
armor_weights = [16, 8, 4, 2, 1]

def loot():
    if random.randint(1, 2) == 1:
        pool = weapon_pool
        weights = weapon_weights
    else:
        pool = armor_pool
        weights = armor_weights
    return random.choices(pool, weights=weights, k=1)[0]
