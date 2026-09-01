import random
import time

pokedex = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran♀", "Nidorina", "Nidoqueen", "Nidoran♂", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]
shiny_odds = 256

def txt_increment(filename):
    with open("{}.txt".format(filename), "r") as f:
        counter = int(f.read())
    counter += 1
    with open("{}.txt".format(filename), "w") as f2:    
        f2.write(f"{str(counter)}")

def txt_decrement(filename):
    with open("{}.txt".format(filename), "r") as f:
        counter = int(f.read())
    counter -= 1
    with open("{}.txt".format(filename), "w") as f2:    
        f2.write(f"{str(counter)}")

def shiny_check(odds):
    if random.randint(1, odds) == 1:
        return "(Shiny)"
    else:
        return "(Normal)"
    
def attack():
    if random.random() >= 0.5:
        txt_increment("pokeball")
    if random.random() >= 0.75:
        txt_increment("great_ball")
    if random.random() >= 0.9:
        txt_increment("ultra_ball")

def ball_check(filename):
    with open("{}.txt".format(filename), "r") as f:
        if int(f.read()) >= 1:
            return True
        else:
            return False

def action(type):
    if type == 1:
        return "attack"
    elif type == 2:
        return "pokeball"
    elif type == 3:
        return "great_ball"
    elif type == 4:
        return "ultra_ball"
    elif type == 5:
        return "items"
    elif type == 6:
        return "box"
    else:
        return False
    
def catch(ball_type):
    if ball_type == "pokeball":
        if random.random() <= 0.5:
            return True
        else:
            return False
    if ball_type == "great_ball":
        if random.random() <= 0.75:
            return True
        else:
            return False
    if ball_type == "ultra_ball":
        if random.random() <= 0.9:
            return True
        else:
            return False

def encounter(pmon):
    print(pmon)
    print("1) Attack | 2) Poké Ball | 3) Great Ball | 4) Ultra Ball | 5) View Items | 6) View Box")
    return input()


while True:
    print("")
    time.sleep(5)
    pokemon = (random.choice(pokedex) + " " + shiny_check(shiny_odds))
    move = action(int(encounter(pokemon)))

    if move == "items":
        print("")
        with open("pokeball.txt", "r") as f:
            print("Pokéballs: " + (f.read()))
        with open("great_ball.txt", "r") as f:
            print("Great Balls: " + (f.read()))
        with open("ultra_ball.txt", "r") as f:
            print("Ultra Balls: " + (f.read()))
        continue

    elif move == "box":
        print("")
        with open("pokemon.txt", "r") as f:
            print(f.read())


    elif move == "attack":
        attack()
        print("Attack success!")
        continue
    
    elif move != "items" or "box" or "attack":
        if ball_check(move):
            if catch(move):
                print("SUCCESS!")
                with open("pokemon.txt", "a") as f:
                    f.write("\n" + pokemon)
                txt_decrement(move)
                continue
            else:
                print("FAIL!")
                txt_decrement(move)
                continue
        else:
            print("You don't have that!")
            continue