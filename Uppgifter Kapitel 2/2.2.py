x = "25"
y = 8.5
others = ["3.14", "100", "7", "2.5"]

print(int(x))
print(float(x))

print(int(y))
print(str(y))

# for i in others:
#    print("\n")
#    print(int(i))
#    print(float(i))

for i in others:
    print("")
    print(int(float(i)))
    print(float(i))