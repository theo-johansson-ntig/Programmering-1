import random

random_list = []
largest = 0
smallest = 1000

for i in range(100):
    random_list.append(random.randint(1, 1001))

for i in random_list:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print(random_list)
print(f"\nStörsta talet: {largest} | Minsta talet: {smallest}")