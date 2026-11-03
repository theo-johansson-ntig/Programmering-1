import queue
from os import system
from time import sleep

numbers = []
processed = []

while True:
    system("clear||cls")
    num = input("Ange tal:\n")
    if num == "":
        break
    else:
        try:
            numbers.append(int(num))
        except ValueError:
            print("Felaktigt värde")
            sleep(1)
            continue

while numbers:
    a = numbers[0]
    if a not in processed:
        processed.append(a)
    numbers.pop(0)

print(", ".join(map(str, processed)))