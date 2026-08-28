price = float(input("Varans pris exkl. moms: "))
sales_tax = float(input("Varans momssats i %: "))

print(f"\nVarans pris exkl. moms: {price}")
print(f"Varans momssats i %: {sales_tax}%")
print(f"Varans pris inkl. moms: {price*(1+(sales_tax/100))}")