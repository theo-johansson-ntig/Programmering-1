import json
import hashlib

with open("db.json", "r") as file:
    data = json.load(file)

while True:
    un = input("Username: ").lower()
    user = next((u for u in data if u["username"] == un), None)
    
    if user is None:
        print("Incorrect username")
        continue

    pw = input("Password: ")
    if user["password"] == hashlib.sha256(pw.encode()).hexdigest():
        print(user["info"])
        break

    print("Incorrect password")
