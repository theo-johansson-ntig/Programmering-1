import random

numbers = [random.randint(1, 50) for i in range(20)]
numbers_odd = [i for i in numbers if (i % 2) == 1]
numbers_even = [i for i in numbers if (i % 2) == 0]

print(numbers_odd)
print(numbers_even)