summa = 1000

while True:
    print(f"\nKontosaldo: {summa}")
    handling = int(input("1) Kontoinsättning | 2) Kontoutdrag | 3) Avsluta\n"))
    if handling == 1:
        summa += int(input("Ange hur mycket som ska sättas in\n"))
    elif handling == 2:
        belopp = int(input("Ange hur mycket som ska tas ut\n"))
        if belopp > summa:
            print("Du kan inte ta ut mer pengar än vad som finns på kontot.")
        else:
            summa -= belopp
    elif handling == 3:
        break
    else:
        print("Felaktig input.")
    