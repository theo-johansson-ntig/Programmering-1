string = input("Ange text:\n").lower()

if string[:1] == string[-1]:
    print("Första och sista bokstaven är samma")
else:
    print("Första och sista bokstaven är inte samma")
