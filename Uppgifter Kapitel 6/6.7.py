import re

m = []

while True:
    s = input('? ')
    if re.search("[^0123456789 ]", s) != None:
        print("Du måste ange giltiga värden")
        continue
    if s == '':
        break
    ls = s.split()
    rad = [float(e) for e in ls]
    m.append(rad)
