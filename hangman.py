head = " O"
torso = "|"
l_arm = "/"
r_arm = "\\"
l_leg = "/"
r_leg = "\\"

while True:
    man = head + "\n" + l_arm + torso + r_arm + "\n" + l_leg + " " + r_leg
    print(man)
    word = input("Ange ett ord som motståndaren ska gissa: ")
    word_hint = "_" * len(word)



