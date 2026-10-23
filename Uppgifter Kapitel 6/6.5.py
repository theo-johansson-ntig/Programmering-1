namn = []
pris = []

while True:
    s = input("Ange kontantkortets namn och pris: ")
    if s == "":
        break
    s = s.rpartition(" ")
    namn.append(s[0])
    pris.append(float(s[2]))

m = min(pris)
k = pris.index(m)
print(f"{namn[k]} är billigast")
print(f"Kostnad: {m:.2f} kr/månad")