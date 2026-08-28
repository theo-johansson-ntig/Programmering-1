length = input("Golvets längd: ")
width = input("Golvets bredd: ")

if length.isdigit():
    length = int(length)
else:
    length = float(length)

if width.isdigit():
    width = int(width)
else:
    width = float(width)

area = length * width

print(f"Du behöver {area}m² golv.")