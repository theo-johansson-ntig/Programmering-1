li_input = input("Ange listans element separerade med mellanslag:\n")
tu_input = input("Ange tupelns element separerade med mellanslag:\n")

li = li_input.split()
tu = tuple(tu_input.split())

if list(tu) == li:
    print("Likadana")
else:
    print("Annorlunda")

same = len(li) == len(tu)
if same:
    for i in range(len(li)):
        if li[i] != tu[i]:
            same = False
if same:
    print("Likadana")
else:
    print("Annorlunda")

