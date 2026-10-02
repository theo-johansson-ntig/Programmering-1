# Leta efter det sista vita tecknet i en text
s = input("Skriv en text: ")
sr = s[::-1]
i = 0       # i används som räknare

for c in sr:
    if c == " " or c == "\t":
        break
    i = i + 1
if i < len(s):
    index = len(s) - i - 1
    print(f"Sista vita tecken finns på plats nr {index}")
else:
    print("Inget vitt tecken")