# Översätt amerikanskt datum till svensk form
a = input("Skriv ett amerikanskt datum som mm/dd/åå: ")
månad = a[:2]
dag = a[3:5]
år = a[6:]
s1 = "20" + år + "-" + månad + "-" + dag
s2 = dag + "/" + månad

print("ÅÅÅÅ-MM-DD: " + s1)
print("DD/MM: " + s2)