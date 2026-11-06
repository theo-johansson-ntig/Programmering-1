values = sorted(map(int, input("Ange värden separerade med mellanslag:\n").split()))

for i in range((len(values)-1)//2):
    values = values[1:-1]

median = sum(values)/len(values)

if median.is_integer():
    print(int(median))
else:
    print(median)
