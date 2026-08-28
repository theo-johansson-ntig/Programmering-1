user_input = input("Skriv ett tal: ")

if user_input.isdigit():
    print(f"Det dubbla talet är {int(user_input)*2}")
else:
    print(f"Det dubbla talet är {float(user_input)*2}")