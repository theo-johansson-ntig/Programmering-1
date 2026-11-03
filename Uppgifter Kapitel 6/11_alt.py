import random

numbers_odd = []
numbers_even = []

numbers = [random.randint(1, 50) for i in range(20)]

# for i in numbers:
#     if i % 2 == 1:
#         numbers_odd.append(i)
#     else:
#         numbers_even.append(i)

for i in numbers:
    (numbers_odd if i % 2 == 1 else numbers_even).append(i)

print(numbers_odd)
print(numbers_even)