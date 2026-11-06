from os import system
from time import sleep

temps = []
aa_temps = []

while True:
    system("clear||cls")
    user_temp = input("Ange temperatur:\n")
    if user_temp == "":
        if not temps:
            print("Inga temperaturer angivna")
            sleep(1)
        else:
            break
    else:
        try:
            temps.append(float(user_temp))
        except ValueError:
            print("Ogiltigt värde")
            sleep(1)
            continue

avg_temp = sum(temps) / len(temps)

print(f"Medeltemperatur: {avg_temp:.1f}°")

for station, temp in enumerate(temps, start=1):
    if temp > avg_temp:
        print(f"Station {station}: {temp:.1f}°")


