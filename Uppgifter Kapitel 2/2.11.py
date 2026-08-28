ticket_price = 120
popcorn_price = 50
soda_price = 25

ticket_amount = int(input("Hur många biobiljetter ska köpas? "))
popcorn_amount = int(input("Hur många popcornlådor ska köpas? "))
soda_amount = int(input("Hur många läsker ska köpas? "))

total_ticket = ticket_price*ticket_amount
total_popcorn = popcorn_price*popcorn_amount
total_soda = soda_price*soda_amount

print(f"\nHela biobesöket kostar {total_ticket+total_popcorn+total_soda}")
print(f"Biobiljetter: {total_ticket} | Popcorn: {total_popcorn} | Läsk: {total_soda}")