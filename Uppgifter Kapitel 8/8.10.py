def hamta_betyg(poang):
    if poang >= 25:
        return "Godkänd"
    else:
        return "Underkänd"
    
elevpoang = {
    1: 32,
    2: 18,
    3: 25,
}

for i in elevpoang:
    print(f"Elev {i}: {hamta_betyg(elevpoang[i])}")