import re

def validering(k, p):
    return (k + sum(p)) % 10 == 0

pnum = [int(d) for d in (re.sub(r'[^0-9]', '', input("Ange personnummer: ")))]    
if len(pnum) == 12:
    pnum = pnum[2:]
kontroll = pnum[-1]
pnum_luhn = []

for i in range(len(pnum)-1):
    double = pnum[i] * 2
    if i % 2 == 0:
        if double >= 10:
            pnum_luhn.extend([int(d) for d in str(double)])
        else:
            pnum_luhn.append(double)
    else:   
        pnum_luhn.append(pnum[i])
    
if validering(kontroll, pnum_luhn):
    print("Personnumret är giltigt")
else:
    print("Personnumret är inte giltigt")
    
print(pnum)
print(pnum_luhn)
print(sum(pnum_luhn))
print(kontroll)