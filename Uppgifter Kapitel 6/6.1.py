const = 3
seq = [2]
length = int(input("Ange ")) - 1

for i in range(length):
    seq.append(seq[i] * const)

print(seq)