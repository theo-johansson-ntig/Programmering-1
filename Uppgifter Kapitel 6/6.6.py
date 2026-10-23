a = []

upto = int(input("Tabell upp till: "))

for i in range(0, upto):
    a.append([])
    for j in range(0, upto):
        a[i].append((i+1)*(j+1))

max_len = len(str(upto**2)) + 1
row = f"{{:<{max_len}}}" * upto

for i in a:
    print(row.format(*i))