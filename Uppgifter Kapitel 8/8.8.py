def medelvärde(lista):
    summa = 0
    for i in lista:
        summa += i
    medel = summa / len(lista)
    return medel

print(medelvärde([4, 8, 15, 16, 23, 42]))