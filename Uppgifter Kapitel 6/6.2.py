import random

random_list = []
negatives = 0
for i in range(random.randint(1, 101)):
    random_list.append(random.randint(-1000, 1001))

for i in random_list:
    if i < 0:
        negatives += 1

print(random_list)
print(f"\nAv {len(random_list)} tal är {negatives} av dem negativa.")