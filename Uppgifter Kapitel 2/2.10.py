old_price = float(input("Vad kostade tröjan ursprungligen? "))
discount = float(input("Vad är rabatten i %? "))
new_price = old_price*(1-(discount/100))

print(f"Tröjan kostar nu {new_price}")