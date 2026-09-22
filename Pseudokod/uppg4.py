from random import randint

tal = randint(1,20)
gissning = 0

while gissning != tal:
    gissning = int(input("Ange ett heltal mellan 1 och 20: "))
    if gissning < tal:
        print("För lågt!")
    elif gissning > tal:
        print("För högt!")
    else:
        print("Rätt!")