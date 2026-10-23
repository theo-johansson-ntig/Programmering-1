num_list = list(map(int, input("Ange tal separerade med mellanslag: ").split()))

while True:
    try:
        num_list.remove(0)
    except ValueError:
        break

print(num_list)