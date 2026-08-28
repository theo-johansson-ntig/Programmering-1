length = input("Vad är rektangelns längd? ")
width = input("Vad är rektangelns bredd? ")

if length.isdigit():
    length = int(length)
else:
    length = float(length)

if width.isdigit():
    width = int(width)
else:
    width = float(width)

circumference = (2*length) + (2*width)
area = length * width

print(f"\nRektangelns omkrets är {circumference}")
print(f"Rektangelns area är {area}")